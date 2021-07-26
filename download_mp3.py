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


def download_video(url):
    video = url.strip()
    ydl = youtube_dl.YoutubeDL()
    try:
        ydl_opts = {
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

