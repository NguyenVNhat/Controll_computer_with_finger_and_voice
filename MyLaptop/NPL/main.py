import npl
import sys
sys.path.insert(0,'Models')
sys.path.insert(1,'src')
sys.path.insert(2,'src')
import Internet,App,Basic,CMD,ComputerFunction
import socket
import json
import threading

controlVolumn = ['âm-lượng','âm-thanh','loa']
controlLight = ['độ-sáng','ánh-sáng']
screenShort = ['màn-hình']
oldScreen = ['trang-cũ']
time= ['thời-gian','ngày-mấy','ngày-bao-nhiêu','mấy-giờ']
weather = ['thời-tiết']
delapp = ['tắt-ứng-dụng']

def mainFunction(n):
    try:
        ans,string = npl.transformer(n)
        if ans['LoaiDongTu2'] == 2.0:
            keyFind = string.split(ans['DongTu2'])[1]
            App.open_folder(keyFind)
            return True
        elif ans['LoaiChuThe'] == 'cmd':
            CMD.OpenSetting(ans['Url'])
            return True
        elif ans['LoaiChuThe'] == 'web':
            if ans['DongTu2'] =='':
                Internet.open_website(ans['Url'])
            else:
                keyFind = string.split(ans['DongTu2'])[1]
                if ans['LoaiDongTu2'] == 1.0:
                    urlFind = ans['UrlFind']+keyFind
                    Internet.open_website(urlFind)
            return True
        elif ans['LoaiChuThe'] == 'app':
            nameapp = string.split(ans['ChuThe'])[1]
            App.OpenApp(nameapp)
            return True
        elif ans['LoaiChuThe'] == 'cpt':
            if ans['ChuThe'] in controlVolumn:
                if (ans['Value'] == ''):
                    ans['Value'] = '100'
                ComputerFunction.controlVolumn(int(ans['Value']))
            if ans['ChuThe'] in controlLight:
                if (ans['Value'] == ''):
                    ans['Value'] = '100'
                ComputerFunction.controlBrightness(int(ans['Value']))
            if ans['ChuThe'] in screenShort:
                ComputerFunction.screenShot()
            if ans['ChuThe'] in oldScreen:
                ComputerFunction.Return_Window()
            if ans['ChuThe'] in time:
                ComputerFunction.get_time()
            if ans['ChuThe'] in weather:
                Internet.current_weather(string.split(ans['ChuThe'])[1])     
            if ans['ChuThe'] in delapp:
                ComputerFunction.alt_f4()
            return True
    except:
        return False