import jetson.inference
import jetson.utils
import time
import cv2
import numpy as np
timeStamp = time.time()
fpsFilter = 0

net = jetson.inference.imageNet('alexnet',['--model=/home/jnano/Downloads/jetson-inference/python/training/classification/myModel/resnet18.onnx','--labels=/home/jnano/Downloads/jetson-inference/myTrain/labels.txt','--input_blob=input_0','--output_blob=output_0'])

#imagenet-camera --model=/home/jnano/Downloads/jetson-inference/python/training/classification/myModel/resnet18.onnx --labels=/home/jnano/Downloads/jetson-inference/myTrain/labels.txt --camera=/dev/video1 --width=480 --height=640 --input_blob=input_0 --output_blob=output_0
dispW = 640
dispH = 480
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
    _, frame = cam.read()
    # img, width, height = cam.CaptureRGBA() # NVIDIA
    # NVIDA DETECT
    height=frame.shape[0]
    width=frame.shape[1]
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA).astype(np.float32)
    img = jetson.utils.cudaFromNumpy(img)
    classID, confidence = net.Classify(img,width,height)
    item = ''
    item = net.GetClassDesc(classID)
    
    # display.RenderOnce(img,width,height) # NVIDIA
    dt = time.time() - timeStamp
    timeStamp = time.time()
    fps = 1/dt
    fpsFilter = .9*fps+.1*fps
    # print(str(round(fpsFilter,1))+' fps') # NVIDIA
    cv2.putText(frame,str(round(fpsFilter,1))+' fps '+item,(0,30),font,.60,(0,0,255),2)
    cv2.imshow('detCam',frame)
    if (cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
