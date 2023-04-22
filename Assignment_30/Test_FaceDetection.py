import numpy as np
import cv2
import tensorflow as tf
from functools import partial
import time
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel



fd = UltraLightFaceDetecion("Assignment_30\weights\RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("Assignment_30\weights\coor_2d106.tflite")

image = cv2.imread("Assignment_30/input/face.jpeg")
fruit = cv2.imread("Assignment_30/input/fruit.jpg")
fruit=cv2.resize(fruit,(image.shape[0],image.shape[1]))
color = (0, 0, 255)
start_time = time.perf_counter()
boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
#   for i,p in enumerate(np.round(pred).astype(np.int)):
        # cv2.circle(image, tuple(p), 1, color, 1)
        # cv2.putText(image,str(i),tuple(p),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0))

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
    print(lips_landmarks)

    x_l,y_l,w_l,h_l=cv2.boundingRect(lips_landmarks)

    eye1_landmarks=np.array(eye1_landmarks,dtype=int)
    print(eye1_landmarks)

    x_e1,y_e1,w_e1,h_e1=cv2.boundingRect(eye1_landmarks)

    eye2_landmarks=np.array(eye2_landmarks,dtype=int)
    print(eye2_landmarks)

    x_e2,y_e2,w_e2,h_e2=cv2.boundingRect(eye2_landmarks)

mask=np.zeros(image.shape,dtype=np.uint8)
cv2.drawContours(mask, [lips_landmarks], -1, (255,255,255),-1)
cv2.drawContours(mask, [eye1_landmarks], -1, (255,255,255),-1)
cv2.drawContours(mask, [eye2_landmarks], -1, (255,255,255),-1)
mask=mask//255
result=image * mask
result_lip=result[y_l:y_l+h_l,x_l:x_l+w_l]
result_eye1=result[y_e1:y_e1+h_e1,x_e1:x_e1+w_e1]
result_eye2=result[y_e2:y_e2+h_e2,x_e2:x_e2+w_e2]
print(time.perf_counter() - start_time)

fruit[y_l+200:y_l+h_l+200,x_l-150:x_l+w_l-150]=result_lip
fruit[y_l:y_l+h_e1,x_l-50:x_l+w_e1-50]=result_eye1
fruit[y_l:y_l+h_e2,x_l-200:x_l+w_e2-200]=result_eye2

cv2.imshow("result", fruit )
cv2.waitKey()
cv2.imwrite("Assignment_30/output/result_lip.jpg",result_lip)
cv2.imwrite("Assignment_30/output/result_eye1.jpg",result_eye1)
cv2.imwrite("Assignment_30/output/result_eye2.jpg",result_eye2)
cv2.imwrite("Assignment_30/output/result_fruit.jpg",fruit)



