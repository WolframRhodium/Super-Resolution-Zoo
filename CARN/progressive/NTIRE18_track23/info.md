```python
# NTIRE 2018 challenge on image super-resolution

# Track 2: realistic mild adverse conditions
# assumes that the degradation operators (emulating the image acquisition process from a digital camera) can be estimated through training pairs of low and high-resolution images. The degradation operators are the same within an image space and for all the images.

# Track 3: realistic difficult adverse conditions 
# assumes that the degradation operators (emulating the image acquisition process from a digital camera) can be estimated through training pairs of low and high-resolution images. The degradation operators are the same within an image space and for all the images.

# ProgressiveCARN_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Point', is_caffe_model=False, normalize_mean=None, normalize_std=None)

# ProgressiveCARN_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Point', is_caffe_model=False, normalize_mean=None, normalize_std=None)
```
