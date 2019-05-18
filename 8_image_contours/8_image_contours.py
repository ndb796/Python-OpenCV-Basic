import cv2

'''
* cv2.findContours(image, mode, method)
: 이미지에서 Contour를 찾습니다. (Gray Thresh 전처리 필요)
- mode: Contour를 찾는 방법
1. RETR_EXTERNAL: 바깥쪽 Line만 찾기
2. RETR_LIST: 모든 Line을 찾지만, Hierarchy 구성 X
3. RETR_TREE: 모든 Line을 찾으며, 모든 Hierarchy 구성 O
- method: Contour를 찾는 근사치 방법
1. CHAIN_APPROX_NONE: 모든 Contour 포인트 저장
2. CHAIN_APPROX_SIMPLE: Contour Line을 그릴 수 있는 포인트만 저장

* cv2.drawContours(image, contours, contour_index, color, thickness )
: Contours를 그립니다.
- contour_index: 그리고자 하는 Contours Line (전체: -1)
'''

image = cv2.imread('image.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 127, 255, 0)

cv2.imshow('Image', thresh)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours)

image = cv2.drawContours(image, contours, -1, (0, 255, 0), 4)

cv2.imshow('Image', image)
cv2.waitKey(0)
