**Note**: Mean subtraction (a.k.a. MeanShift) and other pre-processing have been included in the model's definition.

```python
# Bicubic (BI) degradation model

# RCAN_BIX2
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# RCAN_BIX3
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# RCAN_BIX4
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# RCAN_BIX8
sr_args = dict(up_scale=8, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)


# Blur-downscale (BD) degradation model

# RCAN_BDX3
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)
```
