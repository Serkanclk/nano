import jetson.inference
import jetson.utils
w=1280
h=720
flip=2
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
net = jetson.inference.imageNet('googlenet')
#cam = jetson.utils.gstCamera(480,640,'/dev/video1')
cam = jetson.utils.gstCamera(w,h,'0')
disp = jetson.utils.glDisplay()
font = jetson.utils.cudaFont()

while disp.IsOpen():
    frame, width, height = cam.CaptureRGBA()
    classID, confident = net.Classify(frame, width, height)
    item = net.GetClassDesc(classID)
    font.OverlayText(frame, width, height, item, 5,5, font.Magenta, font.Blue)
    disp.RenderOnce(frame, width, height)