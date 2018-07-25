### [NTIRE 2018 challenge on image super-resolution](http://www.vision.ee.ethz.ch/ntire18/#challenge)

[Track 2: realistic mild adverse conditions](https://competitions.codalab.org/competitions/18024):
assumes that the degradation operators (emulating the image acquisition process from a digital camera) can be estimated through training pairs of low and high-resolution images. The degradation operators are the same within an image space and for all the images. The downscaling factor is 4

[Track 3: realistic difficult adverse conditions](https://competitions.codalab.org/competitions/18025):
assumes that the degradation operators (emulating the image acquisition process from a digital camera) can be estimated through training pairs of low and high-resolution images. The degradation operators are the same within an image space and for all the images. The downscaling factor is 4

```python

# ProgressiveCARN_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# ProgressiveCARN_4x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)
```
