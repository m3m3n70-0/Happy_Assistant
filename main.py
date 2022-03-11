# ██╗░░██╗░█████╗░██████╗░██████╗░██╗░░░██╗
# ██║░░██║██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝
# ███████║███████║██████╔╝██████╔╝░╚████╔╝░
# ██╔══██║██╔══██║██╔═══╝░██╔═══╝░░░╚██╔╝░░
# ██║░░██║██║░░██║██║░░░░░██║░░░░░░░░██║░░░
# ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░

from lib.modules.download_mp3 import *
from lib.modules.calculator import *

from youtubesearchpython import VideosSearch
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import qrcode

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

qr_code_commands = ["one", "two", "three"]


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            talk("Yes?")
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

        elif "download" in command:
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

        elif "time" in command:
            timea = datetime.datetime.now().strftime('%H:%M')
            timeb = datetime.datetime.now().strftime('%I:%M:%p')
            talk("the current time is " + timea + " that is " + timeb)

        elif "wikipedia" in command or "who is" in command or "what is" in command:
            search = command.split("wikipedia" and "who is" and "what is", 1)[1]
            print(search)
            wiki_results = wikipedia.search(search)
            result = wiki_results[0]
            page = wikipedia.summary(result, 3, auto_suggest=False)
            talk(page)

        elif "qr code for" in command or "qr codes for" in command:
            qr_link = command.split("for", 1)[1]
            video_search = VideosSearch(qr_link, limit=1)
            input_data = "https://www.youtube.com/watch?v=" + video_search.result()['result'][0]['id']
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(input_data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            talk("downloading qr code from " + qr_link)
            img.save('docs/youtube-qr.png')
            return talk("download complete")

        elif "search" in command:
            search = command.split("search", 1)[1]
            search_result = search
            pywhatkit.search(search_result)
            talk("searching " + search)

        elif "calculate" in command:
            tekst = command
            number1 = [int(word) for word in tekst.split() if word.isdigit()][0]
            number2 = [int(word) for word in tekst.split() if word.isdigit()][1]

            if "add" in command or "+" in command:
                print("that is " + add(number1, number2))
                talk("that is " + add(number1, number2))

            elif "subtract" in command or "-" in command:
                print("that is " + subtract(number1, number2))
                talk("that is " + subtract(number1, number2))

            elif "multiply" in command or "*" in command:
                print("that is " + multiply(number1, number2))
                talk("that is " + multiply(number1, number2))

            elif "divide" in command or "/" in command:
                print("that is " + divide(number1, number2))
                talk("that is " + divide(number1, number2))

        # elif "how are you?" in command:

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
