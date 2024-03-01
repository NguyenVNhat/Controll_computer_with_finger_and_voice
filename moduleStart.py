import os
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipediaapi
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtubesearchpython import VideosSearch
import fnmatch
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pygame

# khai báo biến mặc định
language = 'vi'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
wiki_wiki = wikipediaapi.Wikipedia(language, headers={'User-Agent': user_agent})
path = ChromeDriverManager().install()

''' 
    hàm chuyển văn bản thành âm thanh
    gTTS (google Text To Speech)
    chuyển văn bản thành âm thanh và lưu dưới dạng sound.mp3
    sau đó đọc ra 
    đọc xong xóa để đọc văn bản khác
'''
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
'''
    chuyển âm thanh thành văn bản
'''
def get_audio():
    print("Start:")
    r = sr.Recognizer() # nhận diện giọng nói từ nhiều nguồn
    with sr.Microphone() as source: # mở mic 
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5) # thu âm trong 5 giây
        try:
            text = r.recognize_google(audio, language="vi-VN") # chuyển âm thanh thành văn bản
            print(text)
            return text
        except:
            return None
        
'''
    lấy thời gian hiện tại đưa ra cau chào
'''
def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng bạn {} chúc bạn có một ngày tốt lành. Bắt đầu làm việc nào.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}.  Bắt đầu làm việc nào.".format(name))
    else:
        speak("Chào buổi tối bạn {}.  Bắt đầu làm việc nào.".format(name))

