#!/usr/bin/env python
"""
./HornSchunck.py data/box/box
./HornSchunck.py data/office/office
./HornSchunck.py data/rubic/rubic
./HornSchunck.py data/sphere/sphere
"""
from skimage.color import rgb2grey
from scipy.ndimage.filters import gaussian_filter
import imageio
from matplotlib.pyplot import show
#
from pyoptflow import HornSchunck, getimgfiles
from pyoptflow.plots import compareGraphs

FILTER = 7

def demo(stem):
    flist = getimgfiles(stem)
    ext = flist[0].suffix

    for i in range(len(flist)-1):
        fn1 = f'{stem}.{i}{ext}'
        im1 = imageio.imread(fn1)
        if im1.ndim>2:
            im1 = rgb2grey(im1)
 #       Iold = gaussian_filter(Iold,FILTER)

        fn2 = f'{stem}.{i+1}{ext}'
        im2 = imageio.imread(fn2)
        if im2.ndim>2:
            im2 = rgb2grey(im2)
#        Inew = gaussian_filter(Inew,FILTER)

        U,V = HornSchunck(im1, im2, 1., 100)
        compareGraphs(U,V, im2)

    return U,V


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='Pure Python Horn Schunck Optical Flow')
    p.add_argument('stem',help='path/stem of files to analyze')
    p = p.parse_args()

    U,V = demo(p.stem)

    show()
