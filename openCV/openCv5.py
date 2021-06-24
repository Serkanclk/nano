import cv2
dispW=640
dispH=480
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
 
while True:
    ret, frame = cam.read()
    cv2.imshow('nanoCam',frame)  
    
    frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frameSmall = cv2.resize(frame,(320,240))
    frame2Small = cv2.resize(frame2,(320,240))
    
    cv2.imshow('frame2Small',frame2Small)
    cv2.imshow('frameSmall',frameSmall)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()