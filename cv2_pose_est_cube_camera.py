import numpy as np
import cv2
import glob

# refer to https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_pose/py_pose.html#pose-estimation

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(5,5,0)
objp = np.zeros((5 * 5, 3), np.float32)
objp[:, :2] = np.mgrid[0:5, 0:5].T.reshape(-1, 2)
axis = np.float32([[0, 0, 0], [0, 3, 0], [3, 3, 0], [3, 0, 0],
                   [0, 0, -3], [0, 3, -3], [3, 3, -3], [3, 0, -3]])

# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.

cap = cv2.VideoCapture(1)

# cap.set(propId, value)
cap.set(3, 480)


def draw(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1, 2)

    # draw ground floor in green
    # img = cv2.drawContours(img, [imgpts[:4]], -1, (0, 255, 0), -3)

    # print(imgpts)
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img_camera, "Landing here 0", (int(imgpts[0][0]), int(imgpts[0][1])), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img_camera, "Landing here 1", (int(imgpts[1][0]), int(imgpts[1][1])), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img_camera, "Landing here 2", (int(imgpts[2][0]), int(imgpts[2][1])), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

    # cv2.putText(img_camera, "Landing here 01", (int(imgpts[2][0]), int(imgpts[2][1])), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

    # draw pillars in blue color
    for i, j in zip(range(4), range(4, 8)):
        img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]), (255), 3)

    # draw top layer in red color
    img = cv2.drawContours(img, [imgpts[4:]], -1, (0, 0, 255), 3)

    return img


while cap.isOpened():
    ret_flag, img_camera = cap.read()

    objpoints = []
    imgpoints = []

    img_gray = cv2.cvtColor(img_camera, cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(img_gray, (5, 5), None)
    # print(corners)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(img_gray, corners, (11, 11), (-1, -1), criteria)

        # print(ret)
        # print(corners2)
        # print(corners2.size)
        # print(corners2[0])
        # print(corners2[1])
        # print(corners2[0].size)

        imgpoints.append(corners2)

        # Draw and display the corners
        img_camera = cv2.drawChessboardCorners(img_camera, (5, 5), corners2, ret)

        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img_camera, "lower left",
                    (int(corners2[0][0][0]), int(corners2[0][0][1])), font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(img_camera, "upper left",
                    (int(corners2[4][0][0]), int(corners2[4][0][1])), font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(img_camera, "lower right",
                    (int(corners2[-5][0][0]), int(corners2[-5][0][1])), font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(img_camera, "upper right",
                    (int(corners2[-1][0][0]), int(corners2[-1][0][1])), font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)

    # print(img_gray.shape[::-1])
    # print('\n')
    try:
        # rvec - output rotation vector
        # tvec - output translation vector
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_gray.shape[::-1], None, None)
        # find the rotation and translation vec
        _, rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners2, mtx, dist)

        # project 3D points to image plane
        imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
        img_camera = draw(img_camera, corners2, imgpts)
    except:
        pass

    cv2.imshow('img', img_camera)

    k = cv2.waitKey(1)

    if k == ord('s'):
        cv2.imwrite("test.jpg", img_gray)

    if k == ord('q'):
        break

    # ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_gray[::-1], None, None)

cap.release()
cv2.destroyAllWindows()
