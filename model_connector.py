import mxnet as mx
from mxnet import gluon

# Simple script to connect multiple models sequentially

# params
model_prefixes = [r'.\IRCNN\color\model_sigma=00to04', r'.\waifu2x\waifu2x-caffe@lltcggie\upconv_7_anime_style_art_rgb\noise0_scale2.0x_model']
channels = 3 # channels of input data
w, h = 64, 64 # 2D shape of input data


# internel function
def load_network(prefix, epoch=0, input_names=None):
    '''wrapper function for gluon.SymbolBlock.import'''

    symbol_file = '{}-symbol.json'.format(prefix)

    if input_names is None:
        input_names = ['data']

    param_file = '{}-{:04d}.params'.format(prefix, epoch)
    
    print('Load', symbol_file)
    net = gluon.SymbolBlock.imports(symbol_file, input_names, param_file)

    return net

# process
net = gluon.nn.HybridSequential()
with net.name_scope():
    # load and stack networks
    net.add(*(load_network(prefix) for prefix in model_prefixes))

net.hybridize()

test_data = mx.nd.ones((1, channels, h, w))
net.forward(test_data)
net.export('composed')

print('Success!')
