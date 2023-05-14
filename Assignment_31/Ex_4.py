import numpy as np
import cv2

image_gray=cv2.imread("Assignment_31/Input/building.png", cv2.IMREAD_GRAYSCALE)
# image_gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rows , cols = image_gray.shape
result_Vr = np.zeros((rows,cols))
result_Hr = np.zeros((rows,cols))

kernel_Vr = np.array([[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]])

kernel_Hr = np.array([[-1, -1, -1],
                      [ 0 , 0, 0],
                      [ 1, 1, 1 ]])

for i in range(1 , rows-1):
    for j in range(1 , cols-1):
        small = image_gray[i-1:i+2 , j-1:j+2]
        result_Hr[i,j] = np.sum(small*kernel_Hr)
        result_Vr[i,j] = np.sum(small*kernel_Vr)

result = np.concatenate((image_gray,result_Vr,result_Hr),axis=1)
cv2.imshow("result",result)
cv2.waitKey()
cv2.imwrite("Assignment_31/output/Edge_Hv.jpg",result)




