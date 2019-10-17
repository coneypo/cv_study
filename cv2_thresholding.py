import cv2
import imutils
img_rd = cv2.imread("photos/test_1.jpg")

print(type(img_rd))

img_thre = cv2.threshold(img_rd,225,255,cv2.THRESH_BINARY_INV)[1]

cv2.imshow("win", img_thre)
cv2.waitKey(0)