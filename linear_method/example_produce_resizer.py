import mxnet as mx
from resize_weight import resize_weight

# a script that produces a (center-aligned) linear interpolation resizer in the form of CNN in MXNet

# params
scale = 2
kernel = 'bicubic'
channels = 1
downsample = False

if not downsample:
    name = '{}_{}x'.format(kernel, scale)

    weight_1d = resize_weight(scale=scale, kernel=kernel)
    kwidth = len(weight_1d)
    taps = (kwidth + 1) // (2 * scale)

    # tries to fix the boundary condition via external padding, but the value here might not be accurate
    pad = scale // 2 + (2 * taps - 1) * scale

    # Defining the network
    # Since the interpolations are separable, we implemented them via spatial separable convolutions
    # It's straightforward to modify the code to obtain a single convolution implementation
    data = mx.symbol.Variable('data') # assumes NCHW data format
    upsample_h = mx.symbol.pad(data, mode='edge', pad_width=(0, 0, 0, 0, taps, taps, 0, 0))
    upsample_h = mx.symbol.Deconvolution(upsample_h, kernel=(kwidth, 1), stride=(scale, 1), pad=(pad, 0), 
        num_filter=channels, num_group=channels, no_bias=True, name='{}_h'.format(name))
    upsample_w = mx.symbol.pad(upsample_h, mode='edge', pad_width=(0, 0, 0, 0, 0, 0, taps, taps))
    upsample_w = mx.symbol.Deconvolution(upsample_w, kernel=(1, kwidth), stride=(1, scale), pad=(0, pad), 
        num_filter=channels, num_group=channels, no_bias=True, name='{}_w'.format(name))

    # Loading weights
    net = mx.gluon.SymbolBlock(outputs=upsample_w, inputs=data)
    net_params = net.collect_params()
    net_params['{}_h_weight'.format(name)]._load_init(mx.nd.array(weight_1d.reshape((1, 1, kwidth, 1))), ctx=mx.cpu())
    net_params['{}_w_weight'.format(name)]._load_init(mx.nd.array(weight_1d.reshape((1, 1, 1, kwidth))), ctx=mx.cpu())
    net.hybridize()
    test_data = mx.nd.ones((1, channels, 96, 96))
    net.forward(test_data)

    # Output
    net.export(name)

else:
    name = '{}_{}x_downsample'.format(kernel, scale)

    weight_1d = resize_weight(scale=scale, kernel=kernel, downsample=True)
    kwidth = len(weight_1d)

    data = mx.symbol.Variable('data')
    upsample_h = mx.symbol.pad(data, mode='edge', pad_width=(0, 0, 0, 0, (kwidth - scale) // 2, (kwidth - scale) // 2, 0, 0))
    upsample_h = mx.symbol.Convolution(upsample_h, kernel=(kwidth, 1), stride=(scale, 1), pad=(0, 0), 
        num_filter=channels, num_group=channels, no_bias=True, name='{}_h'.format(name))
    upsample_w = mx.symbol.pad(upsample_h, mode='edge', pad_width=(0, 0, 0, 0, 0, 0, (kwidth - scale) // 2, (kwidth - scale) // 2))
    upsample_w = mx.symbol.Convolution(upsample_w, kernel=(1, kwidth), stride=(1, scale), pad=(0, 0), 
        num_filter=channels, num_group=channels, no_bias=True, name='{}_w'.format(name))

    net = mx.gluon.SymbolBlock(outputs=upsample_w, inputs=data)
    net_params = net.collect_params()
    net_params['{}_h_weight'.format(name)]._load_init(mx.nd.array(weight_1d.reshape((1, 1, kwidth, 1))), ctx=mx.cpu())
    net_params['{}_w_weight'.format(name)]._load_init(mx.nd.array(weight_1d.reshape((1, 1, 1, kwidth))), ctx=mx.cpu())

    net.hybridize()

    test_data = mx.nd.ones((1, channels, 96, 96))
    net.forward(test_data)

    net.export(name)