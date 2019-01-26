#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
from gtts import gTTS
from pygame import mixer
import time
import os


print("What would you like me to say?")
values = input()
i = 0
mixer.init()


# Get the text and convert to mp3 file
tts = gTTS(text=values, lang='en',slow=False)
tts.save('speech{}.mp3'.format(i%2))
# playback the speech
mixer.music.load('speech{}.mp3'.format(i%2))
mixer.music.play()
# wait for playback to end
while mixer.music.get_busy():
    time.sleep(.1)
mixer.stop()
i += 1

# try to remove the temp files. You'll likely be left with 1 to clean up
try:
    os.remove('speech0.mp3')
except:
    pass
try:
    os.remove('speech1.mp3')
except:
    pass

