import cv2
import imutils

img_rd = cv2.imread("photos/test_1.jpg")

print(type(img_rd))

img_blur = cv2.GaussianBlur(img_rd, (11, 11), 0)

cv2.imshow("win", img_blur)
cv2.waitKey(0)
