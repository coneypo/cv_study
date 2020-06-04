# 形态学梯度
# 图像膨胀与腐蚀的差别。
# 结果看上去就像前景物体的轮廓。

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(3, 480)


def nothing(x):
    pass


cv2.namedWindow('img')
cv2.createTrackbar('gradient_kernel', 'img', 0, 20, nothing)


while cap.isOpened():

    kernel_value = cv2.getTrackbarPos('gradient_kernel', 'img')

    ret_flag, img_camera = cap.read()

    kernel = np.ones((int(kernel_value), int(kernel_value)), np.uint8)
    erosion = cv2.morphologyEx(img_camera, cv2.MORPH_GRADIENT, kernel)

    cv2.imshow("img", erosion)

    k = cv2.waitKey(1)

    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()