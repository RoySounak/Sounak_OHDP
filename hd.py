'''import sys
import cv2
import numpy as np

#datapath = sys.argv[1] #opencv-3.0.0/samples/data/shape_sample/

a = cv2.imread("/home/rahul/Desktop/False.jpg",0);
b = cv2.imread("/home/rahul/Desktop/sou.jpg",0);

_, ca, _ = cv2.findContours(a, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_KCOS) 
_, cb, _ = cv2.findContours(b, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_KCOS) 
print (np.shape(ca[0]) , np.shape(cb[0]))

hd = cv2.createHausdorffDistanceExtractor()
sd = cv2.createShapeContextDistanceExtractor()

d1 = hd.computeDistance(ca[0],cb[0])
d2 = sd.computeDistance(ca[0],cb[0])

print (d1, " ", d2)

assert d2 != 0'''

from siftdetector import detect_keypoints
import numpy as np
import cv2
import itertools

def match_template(imagename, templatename, threshold, cutoff):
	
    img = cv2.imread(imagename)
    template = cv2.imread(templatename)

    [kpi, di] = detect_keypoints(imagename, threshold)
    [kpt, dt] = detect_keypoints(templatename, threshold)

    flann_params = dict(algorithm=1, trees=4)
    flann = cv2.flann_Index(np.asarray(di, np.float32), flann_params)
    idx, dist = flann.knnSearch(np.asarray(dt, np.float32), 1, params={})
    del flann

    dist = dist[:,0]/2500.0
    dist = dist.reshape(-1,).tolist()
    idx = idx.reshape(-1).tolist()
    indices = range(len(dist))
    indices.sort(key=lambda i: dist[i])
    dist = [dist[i] for i in indices]
    idx = [idx[i] for i in indices]

    kpi_cut = []
    for i, dis in itertools.izip(idx, dist):
    	if dis < cutoff:
    		kpi_cut.append(kpi[i])
    	else:
    		break

    kpt_cut = []
    for i, dis in itertools.izip(indices, dist):
    	if dis < cutoff:
    		kpt_cut.append(kpt[i])
    	else:
    		break

    h1, w1 = img.shape[:2]
    h2, w2 = template.shape[:2]
    nWidth = w1 + w2
    nHeight = max(h1, h2)
    hdif = (h1 - h2) / 2
    newimg = np.zeros((nHeight, nWidth, 3), np.uint8)
    newimg[hdif:hdif+h2, :w2] = template
    newimg[:h1, w2:w1+w2] = img

    for i in range(min(len(kpi), len(kpt))):
    	pt_a = (int(kpt[i,1]), int(kpt[i,0] + hdif))
    	pt_b = (int(kpi[i,1] + w2), int(kpi[i,0]))
    	cv2.line(newimg, pt_a, pt_b, (255, 0, 0))

cv2.imwrite('matches.jpg', newimg)