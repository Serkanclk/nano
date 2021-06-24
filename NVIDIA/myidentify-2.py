import jetson.inference
import jetson.utils
import cv2
import numpy as np
import time

width = 640
height = 480
#cam = jetson.utils.gstCamera(480,640,'/dev/video1')
cam = jetson.utils.gstCamera(width,height,'0')
display = jetson.utils.glDisplay()
font = jetson.utils.cudaFont()
net = jetson.inference.imageNet('googlenet')
timeMark = time.time()
fpsFilter = 0

while display.IsOpen():
    frame, width, height, = cam.CaptureRGBA(zeroCopy=1)
    classID, confidence = net.Classify(frame,width,height)
    item = net.GetClassDesc(classID)
    # FPS hesaplama
    dt = time.time()-timeMark
    fps = 1/dt
    fpsFilter = .95*fps+.05*fps
    timeMark = time.time()
    font.OverlayText(frame,width,height,str(round(fpsFilter,1))+' fps '+item,5,5,font.Magenta,font.Blue)
    display.RenderOnce(frame,width,height)
    

