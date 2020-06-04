import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rd = cv2.imread("../../photos/people_1.jpg", 0)

f = np.fft.fft2(img_rd)
fshift = np.fft.fftshift(f)
magnitude_sepctrum = 20*np.log(np.abs(fshift))
print(magnitude_sepctrum)
#plt.subplot(121)
#plt.show(img_rd)
#plt.title("Input"), plt.xticks([]), plt.yticks([])

# plt.subplot()
plt.imshow(magnitude_sepctrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.show()