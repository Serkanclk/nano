import face_recognition
import cv2
import os
import pickle
import time
Encodings = []
Names = []

w=320
h=240
flip=2
fpsReport =0
scaleFactor =.30
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

with open('train.pkl','rb') as f:
    Names = pickle.load(f)
    Encodings = pickle.load(f)


font = cv2.FONT_HERSHEY_SIMPLEX

timeStamp = time.time()
while True:
    ret,frame = cam.read()
    frameSmall=cv2.resize(frame,(0,0),fx=scaleFactor,fy=scaleFactor)
    frameRGB = cv2.cvtColor(frameSmall,cv2.COLOR_BGR2RGB)
    facePositions = face_recognition.face_locations(frameRGB,model='cnn')
    allEncodings=face_recognition.face_encodings(frameRGB,facePositions)
    for(top,right,bottom,left),face_encoding in zip(facePositions,allEncodings):
        name = 'Unknown'
        matches =face_recognition.compare_faces(Encodings,face_encoding)
        if True in matches:
            first_match_index = matches.index(True)
            name =Names[first_match_index]
        top=int(top/scaleFactor)
        right=int(right/scaleFactor)
        bottom=int(bottom/scaleFactor)
        left=int(left/scaleFactor)
        cv2.rectangle(frame,(left,top),(bottom,right),(0,255,0),2)
        cv2.putText(frame,name,(left,top-6),font,.75,(0,255,255),2)
    dt = time.time()-timeStamp
    fps = 1/dt
    fps =round(fps,1)
    fpsReport = .90*fpsReport + .1*fps
    fpsReport =round(fpsReport,1)
    #print("fps:",fps)
    timeStamp = time.time()
    cv2.rectangle(frame,(0,0),(75,30),(0,0,0),-1)
    cv2.putText(frame,str(fpsReport)+"fps",(0,25),font,.60,(255,255,255),2)
    cv2.imshow('Video',frame)
    if(cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()