import os
from gtts import gTTS

Text = "this is a test"

print("please wait...processing")
TTS = gTTS(text=Text, lang='en')

# Save to mp3 in current dir.
TTS.save("voice.mp3")

# Plays the mp3 using the default app on your system
# that is linked to mp3s.
os.system("start voice.mp3")