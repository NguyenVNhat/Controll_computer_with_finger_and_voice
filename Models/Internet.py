import datetime
import re
import webbrowser
import requests
from youtubesearchpython import VideosSearch
from comtypes import CLSCTX_ALL


#mở website
def open_website(text):
    reg_ex = re.search('mở web (.+)', text)
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

# tìm kiếm trên google
def googleSearch(text):
    search_url = f"https://www.google.com/search?q={text}"
    webbrowser.open(search_url)

# lấy thông tin từ trang dự báo thời tiết
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

