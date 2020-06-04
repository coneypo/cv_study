# multiview geometry
# find the depth information


import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread("photos/left.jpeg", 0)
img2 = cv2.imread("photos/right.jpeg", 0)

sift = cv2.SIFT()

# find the keypoints and desc with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

good = []
pts1 = []
pts2 = []

for i, (m,n) in enumerate(matches):
    if m.distance < 0.8*n.distance:
        good.append(m)
        pts2.append(kp2[m.trainIdx].pt)
        pts1.append(kp1[m.trainIdx].pt)


