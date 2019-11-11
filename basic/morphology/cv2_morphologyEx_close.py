# 先膨胀
# 再进行腐蚀
# 就叫做闭运算

# 用来填充前景物体中的小洞,或者前景物体上的小黑点

import cv2
import numpy as np

img_rd = cv2.imread("../../photos/pattern_1.png", 0)

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.morphologyEx(img_rd, cv2.MORPH_CLOSE, kernel)

cv2.imshow("win", erosion)
cv2.imwrite("img_morphologyEx_close.jpg", erosion)
cv2.waitKey(0)
