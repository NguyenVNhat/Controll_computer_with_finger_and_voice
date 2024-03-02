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
import moduleStart
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from screen_brightness_control import set_brightness, get_brightness
import pyautogui
from PIL import Image
import random
import string

def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        moduleStart.speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        moduleStart.speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        moduleStart.speak("Mình chưa hiểu ý của bạn. Bạn nói lại được không?")

# điều khiển âm thanh
def controlVolumn(vol):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface.QueryInterface(IAudioEndpointVolume), POINTER(IAudioEndpointVolume))
    vol_scalar = vol / 100.0
    volume.SetMasterVolumeLevelScalar(vol_scalar, None)

# điều khiển độ sáng màn hình
def controlBrightness(value):
    new_brightness = value
    set_brightness(new_brightness)
    current_brightness = get_brightness()

def generate_random_name(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
# chụp màn hình
def screenShot():
    image = pyautogui.screenshot()

    imageFolder = 'screenShot'
    # Lưu ảnh với tên '1.png' trong thư mục
    imageName = "1"
    imagePath = os.path.join(imageFolder, f'{imageName}.png')

    while os.path.exists(imagePath):
        # Tên ảnh đã tồn tại, tạo tên mới
        imageName = generate_random_name()
        imagePath = os.path.join(imageFolder, f'{imageName}.png')
        
    image.save(imagePath)

    # Mở ảnh
    img = Image.open(imagePath)
    img.show()
