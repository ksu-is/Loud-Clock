
import datetime
import time
from os import system


while True:
	s = "# The real time clock!\n\nEver wanted to know what the time is? Well, your journey is about to end!\n\n**The time is "
	t = datetime.datetime.now().strftime('%b %d, %Y, %H:%M') + "**"
	with open("readme.md", "w") as f:
		f.write(s + t)
		
	system("git add .")
	system("git commit -m \"Update time\"")
	system("git push origin master")
	time.sleep(59)
if __name__ == '__main__':
    import os
    from gtts import gTTS
    Text = ("The time is")

    print("please wait...processing")
    TTS = gTTS(text=Text, lang='en')

    # Save to mp3 in current dir.
    TTS.save("voice.mp3")

    # Plays the mp3 using the default app on your system
    # that is linked to mp3s.
    os.system("start voice.mp3")
    tick()
    root.mainloop()

 


