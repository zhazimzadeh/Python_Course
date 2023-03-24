import cv2


img2=cv2.imread("Assignment_26\img2_converted.jpg")

x=img2.shape[0]
y=img2.shape[1]
for i in range(0,x//4):
    for j in range(90,y//4):
        if j-i>0:
            img2[i,j-i]=0

cv2.imshow("exercise5",img2)
cv2.imwrite("Assignment_26\death_symbol.jpg",img2)
cv2.waitKey()

