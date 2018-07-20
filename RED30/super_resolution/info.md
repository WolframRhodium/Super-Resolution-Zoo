**Note**: The output of the network is modified to be directly the super-resolved result, as opposed to the original model.

```python
# RED30_2x
sr_args = dict(up_scale=2, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False, resample_kernel='Catmull-Rom', is_caffe_model=True, normalize_mean=None, normalize_std=None, dynamic_range=1)

# RED30_3x
sr_args = dict(up_scale=3, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False, resample_kernel='Catmull-Rom', is_caffe_model=True, normalize_mean=None, normalize_std=None, dynamic_range=1)

# RED30_4x
sr_args = dict(up_scale=4, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False, resample_kernel='Catmull-Rom', is_caffe_model=True, normalize_mean=None, normalize_std=None, dynamic_range=1)
```
