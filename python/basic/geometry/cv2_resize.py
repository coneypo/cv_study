import cv2
import imutils
img_rd = cv2.imread("../photos/test_1.jpg")

print(type(img_rd))
print(img_rd.size)
print(img_rd.shape)

# imutils.resize will never use height
img_resized = cv2.resize(img_rd, (300, 300))
print(img_resized.shape)

cv2.imshow("win", img_resized)
cv2.waitKey(0)