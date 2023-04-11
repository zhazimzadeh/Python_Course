import cv2
import numpy as np

img1=cv2.imread("Assignment_29\img1.jpg")
img2=cv2.imread("Assignment_29\img2.jpg")

img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

img1=img1.astype(np.float32)
img2=img2.astype(np.float32)

result1=(img1*4/5 +img2*1/5)
result1=result1.astype(np.int)

result2=(img1*3/5 +img2*2/5)
result2=result2.astype(np.int)

result3=(img1*2/5 +img2*3/5)
result3=result3.astype(np.int)

result4=(img1*1/5 +img2*4/5)
result4=result4.astype(np.int)


# cv2.imshow("result 1",result1)
# cv2.imwrite("Assignment_29/result1.jpg",result1)

# cv2.imshow("result 2",result2)
# cv2.imwrite("Assignment_29/result2.jpg",result2)

# cv2.imshow("result 3",result3)
# cv2.imwrite("Assignment_29/result3.jpg",result3)

# cv2.imshow("result 4",result4)
# cv2.imwrite("Assignment_29/result4.jpg",result4)

result = np.concatenate((img1,result1,result2,result3,result4, img2), axis=1)
cv2.imshow("Face Morphing",result)
cv2.imwrite("Assignment_29/FaceMorphing.jpg",result)

cv2.waitKey()