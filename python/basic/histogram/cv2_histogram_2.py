# 直方图

import cv2
from matplotlib import pyplot as plt

img_rd = cv2.imread("../../photos/people_1.jpg")
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histr = cv2.calcHist([img_rd], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

plt.show()