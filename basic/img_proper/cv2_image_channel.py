import cv2
import imutils
img_rd = cv2.imread("../../photos/test_1.jpg")

print(type(img_rd))

print(img_rd.shape)
print(img_rd.size)
print(img_rd.dtype)


b, g, r = cv2.split(img_rd)
#print(b)
#print(g)
#print(r)
# img = cv2.merge(b, g, r)

cv2.imshow("win", b)
cv2.imshow("win", g)
cv2.imshow("win", r)
cv2.waitKey(0)