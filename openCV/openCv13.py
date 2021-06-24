import cv2
import numpy as np

w=640
h=480
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
cv2.namedWindow('nanoCam')

while True:
    ret, frame = cam.read() 
    roi = frame[147:208,236:436].copy()
    roiGray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    roiGray = cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)
    frame[147:208,236:436] = roiGray
    cv2.imshow('ROI',roi)
    cv2.imshow('ROIG',roiGray)
    cv2.imshow('nanoCam',frame)  
    pressedKey = cv2.waitKey(1)
    if pressedKey==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()