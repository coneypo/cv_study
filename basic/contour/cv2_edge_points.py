# 极点

import cv2

img_rd = cv2.imread("../../photos/pattern_3.png")

img_gray = cv2.cvtColor(img_rd, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)

for i in range(len(contours)):
    cnt = contours[i]
    leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
    rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
    topmost = tuple(cnt[cnt[:, :, 1].argmax()][0])
    bottommost = tuple(cnt[cnt[:, :, 1].argmin()][0])
    cv2.circle(img_rd, leftmost, 2, (0, 255, 0), 2)
    cv2.circle(img_rd, rightmost, 2, (0, 255, 0), 2)
    cv2.circle(img_rd, topmost, 2, (0, 255, 0), 2)
    cv2.circle(img_rd, bottommost, 2, (0, 255, 0), 2)

cv2.imshow("CON", img_rd)
cv2.waitKey(0)
