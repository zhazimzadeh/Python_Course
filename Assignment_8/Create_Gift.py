import imageio
import os

folder="Assignment_8/Images/"
file_list=sorted(os.listdir(folder))
Image_Frame=[]
for file in file_list:
    path=folder+file
    image=imageio.imread(path)
    Image_Frame.append(image)
imageio.mimsave("Assignment_8/MyGif.gif",Image_Frame)
print("Your gif was created Succesfully!")