**Note**: The model has been modified to allow RGB input rather than BGR input.

```python
# scale2.0x_model
sr_args = dict(up_scale=2, is_rgb_model=True, pad=(7,7,7,7), crop=None, pre_upscale=True, resample_kernel='Catmull-Rom')
```
