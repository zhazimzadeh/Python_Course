import cv2
import numpy as np


img = np.zeros((255, 100))
img[0:100,0:100] = 255


for i in range(255):
    for j in range(100):
        img[i,j]=255-i


cv2.imshow("exercise5",img)
cv2.imwrite("Assignment_26\geradiant.jpg",img)
cv2.waitKey()
