import cv2
w=640
h=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
Rect_W = int(.2*640)
Rect_H =int(.2*480)
x1 , y1 = 140,100
mult_X =4
mult_Y =4
while True:
    ret, frame = cam.read()
    # 480-640  
    roi = frame[y1:y1+Rect_H,x1:x1+Rect_W].copy()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    frame[y1:y1+Rect_H,x1:x1+Rect_W] = roi

    frame = cv2.rectangle(frame,(x1,y1),(x1+Rect_W,y1+Rect_H),(255,0,0),1)  
    x1 = x1+mult_X
    y1 = y1+mult_Y
    if(x1==0 or x1+Rect_W==w):
        mult_X = mult_X * (-1)
    if(y1==0 or y1+Rect_H==h):
        mult_Y = mult_Y * (-1)

    cv2.imshow('nanoCam',frame)  
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()