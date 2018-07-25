**Note**: Mean subtraction (a.k.a. MeanShift) and residual scaling have been included in the model's definition.

```python
# EDSR_baseline_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# EDSR_baseline_3x
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# EDSR_baseline_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MDSR_baseline_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MDSR_baseline_3x
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MDSR_baseline_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MDSR_baseline_jpeg_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MDSR_baseline_jpeg_3x
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MDSR_baseline_jpeg_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)
```
