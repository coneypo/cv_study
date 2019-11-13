import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rd = cv2.imread("../../photos/people_1.jpg", 0)

dft = cv2.dft(np.float32(img_rd), flags= cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))

plt.imshow(magnitude_spectrum)
plt.show()