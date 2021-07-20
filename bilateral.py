# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 11:11:17 2021

@author: Dilki palihawadana
"""

import cv2
img=cv2.imread('img3.jpg',0)

bilateral_filter=cv2.bilateralFilter(img, 5, 20, 100,borderType=cv2.BORDER_CONSTANT)

cv2.imshow("original",img)
cv2.imshow("bilateral",bilateral_filter)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("bilateral.jpg",bilateral_filter)
