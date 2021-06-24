import cv2
w=640
h=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

x1 , y1, x2, y2 = 140,100,180,140
situ=True
while True:
    ret, frame = cam.read()
    # 480-640
    if(situ):
        x2-=2
        x1-=2
        
        
        if(y1==0 or x1==0):
            situ = False      
    if(not situ):
        x2+=2
        x1+=2
        
        
        if(x2==640 or y2==480):
            situ=True
    frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),-1)  
    cv2.imshow('nanoCam',frame)  
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()