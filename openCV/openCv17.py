import cv2
import numpy as np
w=320
h=240
flip=2
cvLogo=cv2.imread('cv.jpg')
cvLogo=cv2.resize(cvLogo,(320,240))
cvLogoGray= cv2.cvtColor(cvLogo,cv2.COLOR_BGR2GRAY)
cv2.imshow('cvLogoGray',cvLogoGray)
ret, BGMask = cv2.threshold(cvLogoGray,50,255,cv2.THRESH_BINARY)
cv2.imshow('BGmask',BGMask)

FGMask = cv2.bitwise_not(BGMask)
cv2.imshow('FGMask',FGMask)

FG = cv2.bitwise_and(cvLogo,cvLogo,mask=FGMask)
cv2.imshow('FG',FG)
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

while True:
    ret, frame = cam.read()
    BG = cv2.bitwise_and(frame,frame,mask=BGMask)
    cv2.imshow('BG',BG)

    compImage = cv2.add(BG,FG)
    cv2.imshow('compImage',compImage)
    
    cv2.imshow('nanoCam',frame)  
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()