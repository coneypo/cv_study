# Sobel 算子是高斯平滑与微分操作的结合体
# 所以它的抗噪声能力很好

import cv2
import numpy as np

img_rd = cv2.imread("../../photos/checkerboard_2.jpg", 0)

# 参数 1,0 为只在 x 方向求一阶导数,最大可以求 2 阶导数。
sobelx=cv2.Sobel(img_rd, cv2.CV_64F, 1, 0, ksize=5)

# 参数 0,1 为只在 y 方向求一阶导数,最大可以求 2 阶导数。
sobely=cv2.Sobel(img_rd, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow("win", sobely)
cv2.waitKey(0)