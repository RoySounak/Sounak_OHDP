import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import os

dataset_path = '/home/rahul/Documents/project/Scan_Guwahati_Handwriting_data25.8.14/AnmolKerketta'
img_building = cv2.imread(os.path.join(dataset_path, 'False.jpg'))
img_building = cv2.cvtColor(img_building, cv2.COLOR_BGR2RGB)  # Convert from cv's BRG default color order to RGB

orb = cv2.ORB_create()  # OpenCV 3 backward incompatibility: Do not create a detector with `cv2.ORB()`.
key_points, description = orb.detectAndCompute(img_building, None)
img_building_keypoints = cv2.drawKeypoints(img_building, 
                                           key_points, 
                                           img_building, 
                                           flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) # Draw circles.
plt.figure(figsize=(10, 10))
plt.title('ORB Interest Points')
plt.imshow(img_building_keypoints)
plt.show()