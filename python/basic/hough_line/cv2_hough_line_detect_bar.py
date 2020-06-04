import cv2
import numpy as np

cv2.namedWindow('img')

def nothing(x):
    pass

cv2.createTrackbar('canny_l', 'img', 0, 500, nothing)
cv2.createTrackbar('canny_h', 'img', 0, 500, nothing)
cv2.createTrackbar('hough_value', 'img', 0, 500, nothing)


while 1:
    img_rd = cv2.imread("../../photos/checkerboard_2.jpg", 0)

    hough_val = cv2.getTrackbarPos('hough_value', 'img')
    canny_l = cv2.getTrackbarPos('canny_l', 'img')
    canny_h = cv2.getTrackbarPos('canny_h', 'img')

    edges = cv2.Canny(img_rd, canny_l, canny_h, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, hough_val)

    for rho, theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho

        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))

        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(img_rd, (x1, y1), (x2, y2), (0, 0, 255), 2)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

    cv2.imshow("img", edges)

# cv2.HoughLines()
# 返回值就是(ρ, θ)。
# ρ 的单位是像素,θ 的单位是弧度。
# 第一个参数是一个二值化图像,
# 第二和第三个值分别代表 ρ 和 θ 的精确度。
# 第四个参数是阈值,只有累加其中的值高于阈值时才被认为是一条直线,
# 也可以把它看成能检测到的直线的最短长度(以像素点为单位)。
