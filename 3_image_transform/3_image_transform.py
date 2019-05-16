import cv2
import numpy as np

image = cv2.imread('image.png')

# 행과 열 정보만 저장합니다.
height, width = image.shape[:2]

'''
cv2.resize(image, dsize, fx, fy, interpolation)
: 이미지의 크기를 조절합니다.
- dsize: Manual Size
- fx: 가로 비율
- fy: 세로 비율
- interpolation: 보간법
'''
expand = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_AREA)
cv2.imshow('Image', expand)
cv2.waitKey(0)

shrink = cv2.resize(image, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
cv2.imshow('Image', shrink)
cv2.waitKey(0)

'''
cv2.warpAffine(src, M, dsize):
이미지의 위치를 변경합니다.
- M: 변환 행렬
- dsize: 출력 크기
'''
M = np.float32([[1, 0, 50], [0, 1, 10]])
dst = cv2.warpAffine(image, M, (width, height))
cv2.imshow('Image', dst)
cv2.waitKey(0)

'''
* cv2.getRotationMatrix2D(center, angle, scale):
이미지 회전을 위한 변환 행렬을 생성합니다.
- center: 회전 중심
- angle: 회전 각도
- scale: scale factor
'''
M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5)
dst = cv2.warpAffine(image, M, (width, height))
cv2.imshow('Image', dst)
cv2.waitKey(0)
