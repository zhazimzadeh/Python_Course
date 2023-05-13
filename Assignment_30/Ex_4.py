import numpy as np
import cv2
import tensorflow as tf
from functools import partial
import time
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel


lip=[52 , 55, 56, 53, 59,58,61,68,67,71,63,64,65]
eye1=[89,90,87,91,93,96,94,95]
eye2=[39,42,40,41,35,36,33,37]


fd = UltraLightFaceDetecion("Assignment_30\weights\RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("Assignment_30\weights\coor_2d106.tflite")

face = cv2.imread("Assignment_30/input/face.jpeg")
fruit = cv2.imread("Assignment_30/input/fruit.jpg")
fruit=cv2.resize(fruit,[223,226])
# color = (0, 0, 255)
boxes, scores = fd.inference(face)

for pred in fa.get_landmarks(face, boxes):
#   for i,p in enumerate(np.round(pred).astype(np.int)):
        # cv2.circle(face, tuple(p), 1, color, 1)
        # cv2.putText(face,str(i),tuple(p),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0))
    lips_landmarks = []
    for  i in [52 , 55, 56, 53, 59,58,61,68,67,71,63,64,65]:
        lips_landmarks.append(pred[i])

    eye1_landmarks = []
    for  i in [89,90,87,91,93,96,94,95]:
        eye1_landmarks.append(pred[i])

    eye2_landmarks = []
    for  i in [39,42,40,41,35,36,33,37]:
        eye2_landmarks.append(pred[i])

    lips_landmarks=np.array(lips_landmarks,dtype=int)
    # print(lips_landmarks)

    x_l,y_l,w_l,h_l=cv2.boundingRect(lips_landmarks)

    eye1_landmarks=np.array(eye1_landmarks,dtype=int)
    # print(eye1_landmarks)

    x_e1,y_e1,w_e1,h_e1=cv2.boundingRect(eye1_landmarks)

    eye2_landmarks=np.array(eye2_landmarks,dtype=int)
    # print(eye2_landmarks)

    x_e2,y_e2,w_e2,h_e2=cv2.boundingRect(eye2_landmarks)

mask=np.zeros(face.shape,dtype=np.uint8)
cv2.drawContours(mask, [lips_landmarks], -1, (255,255,255),-1)
cv2.drawContours(mask, [eye1_landmarks], -1, (255,255,255),-1)
cv2.drawContours(mask, [eye2_landmarks], -1, (255,255,255),-1)
mask=mask//255
result=face * mask
result_lip=result[y_l:y_l+h_l,x_l:x_l+w_l]
result_eye1=result[y_e1:y_e1+h_e1,x_e1:x_e1+w_e1]
result_eye2=result[y_e2:y_e2+h_e2,x_e2:x_e2+w_e2]

doubled_lip=cv2.resize(result_lip, (w_l*2,h_l*2))
doubled_eye1=cv2.resize(result_eye1,(w_e1*2,h_e1*2))
doubled_eye2=cv2.resize(result_eye2,(w_e2*2,h_e2*2))

for i in range(h_l*2):
    for j in range(w_l*2):
        if doubled_lip[i][j][0] == 0 and doubled_lip[i][j][1] == 0 and doubled_lip[i][j][2] == 0:
            doubled_lip[i][j] = face[int(y_l-h_l//2)+i, int(x_l-w_l//2)+j]
face[int(y_l-h_l//2):int(y_l-h_l//2)+h_l*2, int(x_l-w_l//2):int(x_l-w_l//2)+w_l*2]=doubled_lip

for i in range(h_e1*2):
    for j in range(w_e1*2):
        if doubled_eye1[i][j][0] == 0 and doubled_eye1[i][j][1] == 0 and doubled_eye1[i][j][2] == 0:
            doubled_eye1[i][j] = face[int(y_e1-h_e1//2)+i, int(x_e1-w_e1//2)+j]
face[int(y_e1-h_e1//2):int(y_e1-h_e1//2)+h_e1*2, int(x_e1-w_e1//2):int(x_e1-w_e1//2)+w_e1*2]=doubled_eye1


for i in range(h_e2*2):
    for j in range(w_e2*2):
        if doubled_eye2[i][j][0] == 0 and doubled_eye2[i][j][1] == 0 and doubled_eye2[i][j][2] == 0:
            doubled_eye2[i][j] = face[int(y_e2-h_e2//2)+i, int(x_e2-w_e2//2)+j]
face[int(y_e2-h_e2//2):int(y_e2-h_e2//2)+h_e2*2, int(x_e2-w_e2//2):int(x_e2-w_e2//2)+w_e1*2]=doubled_eye2

cv2.imshow("result", face)
cv2.waitKey()
cv2.imwrite("Assignment_30/output/result_double.jpg", face)