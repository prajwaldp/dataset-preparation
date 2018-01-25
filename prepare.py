import os
import dataset_preparation
import sys
from argparse import ArgumentParser


parser = ArgumentParser(description='Clean a dataset. Intelligently')
parser.add_argument('src', help='The path to the source dataset')
parser.add_argument('dest', help='The path to the destination dataset', nargs='?', default='')

args = parser.parse_args()
src_path = args.src
dest_path = args.dest

if dest_path == '':
    base_path, ext = os.path.splitext(src_path)
    dest_path = '{}-prepared{}'.format(base_path, ext)


if not os.path.isfile(src_path):
    print('The file does not exist')
    sys.exit()


print(dataset_preparation.prepare(src_path))
