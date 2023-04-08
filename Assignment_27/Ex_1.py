import cv2

image = cv2.imread("Assignment_27\Bat.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rows, cols =image.shape
thr=100

# option 1
# for i in range(rows):
#     for j in range(cols):
#         if image[i,j] > thr:
#             image[i,j]=255
#         else: image [i,j]=0

#option 2
# image[image > thr] = 255
# image[image <= thr] = 0

# option 3
_, image = cv2.threshold(image,thr,255,cv2.THRESH_BINARY_INV)

cv2.imshow("Result",image)
cv2.imwrite("Assignment_27\logo.jpg",image)
cv2.waitKey()