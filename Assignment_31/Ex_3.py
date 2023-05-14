import numpy as np
import cv2

image=cv2.imread("Assignment_31\Input\lion.webp")
image_gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rows , cols = image_gray.shape
result = np.zeros((rows,cols),dtype=np.uint8)
kernel= [[-1,-1,-1],
         [-1,8,-1],
         [-1,-1,-1]]
for i in range(1 , rows-1):
    for j in range(1 , cols-1):
        small = image_gray[i-1:i+2 , j-1:j+2]
        result[i,j] = np.sum(small*kernel)

cv2.imshow("result",result)
cv2.waitKey()
cv2.imwrite("Assignment_31/output/Edge_lion.jpg",result)