import jetson.inference
import jetson.utils
import cv2
import numpy as np
import time

width = 640
height = 480
cam = jetson.utils.gstCamera(480,640,'/dev/video1')
#cam = jetson.utils.gstCamera(width,height,'0')
#display = jetson.utils.glDisplay()
#font = jetson.utils.cudaFont()
net = jetson.inference.imageNet('googlenet')
timeMark = time.time()
fpsFilter = 0
font = cv2.FONT_HERSHEY_SIMPLEX
# while display.IsOpen():
while True:
    frame, width, height, = cam.CaptureRGBA(zeroCopy=1)
    classID, confidence = net.Classify(frame,width,height)
    item = net.GetClassDesc(classID)
    # FPS hesaplama
    dt = time.time()-timeMark
    fps = 1/dt
    fpsFilter = .95*fps+.05*fps
    timeMark = time.time()
    #font.OverlayText(frame,width,height,str(round(fpsFilter,1))+' fps '+item,5,5,font.Magenta,font.Blue)
    #display.RenderOnce(frame,width,height)
    frame = jetson.utils.cudaToNumpy(frame,width,height,4)#RGBA
    frame = cv2.cvtColor(frame,cv2.COLOR_RGBA2BGR).astype(np.uint8) #format = float32 -> uint8
    cv2.putText(frame,str(round(fpsFilter,1))+' fps '+item,(0,30),font,.60,(0,0,255),2)
    cv2.imshow('recCam',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
