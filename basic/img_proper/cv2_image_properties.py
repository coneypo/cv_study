import cv2
import imutils
img_rd = cv2.imread("../../photos/test_1.jpg")

print(type(img_rd))

print(img_rd.shape)
print(img_rd.size)
print(img_rd.dtype)

# qcv2.imshow("win", img_rd)
# cv2.waitKey(0)