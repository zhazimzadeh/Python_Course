import cv2
import numpy as np

img3_rgb=cv2.imread("Assignment_26\pic3.jpg")
img3 = cv2.cvtColor(img3_rgb, cv2.COLOR_BGR2GRAY)
x=img3.shape[0]
y=img3.shape[1]
img3_rotated = np.zeros((x, y))

for i in range(img3.shape[0]):
    for j in range(img3.shape[1]):
        img3_rotated[i,j] = img3[x - i -1,y - j -1]

cv2.imshow("exercise3",img3_rotated)
cv2.imwrite("Assignment_26\img3_rotated.jpg",img3_rotated)
cv2.waitKey()
