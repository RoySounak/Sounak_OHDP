#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 13:48:09 2018

@author: rahul
"""

from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def mse(imageA, imageB):
      
      err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
      err /= float(imageA.shape[0] * imageA.shape[1])
      return err

def compare_images(imageA, imageB, title):
   
     m = mse(imageA, imageB)
     s = ssim(imageA, imageB)
   
     fig = plt.figure(title)
     plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

     ax = fig.add_subplot(1, 2, 1)
     plt.imshow(imageA, cmap = plt.cm.gray)
     plt.axis("off")

     ax = fig.add_subplot(1, 2, 2)
     plt.imshow(imageB, cmap = plt.cm.gray)
     plt.axis("off")

     plt.show()

true = cv2.imread("//home/rahul/Documents/project/Scan_Guwahati_Handwriting_data25.8.14/WanjoplangWansai-13/True.jpg")
false = cv2.imread("//home/rahul/Documents/project/Scan_Guwahati_Handwriting_data25.8.14/WanjoplangWansai-13/False.jpg")
true = cv2.cvtColor(true, cv2.COLOR_BGR2GRAY)
false = cv2.cvtColor(false, cv2.COLOR_BGR2GRAY)
fig = plt.figure("Images")
images = ("true", true), ("false", false)
for (i, (name, image)) in enumerate(images):
        ax = fig.add_subplot(1, 3, i + 1)
        ax.set_title(name)
        plt.imshow(image, cmap = plt.cm.gray)
        plt.axis("off")
plt.show()
compare_images(true, true, "true vs. true")
compare_images(true, false, "true vs. false")
