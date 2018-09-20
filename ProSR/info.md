### [NTIRE 2018 challenge on image super-resolution](http://www.vision.ee.ethz.ch/ntire18/#challenge)

[Track 1: classic bicubic](https://competitions.codalab.org/competitions/18015):
uses the bicubic downscaling (Matlab imresize). The downscaling factor is 8.

**Note**: Pre-processing has been included in the model's definition. Residual scaling is also removed if the factor is 1.

```python
# ProSRs_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Catmull-Rom')

# ProSRs_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Catmull-Rom')

# ProSRs_8x
sr_args = dict(up_scale=8, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Catmull-Rom')

# ProSR_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Catmull-Rom')

# ProSR_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Catmull-Rom')

# ProSR_8x
sr_args = dict(up_scale=8, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Catmull-Rom')

# ProSRGAN_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Catmull-Rom')

# ProSRGAN_8x
sr_args = dict(up_scale=8, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, merge_source=True, resample_kernel='Catmull-Rom')



# old models

# ProSR_2x_old
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# ProSR_4x_old
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# ProSR_8x_old
sr_args = dict(up_scale=8, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# ProSRL_2x_old (freeze_psnr_x2_net_G.pth)
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# ProSRL_4x_old (freeze_psnr_x4_net_G.pth)
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# ProSRL_8x_old (freeze_psnr_x8_net_G.pth)
sr_args = dict(up_scale=8, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)
```
