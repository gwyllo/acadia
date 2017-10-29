from pdb import set_trace as st
import os
import numpy as np
import cv2
import argparse

parser = argparse.ArgumentParser('create image pairs')
parser.add_argument('--input_dir', dest='input_dir', help='input directory for image A', type=str, default='./datasets/archdaily_sketches/single')
parser.add_argument('--output_dir', dest='output_dir', help='output directory', type=str, default='./datasets/archdaily_sketches/test')
parser.add_argument('--num_imgs', dest='num_imgs', help='number of images',type=int, default=1000000)
args = parser.parse_args()

for arg in vars(args):
    print('[%s] = ' % arg,  getattr(args, arg))

splits = os.listdir(args.input_dir)
pth_in = args.input_dir
pth_out = args.output_dir

if not os.path.isdir(pth_out):
        os.makedirs(pth_out)

for sp in splits:
    img_src_path = os.path.join(pth_in, sp)
    img_tar_path = os.path.join(pth_out, sp)
    print('processing image from '+img_src_path+' to '+img_tar_path)
    im = cv2.imread(img_src_path, cv2.IMREAD_COLOR)
    if im is not None:
        im_AB = np.concatenate([im, im], 1)
        cv2.imwrite(img_tar_path, im_AB)
    else:
        print "Could not load file: "+img_src_path
