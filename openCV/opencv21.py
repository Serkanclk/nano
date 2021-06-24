import cv2
import numpy as np
def nothing(x):
    pass
cv2.namedWindow('Trackbars')
cv2.createTrackbar('hueLower','Trackbars',50,180,nothing)
cv2.createTrackbar('hueHigher','Trackbars',100,180,nothing)
cv2.createTrackbar('hue2Lower','Trackbars',50,180,nothing)
cv2.createTrackbar('hue2Higher','Trackbars',100,180,nothing)
cv2.createTrackbar('satLower','Trackbars',100,255,nothing)
cv2.createTrackbar('satHigher','Trackbars',255,255,nothing)
cv2.createTrackbar('valLower','Trackbars',100,255,nothing)
cv2.createTrackbar('valHigher','Trackbars',255,255,nothing)

w=320
h=240
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam= cv2.VideoCapture(camSet)
cam= cv2.VideoCapture(1)
while True:
    ret, frame = cam.read()
    
   

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    hueLow = cv2.getTrackbarPos('hueLower','Trackbars')
    hueHigh = cv2.getTrackbarPos('hueHigher','Trackbars')
    hue2Low = cv2.getTrackbarPos('hue2Lower','Trackbars')
    hue2High = cv2.getTrackbarPos('hue2Higher','Trackbars')
    satLow = cv2.getTrackbarPos('satLower','Trackbars')
    satHigh = cv2.getTrackbarPos('satHigher','Trackbars')
    valLow = cv2.getTrackbarPos('valLower','Trackbars')
    valHigh = cv2.getTrackbarPos('valHigher','Trackbars')

    lower_bound = np.array([hueLow,satLow,valLow])
    upper_bound = np.array([hueHigh,satHigh,valHigh])

    lower_bound2 = np.array([hue2Low,satLow,valLow])
    upper_bound2 = np.array([hue2High,satHigh,valHigh])

    FGMask =cv2.inRange(hsv,lower_bound,upper_bound)
    FGMask2 =cv2.inRange(hsv,lower_bound2,upper_bound2)
    FGMaskMerge = cv2.add(FGMask,FGMask2)
    cv2.imshow('FGmask',FGMaskMerge)
    contours,hierarchy=cv2.findContours(FGMaskMerge,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        (x,y,w,h) = cv2.boundingRect(cnt)
        if area >=50:
            #cv2.drawContours(frame,[cnt],0,(0,255,0),2)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)  
    cv2.drawContours(frame,contours,0,(255,0,0),3)
    cv2.imshow('nanoCam',frame)  

    
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()