# ██╗░░██╗░█████╗░██████╗░██████╗░██╗░░░██╗
# ██║░░██║██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝
# ███████║███████║██████╔╝██████╔╝░╚████╔╝░
# ██╔══██║██╔══██║██╔═══╝░██╔═══╝░░░╚██╔╝░░
# ██║░░██║██║░░██║██║░░░░░██║░░░░░░░░██║░░░
# ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░

from download_mp3 import *

from youtubesearchpython import VideosSearch
import speech_recognition as sr
import pyttsx3
import pywhatkit

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

    except:
        pass
    return command


def run_happy():
    command = take_command()
    print(command)
    if "happy" in command:
        command = command.replace("happy", "")

        if "play" in command:
            song = command.split("play", 1)[1]
            print(song)
            talk("playing " + song)
            pywhatkit.playonyt(song, use_api=True)

        if "download" in command:
            song = command.split("download", 1)[1]
            talk("downloading " + song)
            video_search = VideosSearch(song, limit=1)
            url = "https://www.youtube.com/watch?v=" + video_search.result()['result'][0]['id']
            download_video(url)
            video = pafy.new(url)
            best = video.getbest()
            media = vlc.MediaPlayer(best.url)
            media.play()
            print(url)

    else:
        print("you need to use the wake word 'happy'")
        talk("you need to use the wake word happy")
        run_happy()


# def confirm_done():
#     talk("can i help with anything else")
#     print("Can I help with anything else?")
#     command = take_command()
#     if "yes" in command:
#         run_happy()


run_happy()

# "Play" lets you play a song on youtube
# "Download" lets you download a song



