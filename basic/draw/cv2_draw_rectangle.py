import cv2
import imutils
img_rd = cv2.imread("../photos/test_1.jpg")

print(type(img_rd))

print(img_rd.shape)

cv2.rectangle(img_rd, (10,10), (30,30), (0,255,0))

cv2.imshow("win", img_rd)
cv2.waitKey(0)