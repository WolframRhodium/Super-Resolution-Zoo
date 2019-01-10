**Note**: The models have been modified to allow RGB input rather than BGR input.

```python
# DBPN_2x
sr_args = dict(up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# DBPN_8x
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# DBPN_8x
sr_args = dict(up_scale=8, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)
```

------
### [NTIRE 2018 challenge on image super-resolution](http://www.vision.ee.ethz.ch/ntire18/#challenge)

[Track 1: classic bicubic](https://competitions.codalab.org/competitions/18015):
uses the bicubic downscaling (Matlab imresize). The downscaling factor is 8.

```python
# NTIRE2018_x8
sr_args = dict(up_scale=8, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)
```

------
### [PIRM 2018 Challenge on Perceptual Image Super-resolution](https://www.pirm2018.org/PIRM-SR.html)

```python
# PIRM2018_region1
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# PIRM2018_region2
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# PIRM2018_region3
sr_args = dict(up_scale=4, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)
```
