import cv2
import numpy as np

w=640
h=480
flip=2
def nothing(x):
    pass
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
cv2.namedWindow('nanoCam')
cv2.createTrackbar('xVal','nanoCam',0,w,nothing)
cv2.createTrackbar('yVal','nanoCam',0,h,nothing)
cv2.createTrackbar('rectH','nanoCam',25,h,nothing)
cv2.createTrackbar('rectW','nanoCam',25,w,nothing)
while True:
    ret, frame = cam.read() 
    
    xVal = cv2.getTrackbarPos('xVal','nanoCam')
    yVal = cv2.getTrackbarPos('yVal','nanoCam')
    rectH = cv2.getTrackbarPos('rectH','nanoCam')
    rectW = cv2.getTrackbarPos('rectW','nanoCam')
    frame = cv2.rectangle(frame,(xVal,yVal),(xVal+rectW,yVal+rectH),(255,0,0),3)
    cv2.imshow('nanoCam',frame)  
    pressedKey = cv2.waitKey(1)
    if pressedKey==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()