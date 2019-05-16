import cv2
import numpy as np

img = cv2.imread('digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 세로로 50줄, 가로로 100줄로 사진을 나눕니다.
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
x = np.array(cells)

'''
모든 글자는 (20 x 20) 크기로 나누어집니다.
print(x[0, 5].shape)
다음과 같이 하나씩 글자를 출력할 수 있습니다.
cv2.imshow('Image', x[0, 5])
cv2.waitKey(0)
다음과 같이 하나씩 글자를 저장할 수 있습니다.
cv2.imwrite('test0.png', x[0, 0])
cv2.imwrite('test1.png', x[5, 0])
cv2.imwrite('test2.png', x[10, 0])
cv2.imwrite('test3.png', x[15, 0])
cv2.imwrite('test4.png', x[20, 0])
cv2.imwrite('test5.png', x[25, 0])
cv2.imwrite('test6.png', x[30, 0])
cv2.imwrite('test7.png', x[35, 0])
cv2.imwrite('test8.png', x[40, 0])
cv2.imwrite('test9.png', x[45, 0])
'''

# 각 (20 X 20) 크기의 사진을 한 줄(1 X 400)으로 바꿉니다.
train = x[:, :].reshape(-1, 400).astype(np.float32)

# 0이 500개, 1이 500개, ... 로 총 5,000개가 들어가는 (1 x 5000) 배열을 만듭니다.
k = np.arange(10)
train_labels = np.repeat(k, 500)[:, np.newaxis]

np.savez("trained.npz", train=train, train_labels=train_labels)