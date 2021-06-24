import cv2

w = 1280
h = 960
flip = 2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# 'nvarguscamerasrc = gstreamer
# video/x-raw(memory:NVMM)
# width = 3264 / kameranın full res'i w değişkeni ile display
# height = 2464 / kameranın full res'i h değişkeni ile display
# format = NV12
# framerate =28/1 / 28 FPS olarak ayarlı
# nvvidconv flip-method= str(flip)
# +'! video/x-raw,
# width = +str(w) + 'height = +str(h)' / display h ve w
# format = BGRx !videoconvert ! video/x-raw
# format = BGR ! appsink
cam=cv2.VideoCapture(camSet)
while(True):
    ret, frame =cam.read()
    cv2.imshow('piCam',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()