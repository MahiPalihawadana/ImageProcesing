# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:58:27 2021

@author: Dilki palihawadana
"""

import cv2
from skimage import io,img_as_float
from skimage.filters import gaussian

img = img_as_float(io.imread('img2.jpg',as_gray=True))

gaussain_cv2 = cv2.GaussianBlur(img, (3,3), 0,borderType=cv2.BORDER_CONSTANT)

gaussian_skimage = gaussian(img,sigma=1, mode='constant',cval=0.0)

cv2.imshow("original",img)
cv2.imshow("cv2 gaussian", gaussain_cv2)
cv2.imshow("skimage gaussian", gaussian_skimage)

cv2.waitKey(0)
cv2.destroyAllWindows()



