# 先腐蚀
# 再进行膨胀
# 就叫做开运算

# 它被用来去除噪声

import cv2
import numpy as np

img_rd = cv2.imread("../../photos/pattern_1.png", 0)

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.morphologyEx(img_rd, cv2.MORPH_OPEN, kernel)

cv2.imshow("win", erosion)
cv2.imwrite("img_morphologyEx_open.jpg", erosion)
cv2.waitKey(0)
