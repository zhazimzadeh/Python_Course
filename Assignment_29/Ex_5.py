import numpy as np
import cv2
from skimage import data, filters
 
# Open Video
cap = cv2.VideoCapture("Assignment_29\cars.mp4")
 
# Randomly select 25 frames
frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)
 
# Store selected frames in an array
frames = []
for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    frames.append(frame)
 
# Calculate the median along the time axis
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)    
 
# Display median frame
cv2.imshow('frame', medianFrame)
cv2.imwrite("Assignment_29\cars.jpg",medianFrame)
cv2.waitKey(0)