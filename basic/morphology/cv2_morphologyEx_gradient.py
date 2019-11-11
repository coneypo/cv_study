# 形态学梯度
# 图像膨胀与腐蚀的差别。
# 结果看上去就像前景物体的轮廓。

import cv2
import numpy as np

img_rd = cv2.imread("../../photos/pattern_1.png", 0)

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.morphologyEx(img_rd, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("win", erosion)
cv2.imwrite("img_morphologyEx_GRADIENT.jpg", erosion)
cv2.waitKey(0)
