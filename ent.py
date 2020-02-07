#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:33:34 2018

@author: rahul
"""
'''
import math
from PIL import Image
imageFile = '/home/rahul/Desktop/False.jpg'
print (imageFile)
im = Image.open(imageFile)
rgbHistogram = im.histogram()
print(rgbHistogram)
print ('Entropy for Red, Green, Blue:')
for rgb in range(3):
     totalPixels = sum(rgbHistogram[rgb * 256 : (rgb + 1) * 256])
     ent = 0.0
     for col in range(rgb * 256, (rgb + 1) * 256):
         freq = float(rgbHistogram[col]) / totalPixels
         if freq > 0:
             ent = ent + freq * math.log(freq, 2)
     ent = -ent
print (ent)
 '''

import numpy as np
from skimage import io, color, img_as_ubyte
from skimage.feature import greycomatrix, greycoprops
from sklearn.metrics.cluster import entropy

rgbImg = io.imread('/home/rahul/Documents/project/Scan_Guwahati_Handwriting_data25.8.14/WanjoplangWansai-13/True.jpg')
grayImg = img_as_ubyte(color.rgb2gray(rgbImg))

distances = [1, 2, 3]
angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
properties = ['energy', 'homogeneity']

glcm = greycomatrix(grayImg, 
                    distances=distances, 
                    angles=angles,
                    symmetric=True,
                    normed=True)

feats = np.hstack([greycoprops(glcm, prop).ravel() for prop in properties])
print(entropy(grayImg))
'''


import numpy
import math
import cv2
 
def image_entropy(img):
    """calculate the entropy of an image"""
    histogram = img.histogram()
    histogram_length = sum(histogram)
 
    samples_probability = [float(h) / histogram_length for h in histogram]
 
    return -sum([p * math.log(p, 2) for p in samples_probability if p != 0])
 
img = cv2.imread('/home/rahul/Desktop/False.jpg')
print (image_entropy(img))'''