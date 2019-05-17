import time
import cv2
import numpy as np
import requests
import shutil
import re


def remove_first_0(string):
    temp = []
    for i in string:
        if i == '+' or i == '-' or i == '*':
            temp.append(i)
    split = re.split('\*|\+|-', string)
    i = 0
    temp_count = 0
    result = ""
    for a in split:
        a = a.lstrip('0')
        if a == '':
            a = '0'
        result += a
        if i < len(split) - 1:
            result += temp[temp_count]
            temp_count = temp_count + 1
        i = i + 1
    return result


FILE_NAME = 'trained.npz'

BLUE = 0
GREEN = 1
RED = 2

# 특정한 색상의 모든 단어가 포함된 이미지를 추출합니다.
def get_chars(image, color):
    other_1 = (color + 1) % 3
    other_2 = (color + 2) % 3

    # 해당하지 않는 색상의 글자는 모두 검은색으로 바꾸어버립니다.
    c = image[:, :, other_1] == 255
    image[c] = [0, 0, 0]

    c = image[:, :, other_2] == 255
    image[c] = [0, 0, 0]

    # 다른 두 색 섞인 것을 제거하기 위해 AA 미만의 색을 검은색으로 바꿉니다.
    c = image[:, :, color] < 170
    image[c] = [0, 0, 0]

    # 검은색이 아닌 경우, 하얀색으로 바꾸어버립니다.
    c = image[:, :, color] != 0
    image[c] = [255, 255, 255]

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


def check(test, train, train_labels):
    # 가장 가까운 K개의 글자를 찾아, 어떤 숫자에 해당하는지 찾습니다. (테스트 데이터 개수에 따라서 조절)
    ret, result, neighbours, dist = knn.findNearest(test, k=1)
    return result


# 파일로부터 학습 데이터를 불러옵니다.
def load_train_data(file_name):
    with np.load(file_name) as data:
        train = data['train']
        train_labels = data['train_labels']
    return train, train_labels


# 각 글자의 (1 x 400) 데이터와 정답 (0 ~ 9, +, *)
train, train_labels = load_train_data(FILE_NAME)

knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)


def get_result(file_name):
    image = cv2.imread(file_name)
    chars = extract_chars(image)

    result_string = ""

    for char in chars:
        test = resize20(char[1])
        matched = check(test, train, train_labels)
        if int(matched) < 10:
            result_string += str(int(matched))
            continue
        if int(matched) == 10:
            matched = '+'
        elif int(matched) == 11:
            matched = '-'
        elif int(matched) == 12:
            matched = '*'
        result_string += matched

    return result_string


count = 0

with requests.Session() as s:
    url = "http://3a905668.ngrok.io"
    response = s.post(url + "/start", data=None)
    image_url = url + response.text
    print('Problem ' + str(count) + ': ' + image_url)
    response = s.get(image_url, stream=True)
    target_image = './target_images/' + str(count) + '.png'
    with open(target_image, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    answer_string = get_result(target_image)
    print('String: ' + answer_string)
    answer_string = remove_first_0(answer_string)
    answer = str(eval(answer_string))
    print('Answer: ' + answer)
    for i in range(0, 100):
        count = count + 1
        params = {'ans': answer}
        start_time = time.time()
        response = s.post(url + "/check", params)
        print('Server Return: ' + str(response.json()))
        image_url = url + response.json()['url']
        print('Problem ' + str(count) + ': ' + image_url)
        response = s.get(image_url, stream=True)
        target_image = './target_images/' + str(count) + '.png'
        with open(target_image, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        print("--- %s seconds ---" % (time.time() - start_time))
        answer_string = get_result(target_image)
        print('String: ' + answer_string)
        answer_string = remove_first_0(answer_string)
        answer = str(eval(answer_string))
        print('Answer: ' + answer)


'''
# 학습 모드
save_npz = True

for char in chars:
    test = resize20(char[1])
    cv2.imshow("Image", test)
    result = check(test, train, train_labels)
    print(result)

    k = cv2.waitKey(0)
'''
