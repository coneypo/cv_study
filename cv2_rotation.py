import cv2
import imutils
img_rd = cv2.imread("photos/test_1.jpg")

print(type(img_rd))

img_rotated = imutils.rotate(img_rd, 40)

cv2.imshow("win", img_rotated)
cv2.waitKey(0)