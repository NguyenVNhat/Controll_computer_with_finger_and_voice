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
lstappuser = ['word','google','powerpoint']
#mở nhiều app trên máy tính
def open_application_multi(text):
    text = text.lower()
    for user_app, actual_app in zip(lstappuser, lstApp):
        if user_app in text:
            text = text.replace(user_app, actual_app)
    
    lst = []
    
    for txt in lstApp:
        if txt in text:
            lst.append(txt)
    print(lst)
    for app in lst:
        open_application(app)
        time.sleep(5)
#mở 1 app
def open_application(text):
    applications_folder = "C:\Program Files" 
    for root, dirs, files in os.walk(applications_folder):
        for file in files:
            if fnmatch.fnmatch(file.lower(), f'*{text.lower()}*'):
                os.startfile(os.path.join(root, file))

#mở website
def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain+'.com'
        webbrowser.open(url)
    
# mở nhạc youtube
def play_song(text):
    mysong = text
    while True:
        result = VideosSearch(mysong, limit=1).result()
        if result['result']:
            break
    video_url = 'https://www.youtube.com/watch?v=' + result['result'][0]['id']
    webbrowser.open(video_url)

def googleSearch(text):
    search_for = text.split("kiếm", 1)[1]
    search_url = f"https://www.google.com/search?q={search_for}"
    webbrowser.open(search_url)

def current_weather(text):
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = text
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        """.format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
        return content

