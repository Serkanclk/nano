import cv2
import numpy as np
evt = -1
coordList=[]
img = np.zeros((200,200,3),np.uint8)
def click(event,x,y,flags,params):
    global point
    global evt
    if (event==cv2.EVENT_LBUTTONDOWN):       
        print('Left Click Coord:',x,',',y)
        point=(x,y)
        coordList.append(point)
        evt = event
    if (event==cv2.EVENT_RBUTTONDOWN):
        #Tıklanan pikselin b,g,r değerleri okunuyor.
        b = frame[y,x,0]
        g = frame[y,x,1]
        r = frame[y,x,2]
        print(b,g,r)
        #Oluşturulacak pencerede gözükecek BGR değerleri.
        colorStr = str(b)+','+str(g)+','+str(r)
        #Oluşturulan npArray a elimizdeki b,g,r değeri aktarılıyor.
        img[:]=[b,g,r]
        cv2.imshow('selectedColor',img)

w=640
h=480
flip=2
cv2.namedWindow('nanoCam')
cv2.setMouseCallback('nanoCam',click)
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
while True:
    ret, frame = cam.read() 
    for i in coordList:
        cv2.circle(frame,i,5,(0,0,255),-1)     
    cv2.imshow('nanoCam',frame)  
    pressedKey = cv2.waitKey(1)
    if pressedKey==ord('q'):
        break
    if(pressedKey==ord('w')):
        coordList=[]
cam.release()
cv2.destroyAllWindows()