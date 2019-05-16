import os
import cv2
import numpy as np

file_names = list(range(0, 13))
train = []
train_labels = []

for file_name in file_names:
    path = './training_data/' + str(file_name) + '/'
    file_count = len(next(os.walk(path))[2])
    for i in range(1, file_count + 1):
        img = cv2.imread(path + str(i) + '.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        train.append(gray)
        train_labels.append(file_name)

x = np.array(train)

# 각 (20 X 20) 크기의 사진을 한 줄(1 X 400)으로 바꿉니다.
train = x[:, :].reshape(-1, 400).astype(np.float32)

# 0 ~ 9, +, *로 정답 라벨을 생성합니다.
# 동일하게 숫자 형태가 들어가야 하므로 +: 10, -: 11, *: 12로 표현
train_labels = np.array(train_labels)[:, np.newaxis]

np.savez("trained.npz", train=train, train_labels=train_labels)
