# 拉普拉斯算子可以使用二阶导数的形式定义,
# 可假设其离散实现类似于二阶 Sobel 导数

import cv2
import numpy as np

img_rd = cv2.imread("../../photos/checkerboard_2.jpg", 0)

# cv2.CV_64F 输出图像的深度(数据类型),可以使用 -1, 与原图像保持一致 np.uint8
laplacian = cv2.Laplacian(img_rd, cv2.CV_64F)


cv2.imshow("win", laplacian)
cv2.waitKey(0)