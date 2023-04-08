import cv2
import numpy as np
import time

landscape_org = cv2.imread('Assignment_27\landscape.jpeg')
landscape = cv2.cvtColor(landscape_org,cv2.COLOR_BGR2GRAY)
rows, cols = landscape.shape
writer = cv2.VideoWriter("Assignment_27\Snow.mp4", cv2.VideoWriter_fourcc(*'MPJG'), 40, (cols, rows))

snow=np.random.random((rows,cols))*255
snow=np.array(snow,dtype=np.uint8)
snow_temp=np.zeros((rows,cols))

while True:
    landscape = cv2.cvtColor(landscape_org,cv2.COLOR_BGR2GRAY)
    for i in range(0,len(landscape)):
        landscape[snow > 230] = 255
    x=len(snow)
    snow_temp[1:x]=snow[0:x-1]
    snow_temp[0]=snow[x-1]
    snow=snow_temp

    landscape_snow = cv2.cvtColor(landscape, cv2.COLOR_GRAY2BGR)
    writer.write(landscape_snow)
    cv2.imshow('result', landscape_snow)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

writer.release()