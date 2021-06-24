import cv2
import numpy as np
w=320
h=240
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

while True:
    ret, frame = cam.read()
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    b=cv2.split(frame)[0] # Blue channel split edildi.
    g=cv2.split(frame)[1] # Green channel
    r=cv2.split(frame)[2] # Red channel
    cv2.imshow('blue',b) # Ayırılan kanalların görüntüleri.
    cv2.imshow('green',g)
    cv2.imshow('red',r)
    cv2.imshow('nanoCam',frame)  
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()