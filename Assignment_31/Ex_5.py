import numpy as np
import cv2
def Noice_Reduction(img,n_kernel):
    kernel= np.ones((n_kernel,n_kernel)) / (n_kernel*n_kernel)
    rows , cols = img.shape
    result = np.zeros((rows,cols),dtype=np.uint8)

    n = (n_kernel-1) // 2
    for i in range(n , rows-n):
        for j in range(n , cols-n):
            small = img[i-n:i+n+1 , j-n:j+n+1]
            result[i,j] = np.sum(small*kernel)

    return result



image_gray=cv2.imread("Assignment_31/Input/image_noisy.png", cv2.IMREAD_GRAYSCALE)

# image_gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

result_3 = Noice_Reduction(image_gray,3)
result_5 = Noice_Reduction(image_gray,5)
result_15 = Noice_Reduction(image_gray,15)

result = np.concatenate((image_gray,result_3,result_5,result_15),axis=1)
cv2.imshow("result",result)
cv2.waitKey()
cv2.imwrite("Assignment_31/Output/Nr_circle.jpg",result)