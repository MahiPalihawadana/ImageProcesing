# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 18:49:50 2021

@author: Dilki palihawadana
"""

#basics opencv

import cv2

from matplotlib import pyplot as plt

img = cv2.imread("img3.jpg",1) 
grey_img=cv2.imread("img3.jpg",0)


plt.imshow(img)

resized =  cv2.resize(img, None,fx=2,fy=2,interpolation = cv2.INTER_CUBIC)

cv2.imshow("original",img)
cv2.imshow("resized", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imshow("color pic",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


