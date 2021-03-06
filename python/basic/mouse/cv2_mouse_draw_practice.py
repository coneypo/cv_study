import cv2
import numpy as np

drawing = False
mode = True
ix, iy = -1, -1


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        print("Begin:  ", ix, iy)
    elif event == cv2.EVENT_LBUTTONUP:
        print("Release:", x, y)
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 3)

        drawing = False


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('img')
cv2.setMouseCallback('img', draw_circle)

while 1:
    cv2.imshow('img', img)
    k = cv2.waitKey(1)

    # 按下 'q' 退出
    if k == ord('m'):
        mode = not mode
    elif k == ord('q'):
        break

cv2.destroyAllWindows()
