import cv2
import numpy as np


chessboard = np.zeros((400, 400))
for i in range(8):
    for j in range(8):
        chessboard[i*50:(i+1)*50,j*50:(j+1)*50] = ((i+j)%2)*255

cv2.imshow("exercise1",chessboard)
cv2.imwrite("Assignment_26\chessboard.jpg",chessboard)
cv2.waitKey()
