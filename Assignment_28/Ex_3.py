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
    # gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # faces = face_detector.detectMultiScale(gray,1.5,5)
    
    # for(x,y,w,h) in faces:
    #     roi_gray = gray[y:y+h,x:x+h]
    #     roi_color=image[y:y+h,x:x+h]
    #     #  cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),3)

        eyes=eye_detector.detectMultiScale(image,1.5,10)
        if len(eyes)==2:
            if eyes[0][0] > eyes[1][0]:
                [eyes[0], eyes[1]] = [eyes[1], eyes[0]]
            x1, y1, w1, h1 = eyes[0]
            x2, y2, w2, h2 = eyes[1]
            w, h = int(max(y1+h1, y2+h2)//2), int((x2+w2-x1)//1.5)
            glassess = cv2.resize(image_glasses, (w, h))
            image_roi=image[y1:h+y1, x1:w+x1]
            for i in range(image_roi.shape[0]):
                 for j in range(image_roi.shape[1]):
                    if glassess[i,j,0]==255 and glassess[i,j,1]==255 and glassess[i,j,2]==255:
                           ...
                    else:
                           image_roi[i,j,0]=glassess[i,j,0]
                           image_roi[i,j,1]=glassess[i,j,1]
                           image_roi[i,j,2]=glassess[i,j,2]
            
            image[y1:h+y1, x1:w+x1]=image_roi[:,:]


        lips=lip_detector.detectMultiScale(image,1.5,10)
        if len(lips)>0:
                lx, ly, lw, lh = lips[0]
                # for lip in lips:
                #     lx2,ly2,lw2,lh2=lip
                #     if lx2>lx+lh:
                #         lx, ly, lw, lh = lip

                lip = cv2.resize(image_lips, (lw, lh))
                image_roi=image[ly:lh+ly, lx:lw+lx]
                for i in range(image_roi.shape[0]):
                    for j in range(image_roi.shape[1]):
                        if lip[i,j,0]==0 and lip[i,j,1]==0 and lip[i,j,2]==0:
                            ...
                        else:
                            image_roi[i,j,0]=lip[i,j,0]
                            image_roi[i,j,1]=lip[i,j,1]
                            image_roi[i,j,2]=lip[i,j,2]
                
                image[ly:lh+ly, lx:lw+lx]=image_roi[:,:]
                # image[fy:fh+fy, fx:fw+fx]=face[:,:]
                


    
        return image
        

cap = cv2.VideoCapture(0)
_, frame = cap.read()
rows, cols, _ = frame.shape
writer = cv2.VideoWriter('Assignment_28\Jila.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 8, (cols, rows))
image_sticker=cv2.imread("Assignment_28\sticker.png")
image_glasses=cv2.imread("Assignment_28\glasses.png")
image_lips=cv2.imread("Assignment_28\lips.png")
# image_lips=cv2.cvtColor(image_lips,cv2.COLOR_BGR2GRAY)

face_detector=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
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

    