import MainModule as Bot
import re
import pyautogui
import time

listApp = ['google','chrome','word','winword','powerpoint','excel']
listFunction = ['giờ','ngày','tháng','năm']
listFunction2 = ['âm lượng','volumne']


Bot.speak("Bắt đầu chương trình")
while True :
    print('--')
    request = input("Nhập từ khóa : ")
    request = request.lower()
    if request is not None:
        if 'mấy giờ ' in request or 'ngày mấy ' in request  :
            Bot.get_time(request)
        elif 'âm lượng' in request:
            vol = request.split('lượng',1)
            Bot.controlVolumn(int(vol[1]))
        elif 'độ sáng' in request:
            val = request.split('sáng',1)
            Bot.controlBrightness(int(val[1]))
        elif 'mở ứng dụng' in request:
            app = request.split('dụng',1)
            Bot.open_application_multi(app[1])
        elif 'mở web' in request:
            web = request.split('web',1)
            Bot.open_website(web[1])
        elif 'mở bài hát' in request:
            song = request.split('hát',1)
            Bot.playSong_youtube(song[1])
        elif 'tìm kiếm trên google' in request:
            search = request.split('google',1)
            Bot.googleSearch(search[1])
        elif 'chụp màn hình' in request:
            Bot.screenShot()
        else :
            print("Sao dị")
    else :
        print('Error')



    
