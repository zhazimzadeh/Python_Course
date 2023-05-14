#  Digital Image Processing: Filters

In these codes, we use [opencv](https://github.com/opencv/opencv).
we can install it with this command in terminal:
    
    pip install opencv-python


## exercise 1
In this exercise 1, we have written a function to get an image as input argument then calculate histogram and return it. Then, we have called the function and visualize the result with plt.plot(), plt.hist() and plt.bar().  :

Input:
![screenshot](Input\building.png)

Output of plt.hist():
![screenshot](output\histogram.png)

Output of plt.bar():
![screenshot](output\bar.png)

Output of plt.plot():
![screenshot](output\plot.png)


## exercise 2
In this exercise 2, We have focused on the flower and blured the background.

output:
![screenshot](Input\flower_input.jpg)

output:
![screenshot](output\blured_background.jpg)


## exercise 3
In this exercise 3, we have used a Laplacian Operator to detect edges of image.

    [-1, -1, -1]
    [-1,  8, -1]
    [-1, -1, -1]

Input:
![screenshot](input\lion.webp)
output:
![screenshot](output\edge_lion.jpg)

## exercise 4

In this exercise ,we have used a suitable kernel to detect vertical and horizontal edges of image.

Input:
![screenshot](input\building.png)

output:
![screenshot](output\Edge_Hv.jpg)

## exercise 5

Mean filtering is a simple and easy to implement method of smoothing images. It is often used to reduce noise in images. The mean filter is computed using a convolution. The idea of mean filtering is simply to replace each pixel value in an image with the mean (average) value of its neighbors, including itself. Often a 3×3 square kernel is used, although larger kernels (e.g. 5×5 squares) can be used for more severe smoothing.
In this exercise ,we have applied a 3x3 and 5x5 and 15x15 average filter to reduce noise in images

Input:
![screenshot](input\xray_noisy.png)

output:
![screenshot](output\Nr_chest.jpg)

Input:
![screenshot](input\pcb.webp)

output:
![screenshot](output\Nr_pcb.jpg)

Input:
![screenshot](input\image_noisy.png)

output:
![screenshot](output\Nr_circle.jpg)









