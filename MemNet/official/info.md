```python
## Super-Resolution

# MemNet_M6R6_80C64_SR (2x)
sr_args = dict(up_scale=2, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False, resample_kernel='Catmull-Rom')

# MemNet_M6R6_80C64_SR (3x)
sr_args = dict(up_scale=3, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False, resample_kernel='Catmull-Rom')

# MemNet_M6R6_80C64_SR (4x)
sr_args = dict(up_scale=4, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False, resample_kernel='Catmull-Rom')

# MemNet_M10R10_212C64_SR (2x)
sr_args = dict(up_scale=2, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False, resample_kernel='Catmull-Rom')

# MemNet_M10R10_212C64_SR (3x)
sr_args = dict(up_scale=3, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False, resample_kernel='Catmull-Rom')

# MemNet_M10R10_212C64_SR (4x)
sr_args = dict(up_scale=4, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False, resample_kernel='Catmull-Rom')


## Gaussian Denoising

# MemNet_M6R6_80C64_GD (sigma = 30/50/70)
args = dict(up_scale=1, is_rgb_model=False, pad=None, crop=None, upscale_uv=False)


## JPEG Deblocking

# MemNet_M6R6_80C64_JD (quality factor = 10/20)
args = dict(up_scale=1, is_rgb_model=False, pad=None, crop=None, upscale_uv=False)
```
