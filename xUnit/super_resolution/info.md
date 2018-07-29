```python
# xSRCNNc_3x
sr_args = dict(up_scale=3, is_rgb_model=False, pad=None, crop=None, pre_upscale=True)

# xSRCNNc_4x
sr_args = dict(up_scale=4, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False)

# xSRCNNf_3x
sr_args = dict(up_scale=3, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False)

# xSRCNNf_4x
sr_args = dict(up_scale=4, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False)

# xSRResNet_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, upscale_uv=False)
```
