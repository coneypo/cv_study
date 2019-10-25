import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 480)

print(cap.isOpened())

# cap.read()

while cap.isOpened():
    ret_flag, img_camera = cap.read()
    cv2.imshow("camera", img_camera)

    # 每帧数据延时 1ms, 延时为0, 读取的是静态帧
    k = cv2.waitKey(1)

    # 按下 's' 保存截图
    if k == ord('s'):
        cv2.imwrite("test.jpg", img_camera)

    # 按下 'q' 退出
    if k == ord('q'):
        break

# 释放所有摄像头
cap.release()

# 删除建立的所有窗口
cv2.destroyAllWindows()