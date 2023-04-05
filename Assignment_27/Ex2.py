import cv2
import numpy as np

# for create gif
import imageio
import os



#Just for test
# image=np.ones((500,800), dtype=np.uint8) *255
# cv2.rectangle(image,(30,35), (350,410), 0,20 )
# cv2.circle(image, (600,200), 100, 120, 10)
# cv2.line(image, (100,100), (700,150), 180, 15)
# cv2.putText(image, "This text is test", (20,200), cv2.FONT_HERSHEY_SIMPLEX, 1, 100)


# for create gif
folder="Assignment_27/noise/"
file_list=sorted(os.listdir(folder))
Image_Frame=[]
for file in file_list:
    path=folder+file
    image=imageio.imread(path)
    Image_Frame.append(image)
imageio.mimsave("Assignment_27/MyGif.gif",Image_Frame)
print("Your gif was created Succesfully!")


image_tv = cv2.imread("Assignment_27\TV.jpg")
image_tv = cv2.cvtColor(image_tv, cv2.COLOR_BGR2GRAY)

while True:
    image=np.random.random((200,200))*255
    image=np.array(image,dtype=np.uint8)
    image_tv[33:149,35:190]=image[33:149,35:190]
    cv2.imshow("result",image_tv)
    if cv2.waitKey(25) & 0XFF == ord('q'):
        break

