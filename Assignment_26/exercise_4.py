import cv2
import numpy as np


my_char = np.zeros((100, 100))
my_char[0:100,0:100] = 255


my_char[10:20,20:80] = 0
my_char[20:30,70:80] = 0
my_char[30:40,60:70] = 0
my_char[40:50,50:60] = 0
my_char[50:60,40:50] = 0
my_char[60:70,30:40] = 0
my_char[70:80,20:30] = 0
my_char[80:90,20:80] = 0

cv2.imshow("exercise4",my_char)
cv2.imwrite("Assignment_26\my_char.jpg",my_char)
cv2.waitKey()
