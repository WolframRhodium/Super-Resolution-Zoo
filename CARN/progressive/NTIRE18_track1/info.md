### [NTIRE 2018 challenge on image super-resolution](http://www.vision.ee.ethz.ch/ntire18/#challenge)

[Track 1: classic bicubic](https://competitions.codalab.org/competitions/18015):
uses the bicubic downscaling (Matlab imresize). The downscaling factor is 8.

```python
# ProgressiveCARN_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Point', is_caffe_model=False, normalize_mean=None, normalize_std=None, dynamic_range=1)

# ProgressiveCARN_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Point', is_caffe_model=False, normalize_mean=None, normalize_std=None, dynamic_range=1)

# ProgressiveCARN_8x
sr_args = dict(up_scale=8, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Point', is_caffe_model=False, normalize_mean=None, normalize_std=None, dynamic_range=1)
```
