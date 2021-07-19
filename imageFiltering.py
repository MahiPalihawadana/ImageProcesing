# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:27:13 2021

@author: Dilki palihawadana
"""
#unsharped mask

from skimage import io,img_as_float
from skimage.filters import unsharp_mask
from skimage.filters import gaussian

img=img_as_float(io.imread("img3.jpg", as_gray=True))

gaussian_img = gaussian(img,sigma=2,mode='constant',cval=0.0)

img2 = (img - gaussian_img)*2

img3=img + img2

from matplotlib import pyplot as plt
plt.imshow(img3,cmap="gray")

