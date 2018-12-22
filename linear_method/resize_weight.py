import numpy as np
import functools

_vectorize_fp64 = functools.partial(np.vectorize, otypes=[np.float64])

@_vectorize_fp64
def box(x):
    """matlab.images.internal.resize.box"""

    return -0.5 <= x < 0.5

@_vectorize_fp64
def triangle(x):
    """matlab.images.internal.resize.triangle"""

    return (x + 1) * (-1 <= x < 0) + (1 - x) * (0 <= x <= 1)

@_vectorize_fp64
def cubic(x):
    """matlab.images.internal.resize.cubic"""

    absx = abs(x)
    absx2 = absx ** 2
    absx3 = absx ** 3

    return ((1.5 * absx3 - 2.5 * absx2 + 1) * (absx <= 1) + 
        (-0.5 * absx3 + 2.5 * absx2 - 4 * absx + 2) * (1 < absx <= 2))

@_vectorize_fp64
def lanczos2(x):
    """matlab.images.internal.resize.lanczos2"""

    eps = np.finfo(np.float64).eps

    return (np.sin(np.pi * x) * np.sin(np.pi * x / 2) + eps) / ((np.pi ** 2 * x ** 2 / 2) + eps) * (abs(x) < 2)

@_vectorize_fp64
def lanczos3(x):
    """matlab.images.internal.resize.lanczos2"""

    eps = np.finfo(np.float64).eps

    return (np.sin(np.pi * x) * np.sin(np.pi * x / 3) + eps) / ((np.pi ** 2 * x ** 2 / 3) + eps) * (abs(x) < 3)


def resize_weight(scale=2, kernel=None, downsample=False):
    """A function that outputs weights for a specified resizer

    This function assumes center-aligned interpolation.

    Args:
        scale: (int) Resize factor. The type of value for downscale is also an integer.
            Default is 2.
        
        kernel: (str) Interpolation method.
            Available methods: box, bilinear(triangle), bicubic(cubic), lanczos2, lanczos3.
            Default is 'bicubic'.
        
        downsample: (bool) Whether the weights are used for downsample instead of upsample.
            Default is False.
    
    Ref:
        [1] P. Getreuer. (2011). Linear Methods for Image Interpolation. Image Processing On Line, 1, pp. 238–259.

    """

    if not isinstance(scale, int) or scale <= 1:
        raise ValueError('\'scale\' must be an integer greater than 1!')
    
    if kernel is None:
        kernel = 'cubic'
    else:
        kernel = kernel.lower()

        if kernel == 'bicubic':
            kernel = 'cubic'

        if kernel == 'bilinear':
            kernel = 'triangle'

    if kernel in ['box', 'triangle']:
        taps = 1
    elif kernel in ['cubic', 'lanczos2']:
        taps = 2
    elif kernel in ['lanczos3']:
        taps = 3
    else:
        raise ValueError('Unknown resize kernel {}!'.format(kernel))

    func = eval(f'{kernel}')

    if scale % 2 == 0: # scale is even
        kernel_width = 2 * scale * taps
        weight_1d = np.empty(kernel_width, dtype=np.float64)
        weight_1d[kernel_width//2:] = func([(2 * i + 1) / (2 * scale) for i in range(kernel_width // 2)])
        weight_1d[:kernel_width//2] = weight_1d[:kernel_width//2-1:-1] # mirror

    else: # scale is odd
        kernel_width = 2 * scale * taps - 1
        weight_1d = np.empty(kernel_width, dtype=np.float64)
        weight_1d[kernel_width//2:] = func([(i / scale) for i in range(kernel_width // 2 + 1)])
        weight_1d[:kernel_width//2] = weight_1d[:kernel_width//2:-1] # mirror

    # kernel normalization
    for i in range(scale):
        weight_1d[i::scale] /= weight_1d[i::scale].sum()

    if downsample:
        weight_1d /= scale
    
    if kernel in ['box']:
        weight_1d = weight_1d[scale//2:-scale//2]

    return weight_1d
