```python
## Blind Realistic Noise Denoising

# CBDNet (denoising model that not considering the JPEG compression)
args = dict(up_scale=1, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

# CBDNet_JPEG (denoising model that considering the JPEG compression)
args = dict(up_scale=1, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)
```
