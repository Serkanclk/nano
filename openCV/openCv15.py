import cv2
goFlag=0
cv2.namedWindow('nanoCam')
def mouse_click(event,x,y,flags,params):
    global x1,y1,x2,y2
    global goFlag
    if (event==cv2.EVENT_LBUTTONDOWN):
        x1=x
        y1=y
        goFlag=0
    if (event==cv2.EVENT_LBUTTONUP):
        x2=x
        y2=y
        goFlag=1
cv2.setMouseCallback('nanoCam',mouse_click)
w=640
h=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

while True:
    ret, frame = cam.read()   
    if(goFlag==1):
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        roi=frame[y1:y2,x1:x2]
        cv2.imshow('ROI',roi)
    cv2.imshow('nanoCam',frame)  
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()