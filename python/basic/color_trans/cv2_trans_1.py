import cv2
import numpy as np
# BGR <> Gray
# BGR <> HSV

# For HSV
# H(色彩/色度)的取值范围是   [0,179]
# S(饱和度)的取值范围       [0,255]
# V(亮度)的取值范围         [0,255]

img_rd = cv2.imread("../../photos/test_1.jpg")
img_rd = cv2.cvtColor(img_rd, cv2.COLOR_BGR2HSV)
print(type(img_rd))

print(img_rd.shape)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# The mask
mask = cv2.inRange(img_rd, lower_blue, upper_blue)

# Add mask with origin image
res = cv2.bitwise_and(img_rd, img_rd, mask=mask)

# cv2.imshow("win", mask)
cv2.imshow("win", res)
cv2.waitKey(0)