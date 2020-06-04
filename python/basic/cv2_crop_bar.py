import cv2
# img_rd = cv2.imread("../photos/people_1.jpg")
img_rd = cv2.imread("../photos/coins.jpeg")

print(type(img_rd))

print(img_rd.shape)
height, width = img_rd.shape[0], img_rd.shape[1]


cv2.namedWindow('img')

def nothing(x):
    pass

cv2.createTrackbar('hl', 'img', 0, height, nothing)
cv2.createTrackbar('hh', 'img', 100, height, nothing)

cv2.createTrackbar('wl', 'img', 0, width, nothing)
cv2.createTrackbar('wh', 'img', 100, width, nothing)


while 1:
    h_l = cv2.getTrackbarPos('hl', 'img')
    h_h = cv2.getTrackbarPos('hh', 'img')
    w_l = cv2.getTrackbarPos('wl', 'img')
    w_h = cv2.getTrackbarPos('wh', 'img')

    img_new = img_rd[h_l:h_h, w_l:w_h]

    cv2.imshow('img', img_new)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

    if k == ord('s'):
        cv2.imwrite("img_new.jpg", img_new)
