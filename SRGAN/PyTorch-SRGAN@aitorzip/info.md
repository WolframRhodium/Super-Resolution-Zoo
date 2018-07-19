**Note**: Mean subtraction (a.k.a. MeanShift) is excluded from the model definition.

```python
# SRGAN_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=False, is_caffe_model=False, normalize_mean=(0.485, 0.456, 0.406), normalize_std=(0.229, 0.224, 0.225), dynamic_range=1)
```
