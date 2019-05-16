import cv2

image = cv2.imread('2_image_operation.png')

# 이미지 Numpy 객체의 특정 픽셀을 가리킵니다.
px = image[100, 100]
# B, G, R 순서로 출력됩니다.
# Gray Scale: B, G, R로 구분되지 않습니다.
print(px)
# R 값만 출력하기
print(px[2])
# 픽셀 수 및 이미지 크기 확인
print(image.shape)
print(image.size)

'''
# 특정 픽셀의 색상은 마음대로 변경 가능
for i in range(0, 100):
    for j in range(0, 100):
        image[i, j] = [0, 0, 0]
'''

cv2.imshow('Image', image)
cv2.waitKey(0)

# Numpy Slicing: ROI 처리 가능
logo = image[20:150, 70:200]
cv2.imshow('Image', logo)
cv2.waitKey(0)

# ROI 단위로 이미지 복사하기
image[0:130, 0:130] = logo
cv2.imshow('Image', image)
cv2.waitKey(0)

# 특정 색상만 보여주기 (0: Blue, 1: Green, 2: Red)
cv2.imshow('Image', image[:, :, 0])
cv2.waitKey(0)

# 특정 색상만 제거하기
image[:, :, 2] = 0
cv2.imshow('Image', image)
cv2.waitKey(0)
