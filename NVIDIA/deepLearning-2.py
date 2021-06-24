import jetson.inference
import jetson.utils
import cv2
import numpy as np
import time

width = 1280
height = 720
dispW = width
dispH = height
flip=2
cam = jetson.utils.gstCamera(480,640,'/dev/video1')
# camSet='nvarguscamerasrc wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.1 saturation=1.2 ! appsink drop=true'
# cam= cv2.VideoCapture(camSet)
#cam = jetson.utils.gstCamera(width,height,'0')
net = jetson.inference.imageNet('googlenet')
timeMark = time.time()
fpsFilter = 0
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    _,frame = cam.read()
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA).astype(np.float32) # format = uint8 ->float32
    img = jetson.utils.cudaFromNumpy(img)
    classID, confidence = net.Classify(img,width,height)
    item =''
    item = net.GetClassDesc(classID)
    # FPS hesaplama
    dt = time.time()-timeMark
    fps = 1/dt
    fpsFilter = .95*fps+.05*fps
    timeMark = time.time()
    cv2.putText(frame,str(round(fpsFilter,1))+' fps '+item,(0,30),font,.60,(0,0,255),2)
    cv2.imshow('recCam',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
