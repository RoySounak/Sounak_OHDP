#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 23:00:36 2018

@author: rahul
"""

import cv2
import numpy as np

c = cv2.imread('/home/rahul/Desktop/True.jpg')

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(c,kernel,iterations = 1)
dialation = cv2.dilate(c,kernel,iterations = 1)
cv2.imshow('erosion', erosion)
cv2.imshow('dialation',dialation)

r = cv2.waitKey(0)
cv2.destroyAllWindows()
