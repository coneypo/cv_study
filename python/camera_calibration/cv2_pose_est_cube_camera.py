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
# axis = np.float32([[0, 0, 0], [0, 4, 0], [4, 4, 0], [4, 0, 0],
#                    [0, 0, -4], [0, 4, -4], [4, 4, -4], [4, 0, -4]])

# axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)
# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.

cap = cv2.VideoCapture(0)

# cap.set(propId, value)
cap.set(3, 480)


def sort_pos(pos_1, pos_2, pos_3, pos_4):
    pos_list = [pos_1, pos_2, pos_3, pos_4]
    pos_list = sorted(pos_list, key=lambda t: t[0])

    pos_list_left = pos_list[:2]
    pos_list_left = sorted(pos_list_left, key=lambda t: t[1])
    left_upper_pos = pos_list_left[0]
    left_lower_pos = pos_list_left[1]

    pos_list_right = pos_list[2:]
    pos_list_right = sorted(pos_list_right, key=lambda t: t[1])
    right_upper_pos = pos_list_right[0]
    right_lower_pos = pos_list_right[1]

    return left_upper_pos, left_lower_pos, right_upper_pos, right_lower_pos


font = cv2.FONT_HERSHEY_COMPLEX

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

        pos_1 = tuple([int(corners2[0][0][0]), int(corners2[0][0][1])])
        pos_2 = tuple([int(corners2[4][0][0]), int(corners2[4][0][1])])
        pos_3 = tuple([int(corners2[-5][0][0]), int(corners2[-5][0][1])])
        pos_4 = tuple([int(corners2[-1][0][0]), int(corners2[-1][0][1])])

        pos_list = [pos_1, pos_2, pos_3, pos_4]
        pos_list = sorted(pos_list, key=lambda t: t[0])

        pos_list_left = pos_list[:2]
        pos_list_left = sorted(pos_list_left, key=lambda t: t[1])
        left_upper_pos = pos_list_left[0]
        left_lower_pos = pos_list_left[1]

        pos_list_right = pos_list[2:]
        pos_list_right = sorted(pos_list_right, key=lambda t: t[1])
        right_upper_pos = pos_list_right[0]
        right_lower_pos = pos_list_right[1]

        text_intel = "intel"
        text_size = cv2.getTextSize(text_intel, font, 1, 1)[0][0]
        # print(text_size)

        centre_pos = (int((int(left_upper_pos[0]) + int(right_upper_pos[0])-text_size) / 2), int((int(left_upper_pos[1]) + int(left_lower_pos[1])) / 2))
        print("left upper:  ", left_upper_pos)
        print("left lower:  ", left_lower_pos)
        print("right upper: ", right_upper_pos)
        print("right lower: ", right_lower_pos)
        print("centre:      ", centre_pos)
        print('\n')

        cv2.putText(img_camera, "upper left", left_upper_pos, font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(img_camera, "lower left", left_lower_pos, font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(img_camera, "upper right", right_upper_pos, font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(img_camera, "lower right", right_lower_pos, font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
    try:
        print('##########################')
        # rvec - output rotation vector
        # tvec - output translation vector
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_gray.shape[::-1], None, None)

        # find the rotation and translation vec
        _, rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners2, mtx, dist)

        # project 3D points to image plane
        imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)

        print(type(imgpts))

        ### Draw ###
        imgpts = np.int32(imgpts).reshape(-1, 2)
        print(imgpts.size)
        print(imgpts.shape)
        # 1. draw ground floor in green
        img_camera = cv2.drawContours(img_camera, [imgpts[:4]], -1, (0, 255, 0), -3)

        # 2. draw pillars in blue color
        for i, j in zip(range(4), range(4, 8)):
           img_camera = cv2.line(img_camera, tuple(imgpts[i]), tuple(imgpts[j]), (255), 3)

        # 3. draw top layer in red color
        img_camera = cv2.drawContours(img_camera, [imgpts[4:]], -1, (0, 0, 255), 3)

        # 4. draw intel log
        cv2.putText(img_camera, text_intel, centre_pos, font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        # 5. draw corners
        corner = tuple(corners[0].ravel())
        # cv2.line(img_camera, corner, tuple(imgpts[0].ravel()), (255,0,0),5)
        # cv2.line(img_camera, corner, tuple(imgpts[1].ravel()), (0,255, 0),5)
        # cv2.line(img_camera, corner, tuple(imgpts[2].ravel()), (0,0,255),5)

        ## End drawing ###

    except:
        pass

    cv2.imshow('Landing area', img_camera)

    k = cv2.waitKey(1)

    if k == ord('s'):
        cv2.imwrite("test.jpg", img_gray)

    if k == ord('q'):
        break

    # ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_gray[::-1], None, None)

cap.release()
cv2.destroyAllWindows()
