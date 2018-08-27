**Note**: The weights of the pre-trained models with residual branches in the original paper have not been uploaded by the author.

```python
# VDSR_4x
sr_args = dict(up_scale=4, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False, resample_kernel='Catmull-Rom')

# DRRN_4x
sr_args = dict(up_scale=4, is_rgb_model=False, pad=None, crop=None, pre_upscale=True, upscale_uv=False, resample_kernel='Catmull-Rom')

# LapSRN_2x
sr_args = dict(up_scale=2, is_rgb_model=False, pad=None, crop=None, pre_upscale=False, upscale_uv=False)

# LapSRN_4x
sr_args = dict(up_scale=4, is_rgb_model=False, pad=None, crop=None, pre_upscale=False, upscale_uv=False)
```
