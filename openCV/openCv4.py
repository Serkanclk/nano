import cv2
dispW=640
dispH=480
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
 
while True:
    ret, frame = cam.read()
    cv2.imshow('nanoCam',frame)  
    cv2.moveWindow('nanoCam',0,0)

    frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret , th1 = cv2.threshold(frame2,0,255,cv2.THRESH_OTSU)
    
    cv2.imshow('gray',th1)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()