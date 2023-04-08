import cv2
import numpy as np

def chess_board(image):
        results = face_detector.detectMultiScale(image,1.3)
        for face in results:
            x,y,w,h=face
            face_image=image[y:y+h,x:x+w]
            face_image_small=cv2.resize(face_image,[10,10])
            face_image_big=cv2.resize(face_image_small,[w, h],interpolation=cv2.INTER_NEAREST)
            image[y:y+h , x:x+w] = face_image_big
        return image
    
def sticker_func(image):
        results = face_detector.detectMultiScale(image,1.3)
        for face in results:
            x,y,w,h=face
            #draw a rectangle around the face
            # cv2.rectangle(frame,[x,y],[x+w,y+h],0,5)
            sticker=cv2.resize(image_sticker,[w, h])
            image[y:y+h,x:x+w ] = sticker
        return image

def mirror(image):
        rows = image.shape[1]
        mirror = cv2.flip(image[:,rows//2:rows], 1)
        image[:,:rows//2] = mirror
        return image

def eye_lips(image):
        eyes = eye_detector.detectMultiScale(image,1.3)
        lips=lip_detector.detectMultiScale(image,1.3)
        for lip in lips:
            x,y,w,h = lip
            Lips = cv2.resize(image_lips,[w,h])
            break
        for i in range((Lips.shape[0])):
             for j in range((Lips.shape[1])):
                if Lips[i,j]>0:
                    image[x+i, y+j] = Lips[i,j]
        # if len(eyes)>1:
        #      eye1=eyes[0]
        #      eye2=eyes[1]
        
        # Eyes = cv2.resize(image,[eye1[2]+eye2[2],eye1[3]+eye2[3]])
        # image[eye1[1]:eye1[1]+eye1[3], eye1[0]:eye1[0]+eye1[2]] = Eyes

        # x2=image.shape[1]
        # y2=image.shape[1]
        # w2=image.shape[1]
        # h2=image.shape[1]
        # x1=0
        # y1=0
        # w1=0
        # h1=0
        # for eye in eyes:
        #     x1,y1,w1,h1=eye
        #     if x1>x2:
        #          x1=x2
        #     if y1>y2:
        #          y1=y2
        #     if w1>w2:
        #          w1=w2
        #     if h1>h2:
        #          h1=h2


        #     #draw a rectangle around the face
        # cv2.rectangle(image,[x,y],[x+w,y+h],0,5)
        # # glasses=cv2.resize(image_glasses,[w1, h2])
        # # cv2.imshow("",glasses)

        # image[y1:y1+h1,x1:x1+w2 ] = glasses
            
        # for face in eyes:
        #     x,y,w,h = face
        #     glasses = cv2.resize(image_glasses,[w,h])
        #     image[y:y+h, x:x+w] = glasses
        return image
     

cap = cv2.VideoCapture(0)
_, frame = cap.read()
rows, cols, _ = frame.shape
writer = cv2.VideoWriter('Assignment_28\Jila.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 8, (cols, rows))
image_sticker=cv2.imread("Assignment_28\sticker.png")
image_glasses=cv2.imread("Assignment_28\glasses.png")
image_lips=cv2.imread("Assignment_28\lips.png")
image_lips=cv2.cvtColor(image_lips,cv2.COLOR_BGR2GRAY)

face_detector=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
lip_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
choice=0
while True:
    _, frame = cap.read()

    if choice==1:
        frame=sticker_func(frame)

    elif choice==2:
        frame=eye_lips(frame)
    elif choice==3:
         frame =  chess_board(frame)

    elif choice==4:
        frame = mirror(frame)

    writer.write(frame)
    cv2.imshow('result',frame)
    if cv2.waitKey(5) & 0XFF == ord('q'):
        break
    elif cv2.waitKey(5) & 0XFF==ord('1'):
       choice=1
    elif cv2.waitKey(5) & 0XFF==ord('2'):
       choice=2
    elif cv2.waitKey(5) & 0XFF==ord('3'):
       choice=3
    elif cv2.waitKey(5) & 0XFF==ord('4'):
       choice=4


writer.release()
cap.release()

    