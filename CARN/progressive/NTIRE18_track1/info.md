```python
# NTIRE 2018 challenge on image super-resolution

# Track 1: classic bicubic
# uses the bicubic downscaling (Matlab imresize)

# ProgressiveCARN_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Point', is_caffe_model=False, normalize_mean=None, normalize_std=None)

# ProgressiveCARN_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Point', is_caffe_model=False, normalize_mean=None, normalize_std=None)

# ProgressiveCARN_8x
sr_args = dict(up_scale=8, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Point', is_caffe_model=False, normalize_mean=None, normalize_std=None)
```
