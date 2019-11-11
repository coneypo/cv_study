import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 480)

while cap.isOpened():
    ret_flag, img_camera = cap.read()

    img_gray = cv2.cvtColor(img_camera, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(img_gray, 127, 255, 0)

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # contours = imutils.grab_contours(contours)

    # print(contours)
    img_camera = cv2.drawContours(img_camera, contours, 3, (0, 255, 0), 3)

    cv2.imshow("camera", img_camera)

    k = cv2.waitKey(1)

    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()