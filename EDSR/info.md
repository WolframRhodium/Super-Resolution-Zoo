**Note**: Mean subtraction (a.k.a. MeanShift) and residual scaling are excluded from the model definition.

```python
# EDSR_baseline_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=255)

# EDSR_baseline_3x
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=255)

# EDSR_baseline_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=255)

# MDSR_baseline_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=255)

# MDSR_baseline_3x
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=255)

# MDSR_baseline_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=255)

# MDSR_baseline_jpeg_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=255)

# MDSR_baseline_jpeg_3x
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=255)

# MDSR_baseline_jpeg_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=255)
```
