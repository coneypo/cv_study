import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rd = cv2.imread("../../photos/coins.jpg")
img_rd_gray = cv2.imread("../../photos/coins.jpg", 0)
img_template = cv2.imread("../../photos/coin_single.jpg", 0)

w, h = img_template.shape[::-1]

res = cv2.matchTemplate(img_rd_gray, img_template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8

loc = np.where(res>=threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rd, pt, (pt[0]+w, pt[1]+h), (0,0,255), 2)

cv2.imshow('img', img_rd)
cv2.waitKey(0)