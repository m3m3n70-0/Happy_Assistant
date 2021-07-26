# ██╗░░██╗░█████╗░██████╗░██████╗░██╗░░░██╗
# ██║░░██║██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝
# ███████║███████║██████╔╝██████╔╝░╚████╔╝░
# ██╔══██║██╔══██║██╔═══╝░██╔═══╝░░░╚██╔╝░░
# ██║░░██║██║░░██║██║░░░░░██║░░░░░░░░██║░░░
# ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░

import speech_recognition as sr
import pyttsx3
import pywhatkit
from youtubesearchpython import VideosSearch
import vlc
import pafy
import youtube_dl
import os

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


def download_video(url):
    video = url.strip()
    ydl = youtube_dl.YoutubeDL()
    try:
        ydl_opts = {
            'outtmpl': "test.mp3",
            # 'outtmpl': unicode(customName),
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video])
    except:
        print("Invalid URL!")


def check_download():
    if os.path.exists("test.mp3"):
        os.remove("test.mp3")
        print("removed copy")


def run_happy():
    check_download()
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        video_search = VideosSearch(song, limit=1)
        url = "https://www.youtube.com/watch?v=" + video_search.result()['result'][0]['id']
        download_video(url)
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
        print(url)
        # pywhatkit.playonyt(song, use_api=True)


run_happy()
