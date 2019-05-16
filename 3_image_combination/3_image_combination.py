import cv2

image_1 = cv2.imread('image_1.jpg')
image_2 = cv2.imread('image_2.png')

'''
* cv2.add(): Saturation 연산을 수행
0보다 작으면 0, 255보다 크면 255로 표현
* Numpy Add: Modulo 연산을 수행
256은 0, 257은 1로 표현
'''

result = cv2.add(image_1, image_2)
cv2.imshow('Image', result)
cv2.waitKey(0)

result = image_1 + image_2
cv2.imshow('Image', result)
cv2.waitKey(0)
