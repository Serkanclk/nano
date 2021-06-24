import cv2
w=640
h=480
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
while True:
    ret, frame = cam.read()
    frame = cv2.rectangle(frame,(350,80),(140,140),(255,0,0),4)
    frame = cv2.circle(frame,(320,200),50,(0,0,255),2)
    frame= cv2.line(frame,(0,0),(255,255),(0,255,0),3)
    cv2.imshow('nanoCam',frame)  
    
    
    
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()

cv2.destroyAllWindows()