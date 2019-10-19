import cv2

img_rd = cv2.imread("photos/test2.png", 0)

_, thresh = cv2.threshold(img_rd, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)

# 以数字3的轮廓为例
cnt = contours[0]
print(cnt)
print(type(cnt))
print(len(cnt))
print(cnt[0])

M = cv2.moments(cnt)
print(M['m00'])

cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']

print(cx, cy)

cv2.imshow("win", image)
cv2.waitKey(0)
