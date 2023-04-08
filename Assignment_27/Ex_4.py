import cv2
import numpy as np

cap = cv2.VideoCapture(0)
_, frame = cap.read()
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
rows, cols = frame.shape

writer = cv2.VideoWriter('Assignment_27\Jila.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 30, (cols, rows))

while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_ROI = frame[(rows//2 - 50):(rows//2 + 50), (cols//2 - 50):(cols//2 + 50)]
    frame_Blur = cv2.GaussianBlur(frame, None, 5, 5, 5   )
    cv2.rectangle(frame_Blur, (cols//2 - 50,rows//2 - 50), (cols//2 + 50,rows//2 + 50), 0,5)
    mean = np.mean(frame_ROI)
    if mean > 150:
        color = 'White'
    elif mean < 70:
        color = 'Black'
    else:
        color = 'Gray'
    cv2.putText(frame_Blur, color, (cols//2 - 40,rows//2 - 80), cv2.FONT_HERSHEY_SIMPLEX, 1, 0, thickness= 3)
    frame_Blur[(rows//2 - 50):(rows//2 + 50), (cols//2 - 50):(cols//2 + 50)] = frame_ROI
    frame = cv2.cvtColor(frame_Blur, cv2.COLOR_GRAY2BGR)
    writer.write(frame)
    cv2.imshow('result', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

writer.release()
cap.release()
cv2.destroyAllWindows()
