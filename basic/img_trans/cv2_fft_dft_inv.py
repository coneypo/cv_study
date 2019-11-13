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

rows, cols = img_rd.shape
crow, ccol = int(rows/2), int(cols/2)

dft = cv2.dft(np.float32(img_rd),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# create a mask with center square=1 and remaining all zeros
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

# apply mask and inverse DFT
fshift =dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])

plt.imshow(img_back)
plt.show()