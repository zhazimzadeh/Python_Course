import numpy as np
import cv2

image=cv2.imread("Assignment_31/Input/flower_input.jpg")
image_gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rows, cols = image_gray.shape
result = np.zeros((rows, cols),dtype=np.uint8) 
n=30
filter = np.ones((n*2+1, n*2+1), np.float32)/((n*2+1)*(n*2+1))

for i in range(n, rows-n):
    for j in range(n, cols-n):
        if image_gray[i,j] < 125:
            small = image_gray[i-n:i+n+1 , j-n:j+n+1]
            result[i,j] = np.sum( small * filter )
        else:
            result[i,j] = image_gray[i,j]

cv2.imshow("result",result)   
cv2.waitKey()   
cv2.imwrite('Assignment_31/output/blured_background.jpg',result)


