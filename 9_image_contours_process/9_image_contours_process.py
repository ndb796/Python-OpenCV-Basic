import cv2

image = cv2.imread('image.png')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 230, 255, 0)
thresh = cv2.bitwise_not(thresh)
cv2.imshow('Image', thresh)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 4)
cv2.imshow('Image', image)
cv2.waitKey(0)

'''
cv2.moments(contour): Contour를 구분할 수 있는 특징을 추출합니다.
'''
# 첫 번째 Contour를 선택합니다.
contour = contours[0]
M = cv2.moments(contour)

'''
* cv2.contourArea(contour): Contour의 면적을 구합니다.
* cv2.arcLength(contour): Contour의 둘레를 구합니다.
* cv2.approxPolyDP(curve, epsilon, closed): 근사치 Contours Line을 구합니다.
- curve: Contours 배열
- epsilon: 최대 거리 (클수록 Point 개수 감소)
- closed: 폐곡선 여부
'''

area = cv2.contourArea(contour)
print(area)
length = cv2.arcLength(contour, True)
print(length)
epsilon = 0.01 * cv2.arcLength(contour, True)
approx = cv2.approxPolyDP(contour, epsilon, True)
image = cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)

cv2.imshow('Image', image)
cv2.waitKey(0)

'''
* cv2.convexHull(contour): Convex Hull 알고리즘으로 외곽을 구합니다.
- 일반적으로 더 대략적인 형태의 외곽을 구할 수 있습니다.
'''
hull = cv2.convexHull(contour)
image = cv2.drawContours(image, [hull], -1, (255, 0, 0), 4)

cv2.imshow('Image', image)
cv2.waitKey(0)

'''
* cv2.boundingRect(contour): Contours Line을 포함하는 사각형을 그립니다.
'''

x, y, w, h = cv2.boundingRect(contour)

image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)

cv2.imshow('Image', image)
cv2.waitKey(0)
