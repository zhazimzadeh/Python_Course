import cv2

img1 = cv2.imread("Assignment_29/a.png",0)
img2 = cv2.imread("Assignment_29/b.png", 0)
result = img2 - img1
cv2.imshow("secret",result)
cv2.imwrite("Assignment_29/secret.jpg", result)
cv2.waitKey()