import cv2

image = cv2.imread('gray_image.jpg', cv2.IMREAD_GRAYSCALE)

'''
* cv2.threshold(src, thresh, maxval, type)
: 임계값을 기준으로 영상을 흑/백으로 분류
- thresh: 임계값 (전체 픽셀에 적용)
- maxval: 임계값을 넘었을 때 적용할 value
- type:
THRESH_BINARY
THRESH_BINARY_INV
THRESH_TRUNC
THRESH_TOZERO
THRESH_TOZERO_INV
'''

images = []
ret, thres1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
ret, thres2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
ret, thres3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
ret, thres4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
ret, thres5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)

images.append(thres1)
images.append(thres2)
images.append(thres3)
images.append(thres4)
images.append(thres5)

for i in images:
    cv2.imshow('Image', i)
    cv2.waitKey(0)

'''
* cv2.adaptiveThreshold(src, maxval, adaptive_method, type, block_size, C)
- maxval: 임계값
- adaptive_method: 임계값을 결정하는 계산 방법
ADAPTIVE_THRESH_MEAN_C: 주변영역의 평균값으로 결정
ADAPTIVE_THRESH_GAUSSIAN_C
- type: 임계값 적용 Type
- block_size: 임계값을 적용할 영역의 크기
'''
image = cv2.imread('hand_writing_image.jpg', cv2.IMREAD_GRAYSCALE)

thres1 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 3)
thres2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 3)

cv2.imshow('Image', thres1)
cv2.waitKey(0)

cv2.imshow('Image', thres2)
cv2.waitKey(0)

'''
* Otsu 이진화를 이용하여 임계값을 자동으로 계산
'''

ret, thres1 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Image', thres1)
cv2.waitKey(0)
