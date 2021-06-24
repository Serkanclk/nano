from threading import Thread
import cv2
import time
import numpy as np
w = int(640)
h = int(480)
flip = 2

class vStream:
    def __init__(self,src,width,height):
        self.width = width
        self.height = height
        self.capture = cv2.VideoCapture(src)
        self.thread = Thread(target=self.update,args=())
        self.thread.daemon=True
        self.thread.start()
    def update(self):
        while True:
            ret, self.frame = self.capture.read()
            self.frame_resized = cv2.resize(self.frame,(self.width,self.height))
    def getFrame(self):
        return self.frame_resized

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
       
cam1 = vStream(1,w,h) # webCam
cam2 = vStream(camSet,w,h) # piCam
while True:
    try:
        myFrame1 = cam1.getFrame() # webCamFrame
        myFrame2 = cam2.getFrame() # piCamFrame
        myFrame3 = np.hstack((myFrame1,myFrame2))
        cv2.imshow('sync',myFrame3)
        # cv2.imshow('webCam',myFrame1)
        # cv2.imshow('piCam',myFrame2)
    except:
        print('frame not readed')
    if cv2.waitKey(1)==ord('q'):
        cam1.capture.release()
        cam2.capture.release()
        cv2.destroyAllWindows()
        exit(1)
        break
