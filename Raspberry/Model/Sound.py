import os
import speech_recognition as sr
from time import strftime
from gtts import gTTS
import pygame
language = 'vi'

def speak(text):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit() 
    os.remove("sound.mp3")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        audio = r.listen(source, phrase_time_limit=5) 
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text
        except:
            return None
def hello():
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng , chúc bạn có một ngày tốt lành. Tôi là CHIBI")
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều . Tôi là CHIBI.  Bắt đầu làm việc nào.")
    else:
        speak("Chào buổi tối bạn . Tôi là CHIBI.  Bắt đầu làm việc nào.")