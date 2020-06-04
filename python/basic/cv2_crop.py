import cv2
import imutils
img_rd = cv2.imread("../photos/test_1.jpg")

print(type(img_rd))

print(img_rd.shape)
img_new = img_rd[100:, :]
img_new2 = img_rd[:, 100:]
print(img_new.shape)
print(img_new2.shape)

cv2.imshow("win", img_new)
cv2.waitKey(0)