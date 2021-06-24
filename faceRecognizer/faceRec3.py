import face_recognition
import cv2
image = face_recognition.load_image_file('/home/nvidia-nano/Desktop/pyCD/faceRecognizer/demoImages/known/Bradd Pitt.jpg')
image_encode = face_recognition.face_encodings(image)[0]

image1 = face_recognition.load_image_file('/home/nvidia-nano/Desktop/pyCD/faceRecognizer/demoImages/known/Leonardo.jpg')
image1_encode = face_recognition.face_encodings(image1)[0]

Encodings = [image_encode,image1_encode]
Names = ['Bradd','Leonardo']

font = cv2.FONT_HERSHEY_SIMPLEX
testImage = face_recognition.load_image_file('/home/nvidia-nano/Desktop/pyCD/faceRecognizer/demoImages/unknown/u16.jpg')

face_locations = face_recognition.face_locations(testImage)
allEncodings = face_recognition.face_encodings(testImage,face_locations)

testImage =cv2.cvtColor(testImage,cv2.COLOR_RGB2BGR)
for (row1,col1,row2,col2),face_encoding in zip(face_locations,allEncodings):
    name = 'Unknown Person'
    matches = face_recognition.compare_faces(Encodings,face_encoding)
    if True in matches:
        first_match_index = matches.index(True)
        name = Names[first_match_index]
    cv2.rectangle(testImage,(col1,row1),(col2,row2),(0,255,0),2)
    cv2.putText(testImage,name,(col2,row1-6),font,.75,(0,255,255),2)
cv2.imshow('window',testImage)
if(cv2.waitKey(0)==ord('q')):
    cv2.destroyAllWindows()