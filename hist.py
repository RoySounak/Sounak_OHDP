#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 13:46:36 2018

@author: rahul
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/rahul/Desktop/True.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
plt.plot(histr,color = col)
plt.xlim([0,256])
plt.show()
