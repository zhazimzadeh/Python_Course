import cv2 
import numpy as np 

image = cv2.imread("Assignment_28\cats.jpeg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cat_datector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
faces = cat_datector.detectMultiScale(image,1.1)
cnt = 0
for face in faces :
    x , y , w , h  = face 
    cv2.rectangle(image , [x, y] , [x+w , y+h]  , [0,0,150] , 2)
    cnt += 1
cv2.putText(image , f"the number of cats : {cnt}" , (100 , 100) , cv2.FONT_HERSHEY_SIMPLEX , 2 , 0 , 8)
cv2.imshow("result" , image)
cv2.waitKey()