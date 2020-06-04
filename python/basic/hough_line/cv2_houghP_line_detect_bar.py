import cv2
import numpy as np

cv2.namedWindow('img')

def nothing(x):
    pass

cv2.createTrackbar('canny_l', 'img', 0, 500, nothing)
cv2.createTrackbar('canny_h', 'img', 0, 500, nothing)
cv2.createTrackbar('hough_value', 'img', 0, 500, nothing)
cv2.createTrackbar('min_line_length', 'img', 0, 500, nothing)

cap = cv2.VideoCapture(0)

cap.set(3, 480)

while 1:

    ret_flag, img_rd = cap.read()

    hough_val = cv2.getTrackbarPos('hough_value', 'img')
    min_line_length_val = cv2.getTrackbarPos('min_line_length', 'img')
    canny_l = cv2.getTrackbarPos('canny_l', 'img')
    canny_h = cv2.getTrackbarPos('canny_h', 'img')

    # edges = cv2.Canny(img_rd, canny_l, canny_h, apertureSize=3)
    edges = cv2.Canny(img_rd, 50, 150, apertureSize=3)

    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, min_line_length_val, minLineLength, maxLineGap)

    for x1, y1, x2, y2 in lines[0]:
        cv2.line(img_rd, (x1, y1), (x2, y2), (0, 0, 255), 2)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

    cv2.imshow("img", img_rd)
    # cv2.imshow("img", edges)