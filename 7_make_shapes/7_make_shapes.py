import cv2
import numpy as np

'''
cv2.line(image, start, end, color, thickness)
: 하나의 직선을 그립니다.
- start: 시작 좌표 (2차원)
- end: 종료 좌표 (2차원)
- thickness: 선의 두께
'''

image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.line(image, (0, 0), (255, 255), (255, 0, 0), 3)

cv2.imshow("Image", image)
cv2.waitKey(0)

'''
cv2.rectangle(image, start, end, color, thickness)
: 하나의 사각형을 그립니다.
- start: 시작 좌표 (2차원)
- end: 종료 좌표 (2차원)
- thickness: 선의 두께 (채우기: -1)
'''

image = cv2.rectangle(image, (20, 20), (255, 255), (255, 0, 0), 3)

cv2.imshow("Image", image)
cv2.waitKey(0)

'''
cv2.circle(image, center, radian, color, thickness)
: 하나의 사각형을 그립니다.
- center: 원의 중심 (2차원)
- radian: 반지름
- thickness: 선의 두께 (채우기: -1)
'''

image = cv2.circle(image, (255, 255), 30, (255, 0, 0), 3)

cv2.imshow("Image", image)
cv2.waitKey(0)

'''
cv2.polylines(image, points, isClosed, color, thickness)
: 하나의 다각형을 그립니다.
- points: 꼭지점들
- isClosed: 닫힌 도형 여부
- thickness: 선의 두께 (채우기: -1)
'''

points = np.array([[5, 5], [128, 258], [483, 444], [400, 150]])
image = cv2.polylines(image, [points], True, (0, 0, 255), 4)

cv2.imshow("Image", image)
cv2.waitKey(0)

'''
cv2.putText(image, text, position, font_type, font_scale, color)
: 하나의 텍스트를 추가합니다.
- position: 텍스트가 출력될 위치
- font_type: 글씨체
- font_scale: 글씨 크기 가중치
'''

image = cv2.putText(image, 'Hello World', (0, 200), cv2.FONT_ITALIC, 2, (255, 0, 0))

cv2.imshow("Image", image)
cv2.waitKey(0)