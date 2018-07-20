**Note**: The output of the network is modified to be directly the deblurred result, as opposed to the original model.

```python
# RED30_deblur_disk
args = dict(up_scale=1, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, is_caffe_model=True, normalize_mean=None, normalize_std=None, dynamic_range=1)

# RED30_deblur_gaussian
args = dict(up_scale=1, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, is_caffe_model=True, normalize_mean=None, normalize_std=None, dynamic_range=1)
```
