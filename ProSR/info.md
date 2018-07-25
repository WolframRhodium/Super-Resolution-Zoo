### [NTIRE 2018 challenge on image super-resolution](http://www.vision.ee.ethz.ch/ntire18/#challenge)

[Track 1: classic bicubic](https://competitions.codalab.org/competitions/18015):
uses the bicubic downscaling (Matlab imresize). The downscaling factor is 8.

**Note**: Pre-processing has been included in the model's definition.

```python
# ProSR_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# ProSR_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# ProSR_8x
sr_args = dict(up_scale=8, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)
```
