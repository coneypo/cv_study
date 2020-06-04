# 膨胀

import cv2
import numpy as np

img_rd = cv2.imread("../../photos/pattern_1.png", 0)

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.dilate(img_rd, kernel, iterations = 1)

cv2.imshow("win", erosion)
cv2.imwrite("img_dilate.jpg", erosion)
cv2.waitKey(0)