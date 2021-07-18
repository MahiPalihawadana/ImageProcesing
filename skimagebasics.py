# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:17:03 2021

@author: Dilki palihawadana
"""

#skimage basics

from matplotlib import pyplot as plt

from skimage import io,color
from skimage.transform import rescale,resize,downscale_local_mean

img = io.imread("img3.jpg", as_gray=True)

img_rescaled = rescale(img,1.0/4.0,anti_aliasing=False)

img_resized = resize(img,(200,200),anti_aliasing=True)



img_downscaled = downscale_local_mean(img,(4,3))

plt.imshow(img_downscaled, cmap='gray')