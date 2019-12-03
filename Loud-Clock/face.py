import cv2
import sys
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)
while True:
    retval, frame = video.capture.read
    gray = cv2.cvtColor(frame, cv2,COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(35, 35)
    
    )
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 200), 2)
cv2.imshow('Video', frame)
if cv2.waitkey(1)& 0xff == ord('q'):
    sys.exit
