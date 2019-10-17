import cv2

cap = cv2.VideoCapture(0)

# 设置视频参数: propId - 设置的视频参数, value - 设置的参数值
cap.set(3, 480)

while cap.isOpened():
    ret_flag, img_camera = cap.read()

    # 1. gray
    img_gray = cv2.cvtColor(img_camera, cv2.COLOR_BGR2GRAY)

    # 2. edge detect
    # threshold1: smaller, connect the lines
    # threshold2:  bigger, find edges
    img_edges = cv2.Canny(image=img_gray, threshold1=300, threshold2=0, apertureSize=3)

    # 3. thresholding
    img_thre = cv2.threshold(img_edges, 195, 255, cv2.THRESH_BINARY_INV)[1]

    # cv2.imshow("camera", img_gray)
    cv2.imshow("camera", img_edges)

    # 每帧数据延时 1ms, 延时为0, 读取的是静态帧
    k = cv2.waitKey(1)

    if k == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
