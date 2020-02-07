#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 17:45:25 2018

@author: rahul
"""

import cv2
import numpy as np

image1 = cv2.imread("/home/rahul/Desktop/True.jpg")
image2 = cv2.imread("/home/rahul/Desktop/False.jpg")

difference = cv2.subtract(image1, image2)

result = not np.any(difference) #if difference is all zeros it will return False

if result is True:
    print ("The images are the same")
else:
    cv2.imwrite("result.jpg", difference)
    print ("the images are different")