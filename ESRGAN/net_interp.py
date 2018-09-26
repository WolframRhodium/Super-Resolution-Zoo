# modified from https://github.com/xinntao/ESRGAN/blob/50fbd2de1d80a014e1c0e1c165913a128f5a8384/net_interp.py

import sys
import mxnet as mx
from shutil import copyfile

alpha = float(sys.argv[1])


params_PSNR_path = 'RRDB_4x-0000.params'
params_ESRGAN_path = 'ESRGAN_4x-0000.params'
params_interp_path = 'interp_{:02d}_4x-0000.params'.format(int(alpha*10))

symbol_path = 'ESRGAN_4x-symbol.json'
symbol_interp_path = 'interp_{:02d}_4x-symbol.json'.format(int(alpha*10))


# duplicate symbol file
copyfile(symbol_path, symbol_interp_path)

# network interpolation
params_PSNR = mx.nd.load(params_PSNR_path)
params_ESRGAN = mx.nd.load(params_ESRGAN_path)
params_interp = {}

print('Interpolating with alpha = {}'.format(alpha))

for key, param_PSNR in params_PSNR.items():
    param_ESRGAN = params_ESRGAN[key]
    params_interp[key] = (1 - alpha) * param_PSNR + alpha * param_ESRGAN

mx.nd.save(params_interp_path, params_interp)


print('Output symbol: {}'.format(symbol_interp_path))
print('Output params: {}'.format(params_interp_path))