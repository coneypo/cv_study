import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 100, (255,0,0), -1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('img')
cv2.setMouseCallback('img', draw_circle)

while 1:
    cv2.imshow('img', img)
    k = cv2.waitKey(1)

    # 按下 'q' 退出
    if k == ord('q'):
        break

cv2.destroyAllWindows()
