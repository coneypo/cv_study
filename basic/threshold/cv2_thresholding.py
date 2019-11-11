import cv2

# Threshold
# When > Threshold, give new value (maybe white)
# When < Threshold, give new value (maybe black)

img_rd = cv2.imread("../../photos/test_1.jpg")


# cv2.THRESH_BINARY
# cv2.THRESH_BINARY_INV
# cv2.THRESH_TRUNC      #
# cv2.THRESH_TOZERO     # set 0 when > threshold
# cv2.THRESH_TOZERO_INV # set 0 when < threshold

img_thre = cv2.threshold(img_rd, 225, 255, cv2.THRESH_BINARY_INV)[1]

cv2.imshow("win", img_thre)
cv2.waitKey(0)
