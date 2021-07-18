# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 16:10:45 2021

@author: Dilki palihawadana
"""
import matplotlib
import matplotlib.pyplot as plt
from skimage import io,img_as_ubyte
from skimage.color import rgb2gray
from skimage.data import page
from skimage.filters import (threshold_otsu, threshold_niblack,
                             threshold_sauvola)


matplotlib.rcParams['font.size'] = 9


#image = page()
img = io.imread("img3.jpg")
image = rgb2gray(img)
binary_global = image > threshold_otsu(image)

window_size = 25
thresh_niblack = threshold_niblack(image, window_size=window_size, k=0.8)
thresh_sauvola = threshold_sauvola(image, window_size=window_size)

binary_niblack = image > thresh_niblack
binary_sauvola = image > thresh_sauvola

plt.figure(figsize=(8, 7))
plt.subplot(2, 2, 1)
plt.imshow(image, cmap=plt.cm.gray)
plt.title('Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Global Threshold')
plt.imshow(binary_global, cmap=plt.cm.gray)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(binary_niblack, cmap=plt.cm.gray)
plt.title('Niblack Threshold')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(binary_sauvola, cmap=plt.cm.gray)
plt.title('Sauvola Threshold')
plt.axis('off')

plt.show()
io.imsave("gt.jpg",img_as_ubyte(binary_global))
io.imsave("nt.jpg",img_as_ubyte(binary_niblack))
io.imsave("st.jpg",img_as_ubyte(binary_sauvola))
