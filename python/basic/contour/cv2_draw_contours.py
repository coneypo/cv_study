import cv2


img_rd = cv2.imread("../../photos/pattern_3.png")

# 1. gray
img_gray = cv2.cvtColor(img_rd, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(img_gray, 127, 255, 0)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contours = imutils.grab_contours(contours)

print(contours)
img_rd = cv2.drawContours(img_rd, contours, -1, (0, 255, 0), 3)
cv2.imshow("CON", img_rd)
cv2.waitKey(0)