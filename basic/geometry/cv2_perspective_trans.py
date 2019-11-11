import cv2
import numpy as np

img_rd = cv2.imread("../../photos/test_1.jpg")

print(type(img_rd))
print(img_rd.size)
print(img_rd.shape)
rows, cols, ch = img_rd.shape

# 对于视角变换,我们需要一个 3x3 变换矩阵。在变换前后直线还是直线。
# 要构建这个变换矩阵,你需要在输入图像上找 4 个点,以及他们在输出图像上对应的位置。
# 这四个点中的任意三个都不能共线。这个变换矩阵可以有函数 cv2.getPerspectiveTransform() 构建。
# 然后把这个矩阵传给函数 cv2.warpPerspective

pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img_rd, M, (300, 300))

cv2.imshow("win", dst)
cv2.waitKey(0)
