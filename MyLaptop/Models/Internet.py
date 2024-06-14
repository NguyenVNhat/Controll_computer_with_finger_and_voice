import datetime
import re
import webbrowser
import requests
from youtubesearchpython import VideosSearch
from comtypes import CLSCTX_ALL
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import Basic
def open_website(url):
        webbrowser.open(url)

# lấy thông tin từ trang dự báo thời tiết
def current_weather(text):
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    text = text.title()
    text = text.strip()
    city = text
    print(text)
        
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
        """.format(day=now.day, month=now.month, year=now.year, hourrise=sunrise.hour, minrise=sunrise.minute,
                   hourset=sunset.hour, minset=sunset.minute,
                   temp=current_temperature, pressure=current_pressure, humidity=current_humidity)
        print(content)
        Basic.speak(content)
    
def send_email(title,text, email_receive):
    email_send = 'nhataaghjkl@gmail.com'
    password = 'llur licc ffkl zaix'
    email_to = email_receive
    message = MIMEMultipart()
    message['From'] = email_send
    message['To'] = email_to
    message['Subject'] = title
    content = MIMEText(text, 'plain', 'utf-8')
    message.attach(content)
    with smtplib.SMTP('smtp.gmail.com', 587) as session:
        session.starttls()
        session.login(email_send, password)
        session.sendmail(email_send, email_to, message.as_string())

