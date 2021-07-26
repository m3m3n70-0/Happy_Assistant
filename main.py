# ██╗░░██╗░█████╗░██████╗░██████╗░██╗░░░██╗
# ██║░░██║██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝
# ███████║███████║██████╔╝██████╔╝░╚████╔╝░
# ██╔══██║██╔══██║██╔═══╝░██╔═══╝░░░╚██╔╝░░
# ██║░░██║██║░░██║██║░░░░░██║░░░░░░░░██║░░░
# ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░

import speech_recognition as sr
import pyttsx3
import pywhatkit
from download_mp3 import *

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "happy" in command:
                command = command.replace("happy", "")
    except:
        pass
    return command


def run_happy():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song, use_api=True)

    if "download" in command:
        song = command.replace("download", "")
        talk("downloading " + song)
        video_search = VideosSearch(song, limit=1)
        url = "https://www.youtube.com/watch?v=" + video_search.result()['result'][0]['id']
        download_video(url)
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
        print(url)


run_happy()

# "Play" lets you play a song on youtube
# "Download" lets you download a song



