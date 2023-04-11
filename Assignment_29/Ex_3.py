import cv2

image=cv2.imread("Assignment_29\photo-to-sketch.jpg",0)
inverted=255-image
blurred=cv2.GaussianBlur(inverted,(21,21),0)
inverted_blurred=255-blurred

sketch = image/inverted_blurred
sketch = sketch * 255

cv2.imshow("sketch",sketch)
cv2.imwrite("Assignment_29/result_sketch.jpg",sketch)

cv2.waitKey()