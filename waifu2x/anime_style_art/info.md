```python
# scale2.0x_model
sr_args = dict(up_scale=2, is_rgb_model=False, pad=(7,7,7,7), crop=None, pre_upscale=True, upscale_uv=False, resample_kernel='Catmull-Rom')

# noise1_model
sr_args = dict(up_scale=2, is_rgb_model=False, pad=(7,7,7,7), crop=None, pre_upscale=True, upscale_uv=False, resample_kernel='Catmull-Rom', is_caffe_model=True, normalize_mean=None, normalize_std=None, dynamic_range=1)

# noise2_model
sr_args = dict(up_scale=2, is_rgb_model=False, pad=(7,7,7,7), crop=None, pre_upscale=True, upscale_uv=False, resample_kernel='Catmull-Rom', is_caffe_model=True, normalize_mean=None, normalize_std=None, dynamic_range=1)

# noise3_model
sr_args = dict(up_scale=2, is_rgb_model=False, pad=(7,7,7,7), crop=None, pre_upscale=True, upscale_uv=False, resample_kernel='Catmull-Rom', is_caffe_model=True, normalize_mean=None, normalize_std=None, dynamic_range=1)
```
