import cv2
import numpy as np

img_rd = cv2.imread("../../photos/test_1.jpg")

print(type(img_rd))
print(img_rd.size)
print(img_rd.shape)
rows, cols, ch = img_rd.shape

# 原图中所有的平行线在结果图像中同样平行
# 为了创建这个矩阵我们需要从原图像中找到三个点以及他们在输出图像中的位置。
# 然后 cv2.getAffineTransform 会创建一个 2x3 的矩阵
# 最后这个矩阵会被传给 函数 cv2.warpAffine

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img_rd, M, (cols, rows))

cv2.imshow("win", dst)
cv2.waitKey(0)
