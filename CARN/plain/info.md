**Note**: Mean subtraction (a.k.a. MeanShift) has been included in the model's definition.

```python
# CARN_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# CARN_3x
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# CARN_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# CARN-Mobile_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# CARN-Mobile_3x
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# CARN-Mobile_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)
```
