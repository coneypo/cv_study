# 在前面的部分我们实现了一个 HPF(高通滤波),
# 现在我们来做 LPF(低通滤波)将高频部分去除。
# 其实就是对图像进行模糊操作。
# 首先我们需要构建一个掩模,
# 与低频区域对应的地方设置为 1,
# 与高频区域 对应的地方设置为 0。

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rd = cv2.imread("../../photos/people_1.jpg", 0)
img_rd_cp = img_rd.copy()

template = cv2.imread('../../photos/people_1_person.jpg', 0)
w, h = template.shape[::-1]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img_rd_cp.copy()

    method = eval(meth)

    # Apply template matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    plt.subplot(121), plt.imshow(res)
    plt.subplot(122), plt.imshow(img)
    plt.suptitle(meth)

    plt.show()
