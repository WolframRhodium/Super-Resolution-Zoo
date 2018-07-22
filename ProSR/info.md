### [NTIRE 2018 challenge on image super-resolution](http://www.vision.ee.ethz.ch/ntire18/#challenge)

[Track 1: classic bicubic](https://competitions.codalab.org/competitions/18015):
uses the bicubic downscaling (Matlab imresize). The downscaling factor is 8.

**Note**:
* The operation of adding the bilinear upscaled image to the network's output is included in the model's definition.
* The input to the network should be first substracted by (0.4488, 0.4371, 0.4040) for each channel.

```python
# ProSR_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, is_caffe_model=False, normalize_mean=None, normalize_std=None, dynamic_range=255)

# ProSR_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, is_caffe_model=False, normalize_mean=None, normalize_std=None, dynamic_range=255)

# ProSR_8x
sr_args = dict(up_scale=8, is_rgb_model=True, pad=None, crop=None, pre_upscale=False, is_caffe_model=False, normalize_mean=None, normalize_std=None, dynamic_range=255)
```
