import cv2

cap = cv2.VideoCapture(0)

# cap.set(propId, value)
# 设置视频参数: propId - 设置的视频参数, value - 设置的参数值
cap.set(3, 480)

# cap.isOpened() 返回 true/false, 检查摄像头初始化是否成功
print(cap.isOpened())

while cap.isOpened():
    ret_flag, img_camera = cap.read()
    img_gray = cv2.cvtColor(img_camera, cv2.COLOR_BGR2GRAY)
    img_thre = cv2.threshold(img_gray, 125, 255, cv2.THRESH_BINARY_INV)[1]

    # cv2.imshow("camera", img_gray)
    cv2.imshow("camera", img_thre)

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