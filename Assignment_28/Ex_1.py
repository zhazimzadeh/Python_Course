import random
import cv2
import numpy as np

width = 500
lenght = 700
Soccer = np.ones((width,lenght,3))
Soccer = np.array(Soccer, dtype=np.uint8)

cv2.rectangle(Soccer, (0,0), (70,500), (0,100,0),100)
cv2.rectangle(Soccer, (170,0), (220,500), (0,200,0),100)
cv2.rectangle(Soccer, (320,0), (370,500), (0,100,0),100)
cv2.rectangle(Soccer, (470,0), (520,500), (0,200,0),100)
cv2.rectangle(Soccer, (620,0), (670,500), (0,100,0),100)

cv2.rectangle(Soccer, (30,30), (lenght - 30,width - 30), (255,255,255),3)
cv2.rectangle(Soccer, (30,140), (140,width - 140), (255,255,255),3)
cv2.rectangle(Soccer, (30,180), (80,width - 180), (255,255,255),3)
cv2.rectangle(Soccer, (lenght - 30,140), (lenght - 140,width - 140), (255,255,255),3)
cv2.rectangle(Soccer, (lenght - 30,180), (lenght - 80,width - 180), (255,255,255),3)
cv2.circle(Soccer, (lenght//2,width//2), 70, (255,255,255),3)
cv2.circle(Soccer, (lenght//2,width//2), 0, (255,255,255),20)
cv2.line(Soccer, (lenght//2,30), (lenght//2,width-30), (255,255,255),3)


cv2.imshow('result',Soccer)
cv2.imwrite('Assignment_28\Soccer.jpg',Soccer)
cv2.waitKey()