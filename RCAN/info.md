**Note**: Mean subtraction (a.k.a. MeanShift) and residual scaling are excluded from the model's definition.
The output is **inconsistent** with the original model currently. I will try to fix it.

```python
# Bicubic (BI) degradation model

# RCAN_BIX2
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=255)

# RCAN_BIX3
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=255)

# RCAN_BIX4
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=255)

# RCAN_BIX8
sr_args = dict(up_scale=8, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=255)


# Blur-downscale (BD) degradation model

# RCAN_BDX3
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=255)
```
