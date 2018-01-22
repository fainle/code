import os, argparse
from collections import ChainMap # python3 才支持

defaults = {'color':'red', 'user':'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k:v for k, v in vars(namespace).items() if v}

combined = ChainMap(command_line_args, os.environ, defaults) # 每个字典 逐一查询 返回第一个找到的值
print(combined['color'])
print(combined['user'])