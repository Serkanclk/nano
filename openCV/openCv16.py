import cv2
import numpy as np
w=640
h=480
flip=2

img1=np.zeros((480,640,1),np.uint8)
img1[0:480,0:320] = [255]
img2=np.zeros((480,640,1),np.uint8)
img2[190:290,270:370] = [255]
bitAnd=cv2.bitwise_and(img1,img2)
bitOr=cv2.bitwise_or(img1,img2)
bitXor=cv2.bitwise_xor(img1,img2)
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
images = [img1,img2,bitAnd,bitOr,bitXor]
imNames = ['img1','img2','1and2','1or2','1xor2']
while True:
    ret, frame = cam.read()
    for i in range(len(images)):
        frameSmall = cv2.resize(images[i],(320,240))
        cv2.imshow(imNames[i],frameSmall)
    frame = cv2.bitwise_and(frame,frame,mask=img2)
    cv2.imshow('nanoCam',frame)  
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()