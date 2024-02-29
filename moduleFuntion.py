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

def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        moduleStart.speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        moduleStart.speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        moduleStart.speak("Mình chưa hiểu ý của bạn. Bạn nói lại được không?")


def controlVolumn():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    volrange = volume.GetVolumeRange()
    minVol = volrange[0]
    maxVol = volrange[1]
    vol = 30
    volume.SetMasterVolumeLevel(vol, None)
