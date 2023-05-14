import numpy as np
import matplotlib.pyplot as plt
import cv2

def histogram_calc(image):
    rows, cols=image.shape
    histogram=np.zeros(256)
    for px in range(256):
        for i in range(rows):
            for j in range(cols):
                if image[i][j]==px:
                    histogram[px]+=1

    return histogram

image=cv2.imread("Assignment_31/Input/building.png")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

result=histogram_calc(image)
# plt.plot(result)
# plt.hist(image.ravel(), 256)
plt.bar(np.arange(0, 256) ,result)
plt.show()