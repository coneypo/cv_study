import cv2
import imutils

cap = cv2.VideoCapture(0)

# 设置视频参数: propId - 设置的视频参数, value - 设置的参数值
cap.set(3, 480)

img_rd = cv2.imread("../photos/test2.png")

# 1. gray
img_gray = cv2.cvtColor(img_rd, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

print(contours)
cv2.drawContours(img_gray, contours, -1, (0, 0, 255), 3)
cv2.imshow("CON", img_gray)
cv2.waitKey(0)