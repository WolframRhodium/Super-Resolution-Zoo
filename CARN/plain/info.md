**Note**: Mean subtraction (a.k.a. MeanShift) is excluded from the model definition.

```python
# CARN_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=1)

# CARN_3x
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=1)

# CARN_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=1)

# CARN-Mobile_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=1)

# CARN-Mobile_3x
sr_args = dict(up_scale=3, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=1)

# CARN-Mobile_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.4488, 0.4371, 0.4040), normalize_std=(1., 1., 1.), dynamic_range=1)
```
