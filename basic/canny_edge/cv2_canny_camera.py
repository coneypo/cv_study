import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 480)

def nothing(x):
    pass


cv2.namedWindow('img')
cv2.createTrackbar('minVal', 'img', 0, 500, nothing)
cv2.createTrackbar('maxVal', 'img', 0, 500, nothing)


while cap.isOpened():

    minVal = cv2.getTrackbarPos('minVal', 'img')
    maxVal = cv2.getTrackbarPos('maxVal', 'img')

    ret_flag, img_camera = cap.read()
    edges = cv2.Canny(img_camera, minVal, maxVal, apertureSize=3)

    cv2.imshow("img", edges)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
