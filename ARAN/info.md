**Note**: MeanShift has been included in the model's definition. Models are converted from `model_best.pt`.

```python
# aran_c0_s0_x2
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# aran_c0_s1_x2 (Spatial Attention)
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# aran_c0_s1_x3 (Spatial Attention)
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# aran_c0_s1_x4 (Spatial Attention)
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# aran_c1_s0_x2 (Channel Attention)
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# aran_c1_s1_x2 (Channel Attention + Spatial Attention)
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)
```
