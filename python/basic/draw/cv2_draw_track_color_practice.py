import cv2
import numpy as np




drawing = False
ix, iy = -1, -1
global r, g, b, w

img = np.zeros((300, 300, 3), np.uint8)


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    # print(mode)

    # Press left button
    if event == cv2.EVENT_LBUTTONDOWN:#  and flags == cv2.EVENT_FLAG_LBUTTON:
        drawing = True
        ix, iy = x, y

    # Move
    elif event == cv2.EVENT_MOUSEMOVE and drawing==True:
        print("Current:", x, y)
        print("Pos:  ", x, y)
        print('RGB:  ', r, g, b, '\n')
        cv2.circle(img, (x, y), w, (r, g, b), -1)
    else:
        drawing = False


cv2.namedWindow('img')

def nothing(x):
    pass

cv2.createTrackbar('R', 'img', 0, 255, nothing)
cv2.createTrackbar('G', 'img', 0, 255, nothing)
cv2.createTrackbar('B', 'img', 0, 255, nothing)
cv2.createTrackbar('Width', 'img', 0, 10, nothing)

cv2.setMouseCallback('img', draw_circle)

while 1:
    cv2.imshow('img', img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

    r = cv2.getTrackbarPos('R', 'img')
    g = cv2.getTrackbarPos('G', 'img')
    b = cv2.getTrackbarPos('B', 'img')
    w = cv2.getTrackbarPos('Width', 'img')


cv2.destroyAllWindows()