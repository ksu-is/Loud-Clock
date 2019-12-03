
import cv2
import sys

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)

while True:

    # Capture frame-by-frame
    retval, frame = video_capture.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect features specified in Haar Cascade
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(35, 35)
    )

    # Draw a rectangle around recognized faces 
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 200), 2)
        minutes = 50
        hours = 7
        seconds = 30
        import time
        while True:
            print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
            seconds = seconds + 1
            time.sleep(1)
            if seconds == 60:
                seconds = 1
            minutes = minutes + 1
            if minutes == 60:
                hours = hours + 1
                minutes = 1
            if hours == 13:
                hours = 1

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Exit the camera view
    if cv2.waitKey(1) & 0xFF == ord('q'):
        sys.exit()