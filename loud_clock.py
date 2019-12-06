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
    if len(faces) == 1:
         
        import pygame
        import datetime
#pulling time
        time = datetime.datetime.now().time()
        timeStrOld = str(time)
        timeStrNew = timeStrOld[0:3]+timeStrOld[3:6]+timeStrOld[6:8]
        print(timeStrNew)

        

        
        if __name__ == '__main__':

            import os
            from gtts import gTTS
    
            Text = ("The time is" + timeStrNew)

 
            TTS = gTTS(text=Text, lang='en')
    

    
    # Save to mp3
            TTS.save("voice.mp3")

    # Plays the mp3 
  
            os.system("start voice.mp3") 
    #gui
            import PySimpleGUI as sg
            

            layout = [ [sg.Text(timeStrNew)] ]

            window = sg.Window('Time').Layout(layout)
            window.Read()
            
            window.Close()
            import time
            time.sleep(5)
    continue    
    
    
