import time
import cv2
import numpy as np

BLUE = 0
GREEN = 1
RED = 2


# 특정한 색상의 모든 단어가 포함된 이미지를 추출합니다.
def get_chars(image, color):
    height = image.shape[0]
    width = image.shape[1]

    other_1 = (color + 1) % 3
    other_2 = (color + 2) % 3

    start_time = time.time()
    print(image.sum(axis=2))

    c = image[:, :, other_1] == 255
    image[c] = [0, 0, 0]

    c = image[:, :, other_2] == 255
    image[c] = [0, 0, 0]

    c = image[:, :, color] < 170
    image[c] = [0, 0, 0]

    c = image[:, :, color] != 0
    image[c] = [255, 255, 255]

    '''
    for i in range(0, height):
        for j in range(0, width):
            if image[i, j, other_2] == 255:
                image[i, j] = [0, 0, 0]

    # 다른 두 색 섞인 것을 제거하기 위해 AA 미만의 색을 검은색으로 바꿉니다.
    for i in range(0, height):
        for j in range(0, width):
            if image[i, j, color] < 170:
                image[i, j] = [0, 0, 0]

    # 검은색이 아닌 경우, 하얀색으로 바꾸어버립니다.
    for i in range(0, height):
        for j in range(0, width):
            if image[i, j, color] != 0:
                image[i, j] = [255, 255, 255]
    '''
    print("--- %s seconds ---" % (time.time() - start_time))

    return image


image = cv2.imread('image_6.png', cv2.IMREAD_COLOR)

image_from_one_color = get_chars(image.copy(), BLUE)

# image_gray = cv2.cvtColor(image_from_one_color, cv2.COLOR_BGR2GRAY)

cv2.imshow('Image Gray', image_from_one_color)
cv2.waitKey(0)