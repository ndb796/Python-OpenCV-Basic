import os
import cv2
import numpy as np

FILE_NAME = 'trained.npz'

BLUE = 0
GREEN = 1
RED = 2

# 특정한 색상의 모든 단어가 포함된 이미지를 추출합니다.
def get_chars(image, color):
    height = image.shape[0]
    width = image.shape[1]

    other_1 = (color + 1) % 3
    other_2 = (color + 2) % 3

    # 해당하지 않는 색상의 글자는 모두 검은색으로 바꾸어버립니다.
    for i in range(0, height):
        for j in range(0, width):
            if image[i, j, other_1] == 255:
                image[i, j] = [0, 0, 0]

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

    return image


# 전체 이미지에서 왼쪽부터 한 단어씩 이미지를 추출합니다.
def extract_chars(image):
    chars = []
    colors = [BLUE, GREEN, RED]
    for color in colors:
        image_from_one_color = get_chars(image.copy(), color)
        image_gray = cv2.cvtColor(image_from_one_color, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(image_gray, 127, 255, 0)

        # RETR_EXTERNAL 옵션으로 숫자의 외각을 기준으로 분리
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            # 추출된 이미지 크기가 50 이상인 경우만 실제 문자 데이터임
            area = cv2.contourArea(cnt)
            if area > 50:
                x, y, width, height = cv2.boundingRect(cnt)
                roi = image_gray[y:y+height, x:x+width]
                chars.append((x, roi))

    chars = sorted(chars, key=lambda char: char[0])
    return chars


# 특정한 이미지를 (20 x 20) 크기로 Scaling 합니다.
def resize20(image):
    resized = cv2.resize(image, (20, 20))
    return resized.reshape(-1, 400).astype(np.float32)


image = cv2.imread("image_6.png")
chars = extract_chars(image)

for char in chars:
    cv2.imshow('Image', char[1])
    input = cv2.waitKey(0)

    if input >= 48 and input <= 57:
        resized = cv2.resize(char[1], (20, 20))
        path = './training_data/' + str(input - 48) + '/'
        file_count = len(next(os.walk(path))[2])
        cv2.imwrite('./training_data/' + str(input - 48) + '/' +
                    str(file_count + 1) + '.png', resized)
    elif input == ord('a') or input == ord('b') or input == ord('c'):
        resized = cv2.resize(char[1], (20, 20))
        path = './training_data/' + str(input - ord('a') + 10) + '/'
        file_count = len(next(os.walk(path))[2])
        cv2.imwrite('./training_data/' + str(input - ord('a') + 10) + '/' +
                    str(file_count + 1) + '.png', resized)