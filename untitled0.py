
import cv2 
import numpy as np
 
img = cv2.imread('/home/rahul/Documents/project/Scan_Guwahati_Handwriting_data25.8.14/WanjoplangWansai-13/True.jpg',0)
#blur = cv2.GaussianBlur(img,(5,5),0)
 
# find normalized_histogram, and its cumulative distribution functio
hist = cv2.calcHist([img],[0],None,[256],[0,256])
hist_norm = hist.ravel()/hist.max()
Q = hist_norm.cumsum()
bins = np.arange(256)
fn_min = np.inf
thresh = -1
xrange=range
for i in xrange(1,256):
 p1,p2 = np.hsplit(hist_norm,[i]) # probabilities
 q1,q2 = Q[i],Q[255]-Q[i] # cum sum of classes
 if q1 == 0:
    q1 = 0.00000001
 if q2 == 0:
    q2 = 0.00000001
 b1,b2 = np.hsplit(bins,[i]) # weights
 # finding means and variances
 m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
 v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
 # calculates the minimization function
 fn = v1*q1 + v2*q2
 if fn < fn_min:
    fn_min = fn
    thresh = i
# find otsu's threshold value with OpenCV function
otsu = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print (thresh)







'''
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('/home/rahul/Desktop/True.jpg',0)
 
ret, imgf = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
 
plt.subplot(3,1,1), plt.imshow(img,cmap = 'gray')
plt.title('Original Noisy Image'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,2), plt.hist(img.ravel(), 256)
plt.axvline(x=ret, color='r', linestyle='dashed', linewidth=2)
plt.title('Histogram'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,3), plt.imshow(imgf,cmap = 'gray')
plt.title('Otsu thresholding'), plt.xticks([]), plt.yticks([])
plt.show()

'''
