```python
## Blind Gaussian Denoising

# GD_Gray_Blind (sigma = [0 55])
args = dict(up_scale=1, is_rgb_model=False, pad=None, crop=None, pre_upscale=False, upscale_uv=False)

# GD_Color_Blind (sigma = [0 55])
args = dict(up_scale=1, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, upscale_uv=False)



### Gaussian Denoising, Single Image Super-Resolution and JPEG Image Deblocking via a Single (DnCNN-3) Model

## Super-Resolution

# DnCNN3 (2x)
sr_args = dict(up_scale=2, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False)

# DnCNN3 (3x)
sr_args = dict(up_scale=3, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False)

# DnCNN3 (4x)
sr_args = dict(up_scale=4, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False)


## Gaussian Denoising

# DnCNN3 (sigma = 15/25/50)
args = dict(up_scale=1, is_rgb_model=False, pad=None, crop=None, pre_upscale=False, upscale_uv=False)


## JPEG Deblocking

# DnCNN3 (quality factor = 10/20/30/40)
args = dict(up_scale=1, is_rgb_model=False, pad=None, crop=None, pre_upscale=False, upscale_uv=False)
```
