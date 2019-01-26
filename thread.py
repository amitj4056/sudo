import _thread
import time
import speech_recognition as sr
import zulip
import sys
from gtts import gTTS
from pygame import mixer
import os

# Define a function for the thread
def send_message( threadName, delay):
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Say something")
      r.adjust_for_ambient_noise(source)
      audio = r.listen(source,timeout=5)
      print("Time over")



   cont = r.recognize_google(audio, language='hi-IN')
   print("TEXT: " + cont)


   # Pass the path to your zuliprc file here.
   client = zulip.Client(config_file="./zuliprc")

   # Send a stream message
   request = {
       "type": "private",
       "to": "nlp-bot@unixloversaurabh.zulipchat.com",
       "subject": "Castle",
       "content": cont
   }
   result = client.send_message(request)
   print(result)


def print_timeThread2( threadName, delay):
   # Pass the path to your zuliprc file here.
   client = zulip.Client(config_file="./zuliprc")
   # Get the 3 last messages sent by "iago@zulip.com" to the stream "Verona"
   request = {
       'use_first_unread_anchor': True,
       'num_before': 1,
       'num_after': 0,
       'narrow': [{'operator': 'sender', 'operand': 'nlp-bot@unixloversaurabh.zulipchat.com'},
                  {'operator': 'is', 'operand': 'private'}],
       'client_gravatar': True,
       'apply_markdown': True
   }  # type: Dict[str, Any]
   result = client.get_messages(request)
   print(result)


   mixer.init()
   # Get the text and convert to mp3 file
   tts = gTTS(text="saurabh is good boy", lang='en',slow=False)
   tts.save('speech{}.mp3'.format(0))
   # playback the speech
   mixer.music.load('speech{}.mp3'.format(0))
   mixer.music.play()
   # wait for playback to end
   while mixer.music.get_busy():
       time.sleep(.1)
   mixer.stop()

   # try to remove the temp files. You'll likely be left with 1 to clean up
   try:
       os.remove('speech0.mp3')
   except:
       pass




# Create two threads as follows
try:
   #_thread.start_new_thread( send_message, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_timeThread2, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
