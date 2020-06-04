# 最小外接圆

import cv2

img_rd = cv2.imread("../../photos/pattern_3.png")

img_gray = cv2.cvtColor(img_rd, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)

for i in range(len(contours)):
    cnt = contours[i]
    (x,y), radius = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    radius = int(radius)
    cv2.circle(img_rd, center, radius, (0, 255, 0),2)

cv2.imshow("CON", img_rd)
cv2.waitKey(0)