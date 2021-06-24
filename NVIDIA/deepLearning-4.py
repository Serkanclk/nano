import jetson.inference
import jetson.utils
import time
import cv2
import numpy as np
timeStamp = time.time()
fpsFilter = 0

net = jetson.inference.detectNet('ssd-mobilenet-v2',threshold=.5)
dispW = 1280
dispH = 720
flip = 2
font = cv2.FONT_HERSHEY_SIMPLEX
# camSet='nvarguscamerasrc wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.1 saturation=1.2 ! appsink drop=true'
# cam= cv2.VideoCapture(camSet)
#cam = jetson.utils.gstCamera(dispW,dispH,'0')
#cam = jetson.utils.gstCamera(720,1280,'/dev/video1')
#display = jetson.utils.glDisplay()
cam = cv2.VideoCapture('/dev/video1')
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
# while display.IsOpen():
while True:
    _, img = cam.read()
    # img, width, height = cam.CaptureRGBA() # NVIDIA
    height=img.shape[0]
    width=img.shape[1]
    # NVIDA DETECT
    frame = cv2.cvtColor(img,cv2.COLOR_BGR2RGBA).astype(np.float32)
    frame = jetson.utils.cudaFromNumpy(frame)
    detections = net.Detect(frame,width,height)
    for detect in detections:
        ID = detect.ClassID
        item = net.GetClassDesc(ID)
        print(item)
    # display.RenderOnce(img,width,height) # NVIDIA
    dt = time.time() - timeStamp
    timeStamp = time.time()
    fps = 1/dt
    fpsFilter = .9*fps+.1*fps
    # print(str(round(fpsFilter,1))+' fps') # NVIDIA
    cv2.putText(img,str(round(fpsFilter,1))+' fps',(0,30),font,.60,(0,0,255),2)
    cv2.imshow('detCam',img)
    if (cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
