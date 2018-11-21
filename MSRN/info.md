**Note**: Pre-processing has been included in the model's definition (The range of input and output has been set to 1).

```python
# MSRN_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MSRN_3x
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MSRN_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# MSRN_2x_old
sr_args = dict(up_scale=2, is_rgb_model=False, pad=None, crop=None, pre_upscale=False, upscale_uv=False)

# MSRN_3x_old
sr_args = dict(up_scale=3, is_rgb_model=False, pad=None, crop=None, pre_upscale=False, upscale_uv=False)
```
