# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:17:03 2021

@author: Dilki palihawadana
"""

#skimage basics

from matplotlib import pyplot as plt

from skimage import io,color
from skimage.transform import rescale,resize,downscale_local_mean
from skimage.filters import gaussian,sobel

img = io.imread("img3.jpg", as_gray=True)

img_rescaled = rescale(img,1.0/4.0,anti_aliasing=False)

img_resized = resize(img,(200,200),anti_aliasing=True)



img_downscaled = downscale_local_mean(img,(4,3))

plt.imshow(img_downscaled, cmap='gray')


#filtering

img2 = io.imread("img3.jpg")
plt.imshow(img2)
gaussian_using_sk = gaussian(img2, sigma=2,mode='constant' ,cval=0.0)
plt.imshow(gaussian_using_sk)

img_gray = io.imread("img3.jpg", as_gray=True)
sobel_img = sobel(img_gray)
plt.imshow(sobel_img, cmap='gray')
