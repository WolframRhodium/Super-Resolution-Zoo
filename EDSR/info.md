**Note**: Pre-processing has been included in the model's definition (The range of input and output has been set to 1). Residual scaling is also removed if the factor is 1.

```python
# EDSR_baseline_x2
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# EDSR_baseline_x3
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# EDSR_baseline_x4
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# EDSR_x2
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# EDSR_x3
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# EDSR_x4
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MDSR_baseline_x2
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MDSR_baseline_x3
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MDSR_baseline_x4
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MDSR_baseline_jpeg_x2
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MDSR_baseline_jpeg_x3
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MDSR_baseline_jpeg_x4
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MDSR_x2
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MDSR_x3
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MDSR_x4
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)
```
