import pyaudio,os
import speech_recognition as sr


def excel():
        os.system("start excel.exe")

def internet():
        os.system("start chrome.exe")

def media():
        os.system("start wmplayer.exe")

def mainfunction(source):
    audio = r.listen(source)
    user = r.recognize(audio)
    print(user)
    if user == "Excel":
        print("Excel")
    elif user == "Internet":
        print(internet)
    elif user == "music":
        print(media)

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainfunction(source)
