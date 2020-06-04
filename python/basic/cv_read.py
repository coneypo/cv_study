import cv2

img_rd = cv2.imread("../photos/test_1.jpg")
# print(img_rd.shape)
# print(type(img_rd))

img_new = img_rd[-2:, -2:]
print("img_rd[-2:, -2:]:", '\n', img_rd[-2:, -2:], '\n')
print("img_rd[-2:, -2:][0]:", '\n',  img_rd[-2:, -2:][0], '\n')
print(img_rd[:2, -2:].shape)
print('\n')

print('NEW')
img_new_gray = cv2.cvtColor(img_new, cv2.COLOR_BGR2GRAY)
print(img_new_gray)
print(img_new_gray.shape)

img_new_2_gray = cv2.cvtColor(img_rd[:100, 20:], cv2.COLOR_BGR2GRAY)


cv2.imshow("21", img_new_2_gray)
cv2.waitKey(0)