**Note**: WDSR-B models in this folders are actually WDSR-A style models with more filters per layer.

```python
# EDSR-8-x2
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# WDSR-a-8-x2
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# WDSR-b-8-x2
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# WDSR-b-8-x3
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# WDSR-b-8-x4
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# WDSR-b-16-x2
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# WDSR-b-16-x4
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# WDSR-b-32-x2
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# WDSR-b-32-x2
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)
```