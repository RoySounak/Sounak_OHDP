#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 22:39:06 2018

@author: rahul
"""

import cv2
import numpy as np
c = cv2.imread('/home/rahul/Desktop/False.jpg')
height, width = c.shape[:2]
cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Frame', 500, 500)
cv2.circle(c, (150,110), 15, (0,0,255), -10)
cv2.circle(c, (2400,110), 15, (0,0,255), -10)
cv2.circle(c, (150,1800), 15, (0,0,255), -10)
cv2.circle(c, (2400,1800), 15, (0,0,255), -10)

pts1 = np.float32([[150,110],[2400,110],[150,1800],[2400,1800]])

pts2 = np.float32([[0,0],[2300,0],[0,1900],[2300,1900]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)


results = cv2.warpPerspective(c,matrix,(2300,1900))

cv2.imshow('New',results)

cv2.imshow('Frame', c)
r = cv2.waitKey(0)
cv2.destroyAllWindows()
