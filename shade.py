# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 12:04:34 2021

@author: Dilki palihawadana
"""

import cv2
import numpy as np

img = cv2.imread("img3.jpg", 1)

lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab_img)


clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(8,8))
clahe_img = clahe.apply(l)
CLAHE_img = cv2.merge((clahe_img,a,b))

corrected_image = cv2.cvtColor(CLAHE_img, cv2.COLOR_LAB2BGR)

cv2.imshow("Original image", img)
cv2.imshow("Corrected image", corrected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("shade.jpg",corrected_image )