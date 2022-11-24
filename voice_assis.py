import os
import random
import pyttsx3
import datetime
import wikipedia
import webbrowser as wb
from pycoingecko import *
import speech_recognition as sr
from PIL import Image, ImageDraw, ImageFont

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


os.path.join(
    "C:\\Users\\Yorichi\\Desktop\\jarvis\\musics",
    "C:\\Users\\Yorichi\\Desktop\\jarvis\\videos",
)

user_info = {
    'name': 'Sobhan',
    'family': 'Gojo',
    'age': '13',
}


# speak Func
def speak(audio: str):
    engine.say(audio)
    engine.runAndWait()


# takeCommand function giving audio(voice) command
def take_command() -> str:
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print('Listening ...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:

        print('Recognizing ...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User command => {query.lower()}\n')

    except Exception as e:
        print(e)
        print('Unable to recognize your voice')
        return 'None'

    return query.lower()


def wishMe():

    houre = int(datetime.datetime.now().hour)
    if houre >= 0 and houre <= 12:
        speak(f'Good Morning {user_info["name"]}')
    elif houre <= 12 and houre <= 18:
        speak(f'Good Afternoon {user_info["name"]}')
    else:
        speak(f'Good Evening {user_info["name"]}')

    ass_name = 'Jarvis 1 point o'
    speak(ass_name)


def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


if '__main__' == __name__:

    Clear()
    wishMe()

    while True:
        try:
            query = take_command().lower()

            if 'open google' in query:

                speak('opening google via firefox')
                wb.open_new_tab('https://google.com')

            elif 'open youtube' in query:

                wb.open_new_tab('https://youtube.com')

            elif 'open download anime site' in query:

                wb.open_new_tab('https://aiofilm.com')

            elif 'search' in query:

                query = query.replace('search', "")
                wb.open_new_tab('https://www.google.com/search?client=firefox-b-d&q='+query)

            elif 'vs code' in query:

               os.system('code')

            elif 'play father or son' in query:

                speak('PLaying father or son soon')
                """video_dir = 'H:\\Father'
                parts = os.listdir(music_dir)
                print(parts)
                selected = random.choices(parts)
                print(selected)
                random = os.startfile(os.path.join(music_dir, selected[0]))"""
            elif 'play music' in query:

                query = query.replace('play music', "").replace(" ", "")
                music_dir = 'C:\\Users\\Yorichi\\Desktop\\jarvis\\musics'
                musics = os.listdir(music_dir)

                print(query)
                print(musics)

                if query + '.mp3' in musics:

                    speak('playing')
                    os.startfile(os.path.join(music_dir, f'{query}.mp3'))
                else:

                    speak(f'cannot find {query} song')

            elif 'play random music' in query:
                musics_dir = 'C:\\Users\\Yorichi\\Desktop\\jarvis\\musics'
                musics_list = os.listdir(musics_dir)
                selected_music = random.choice(musics_list)
                print(selected_music)
                speak(f'{selected_music}')
                speak('playing music')
                os.startfile(os.path.join(musics_dir, selected_music))

            elif 'get price of' in query:

                query = query.replace("get price of", "").replace(" ", "")
                api = CoinGeckoAPI()
                price = api.get_price(ids=query, vs_currencies='usd')
                price = price[query]['usd']
                price = float(price)
                speak(str(price) + 'dollar')
                print(price)
            elif 'wikipedia find' in query:

                query = query.replace("wikipedia find", "").replace(" ", "")
                img = Image.new(mode='RGB', size=(1000, 760), color=(255, 255, 255))
                drawed = ImageDraw.Draw(img)
                font = ImageFont.truetype('C:\\Users\\Yorichi\\Desktop\\jarvis\\micross.ttf', 15)
                
                try:
                    search_res = wikipedia.summary(query, sentences=2)
                    drawed.text((50, 50), f"""\n{search_res[0:50]}{search_res[49:100]}\n{search_res[99:150]}
                            {search_res[149:-1]}""", fill=(0, 0, 0), font=font)
                    img.show()
                    speak(search_res)
                except Exception as e:
                    drawed.text((50, 50), f"{e}", fill=(0, 0, 0), font=font)
                    img.show()
                    print(e)
                    speak(str(e))
                    continue
                    
            elif 'goodbye' in query:
                speak('goodbye')
                exit()
        except KeyboardInterrupt as key_error:
            speak('Good bye')
            exit()
        except Exception as e:
            print(e)
            with open('logs.txt', 'w') as log_file:
                log_file.write(f'error at {datetime.datetime.now()} => {str(e)}')
                log_file.close()
            speak('I have some error')
            continue
