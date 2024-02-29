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

lstApp = ['winword','chrome','powerpnt']
lstAppUser = ['word','google','powerpoint']
def open_application_multi(text):
    for user_app, actual_app in zip(lstAppUser, lstApp):
        if user_app in text:
            text = text.replace(user_app, actual_app)
    lst = []
    for txt in lstApp:
        if txt in text:
            lst.append(txt)
    for app in lst:
        open_application(app)
        time.sleep(5)

def open_application(text):
    applications_folder = "C:\Program Files" 
    for root, dirs, files in os.walk(applications_folder):
        for file in files:
            if fnmatch.fnmatch(file.lower(), f'*{text.lower()}*'):
                os.startfile(os.path.join(root, file))
                return
    print(f"Không tìm thấy ứng dụng có từ khóa '{text}'.")