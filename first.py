# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 19:38:42 2021

@author: Dilki palihawadana
"""

""" Reading iamges"""

from skimage import io,img_as_float,img_as_ubyte

img = io.imread("img1.jpg")
print(img.shape) #y,x,c

img2 = img_as_float(img)

img_8bit = img_as_ubyte(img2)


import cv2
img_cv2=cv2.imread("img1.jpg")
#BGR instead of RGB

grey_img=cv2.imread("img1.jpg",0)
color_img=cv2.imread("img1.jpg",1)

#convert BGR to RGB
img_opencv=cv2.cvtColor(color_img,cv2.COLOR_BGR2RGB)

"""Saving Images"""

from skimage import filters
gaussian_img=filters.gaussian(img,sigma=3)

io.imsave("s1.jpg",gaussian_img)

gaussian_img_8bit = img_as_ubyte(gaussian_img)
io.imsave("s2.jpg",gaussian_img_8bit)

gaussian_img_8bit_RGB = cv2.cvtColor(gaussian_img_8bit,cv2.COLOR_BGR2RGB)
cv2.imwrite("s4.jpg",gaussian_img_8bit_RGB)


from matplotlib import pyplot as plt
plt.imsave("s1_pyplot.jpg",gaussian_img)

"""Viewing 2D images"""
#method 1
io.imshow(img)

#mwthod2
import matplotlib.pyplot as plt
plt.imshow(img)

img_gray=io.imread("img1.jpg",as_gray=True)
#plt.imshow(img_gray,cmap="hot")
#plt.imshow(img_gray,cmap="jet")

#multiple plots using pyplot
fig = plt.figure(figsize=(10,10))

ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img_gray,cmap='hot')
ax1.title.set_text('1st')

ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img_gray,cmap='jet')
ax2.title.set_text('2nd')

ax3 = fig.add_subplot(2,2,3)
ax3.imshow(img_gray,cmap='gray')
ax3.title.set_text('3rd')

ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img_gray,cmap='nipy_spectral')
ax4.title.set_text('4th')

plt.show()





