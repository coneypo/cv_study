# 直方图

import cv2
import numpy as np
from matplotlib import pyplot as plt


img_rd = cv2.imread("../../photos/checkerboard_1.jpg", 0)
# img_rd = cv2.imread("../../photos/pattern_3.png", 0)
hist = cv2.calcHist([img_rd], [0], None, [256], [0, 256])
hist, bins = np.histogram(img_rd.ravel(), 256, [0, 256])

plt.hist(img_rd.ravel(), 256, [0, 256])
plt.show()