import vlc
import pafy
import youtube_dl
import os

# Download the video and stores it.
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
        print("This URL does not work.")

# Checks the download
def check_download():
    if os.path.exists("test.mp3"):
        os.remove("test.mp3")
        print("removed copy")

