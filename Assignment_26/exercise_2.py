import cv2
import numpy as np



img1_rgb=cv2.imread("Assignment_26\pic1.jpg")
img2_rgb=cv2.imread("Assignment_26\pic2.jpg")
img1 = cv2.cvtColor(img1_rgb, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2_rgb, cv2.COLOR_BGR2GRAY)
img1_converted=np.zeros((img1_rgb.shape[0],img1_rgb.shape[1]))
img2_converted=np.zeros((img2_rgb.shape[0],img2_rgb.shape[1]))
for i in range(0, img1.shape[0]):
    for j in range(0, img1.shape[1]):
        img1_converted[i,j]=255-img1[i,j]


for i in range(0, img2.shape[0]):
    for j in range(0, img2.shape[1]):
        img2_converted[i,j]=255-img2[i,j]

cv2.imshow("exercise2",img1_converted)
cv2.imwrite("Assignment_26\img1_converted.jpg",img1_converted)
cv2.waitKey()
cv2.imshow("exercise2",img2_converted)
cv2.imwrite("Assignment_26\img2_converted.jpg",img2_converted)
cv2.waitKey()

