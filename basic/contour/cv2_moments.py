# 矩
# cv2.moments() 会将计算得到的矩以一个字典的形式返回

import cv2

img_rd = cv2.imread("../../photos/pattern_3.png", 0)

ret, thresh = cv2.threshold(img_rd, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]

# Moment
M = cv2.moments(cnt)

print('### Moments: ###')
print(M)
print('\n')

# Gravity center
print('### Gravity center: ###')
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(cx)
print(cy)
print('\n')

# Area
print('### Area: ###')
area = cv2.contourArea(cnt)
print(area)
print(M['m00'])
print('\n')

# Length
print('### Length: ###')
length = cv2.arcLength(cnt, True)
print(length)
print('\n')
