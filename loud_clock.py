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
    
  

 


