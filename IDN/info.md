```python
# IDN_2x
sr_args = dict(up_scale=2, is_rgb_model=False, pad=(1, 1, 1, 1), crop=(1, 2, 1, 2), pre_upscale=False, upscale_uv=False, merge_source=True, resample_kernel='Catmull-Rom')

# IDN_3x
sr_args = dict(up_scale=3, is_rgb_model=False, pad=(1, 1, 1, 1), crop=(1, 3, 1, 3), pre_upscale=False, upscale_uv=False, merge_source=True, resample_kernel='Catmull-Rom')

# IDN_4x
sr_args = dict(up_scale=4, is_rgb_model=False, pad=(1, 1, 1, 1), crop=(1, 4, 1, 4), pre_upscale=False, upscale_uv=False, merge_source=True, resample_kernel='Catmull-Rom')

# IDN_4x_mscoco
sr_args = dict(up_scale=4, is_rgb_model=False, pad=(1, 1, 1, 1), crop=(1, 4, 1, 4), pre_upscale=False, upscale_uv=False, merge_source=True, resample_kernel='Catmull-Rom')
'''
