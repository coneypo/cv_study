import cv2
import imutils
img_rd = cv2.imread("../photos/test_1.jpg")

print(type(img_rd))
print(img_rd.size)
print(img_rd.shape)

img_resized = imutils.resize(img_rd, width=300)
print(img_resized.shape)

cv2.imshow("win", img_resized)
cv2.waitKey(0)