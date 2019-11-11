import cv2
import imutils
img_rd_1 = cv2.imread("../../photos/test_1.jpg")
img_rd_2 = cv2.imread("../../photos/test.jpg")

print(img_rd_1.shape)
print(img_rd_2.shape)

img_rd_2 = cv2.resize(img_rd_2, (660, 330))

print(img_rd_1.shape)
print(img_rd_2.shape)

def nothing(x):
    pass


cv2.namedWindow('img')

cv2.createTrackbar('mix', 'img', 0, 100, nothing)


while 1:
    # cv2.imshow('dst', img_rd_1)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    mix = cv2.getTrackbarPos('mix', 'img')
    mix = mix/100
    # print(mix)
    img = cv2.addWeighted(img_rd_1, float(mix), img_rd_2, (1-float(mix)), 0)
    cv2.imshow('img', img)

cv2.destroyAllWindow()




