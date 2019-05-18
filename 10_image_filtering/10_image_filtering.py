import cv2
import numpy as np

image = cv2.imread('image.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)

kernel = 2
'''
ex) (2, 2)일 경우:
[1/4, 1/4]
[1/4, 1/4]
'''

'''
cv2.filter2D: 커널 단위로 필터를 적용합니다. (Basic Blur)
'''
kernel = np.ones((kernel, kernel), np.float32) / (kernel * 2)
dst = cv2.filter2D(image, -1, kernel)

cv2.imshow('Image', dst)
cv2.waitKey(0)

'''
* cv2.blur(image, kernel_size): Basic Blur
'''
dst = cv2.blur(image, (2, 2))
cv2.imshow('Image', dst)
cv2.waitKey(0)

'''
* cv2.GaussianBlur(image, kernel_size, sigmaX): Gaussian Blur
- kernel_size: 홀수
'''
dst = cv2.GaussianBlur(image, (9, 9), 0)
cv2.imshow('Image', dst)
cv2.waitKey(0)
