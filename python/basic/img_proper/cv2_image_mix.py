import cv2
import imutils
img_rd_1 = cv2.imread("../../photos/test_1.jpg")
img_rd_2 = cv2.imread("../../photos/test.jpg")

print(img_rd_1.shape)
print(img_rd_2.shape)

img_rd_2 = cv2.resize(img_rd_2, (660, 330))

print(img_rd_1.shape)
print(img_rd_2.shape)

# img_1 and img_2 with same shape
dst = cv2.addWeighted(img_rd_1, 0.7, img_rd_2, 0.3, 0)

cv2.imshow('dst', dst)
# cv2.imshow('dst', img_rd_1)
cv2.waitKey(0)
cv2.destroyAllWindow()