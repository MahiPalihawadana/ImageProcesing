# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 17:04:04 2021

@author: Dilki palihawadana
"""

import cv2
from skimage.filters import median
from skimage import io

img=cv2.imread('img3.jpg',0)

median_cv2 = cv2.medianBlur(img, 3)

from skimage.morphology import disk
median_si = median(img,disk(3), mode ='constant', cval=0.0)

cv2.imshow("original",img)
cv2.imshow("median cv2", median_cv2)
cv2.imshow("median skimage",median_si)

cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite('mediancv2', median_cv2)
io.imsave("median.jpg",median_si)

