import cv2
import numpy as np

img_mask = cv2.imread("Assignment_29/room_mask.jpg")
img_floor = cv2.imread("Assignment_29/room_foreground.jpg")
img_room = cv2.imread("Assignment_29/room_background.jpg")

img_mask=cv2.cvtColor(img_mask,cv2.COLOR_BGR2GRAY)
img_floor=cv2.cvtColor(img_floor,cv2.COLOR_BGR2GRAY)
img_room=cv2.cvtColor(img_room,cv2.COLOR_BGR2GRAY)

img_mask = img_mask / 255.0
img_room = img_room * (1 - img_mask)
img_floor = img_floor * img_mask
result = img_floor+img_room

cv2.imshow("Virtual Decoration",result)
cv2.imwrite('Assignment_29/VirtualDecoration.jpg',result)
cv2.waitKey()