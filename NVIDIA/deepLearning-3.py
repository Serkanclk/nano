import jetson.inference
import jetson.utils
import time
import cv2
timeStamp = time.time()
fpsFilter = 0

net = jetson.inference.detectNet('ssd-mobilenet-v2',threshold=.5)
dispW = 1280
dispH = 720
#cam = jetson.utils.gstCamera(dispW,dispH,'0')
cam = jetson.utils.gstCamera(720,1280,'/dev/video1')
display = jetson.utils.glDisplay()
while display.IsOpen():
    img, width, height = cam.CaptureRGBA()
    detections = net.Detect(img,width,height)
    display.RenderOnce(img,width,height)
    dt = time.time() - timeStamp
    timeStamp = time.time()
    fps = 1/dt
    fpsFilter = .9*fps+.1*fps
    print(str(round(fpsFilter,1))+' fps')