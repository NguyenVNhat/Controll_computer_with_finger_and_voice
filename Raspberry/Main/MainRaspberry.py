import sys
import re
import json
import socket
def AnalysisSound(request):
    # mở website
    with open('Resource/requestWebsite.json', encoding='utf-8') as file:
        data = json.load(file)

    for website, phrases in data.items():
            for p in phrases[0]:
                if p in request and phrases[1][0] in request:
                    if len(phrases[2]) != 0:
                        HasCancel = False
                        Cancel = ''
                        for cancel in phrases[2]:
                            if cancel in request:
                                HasCancel = True
                                Cancel = cancel
                        if HasCancel :
                            return 'mở '+website+" và tìm kiếm" + request.split(Cancel)[1]
                        else :
                            return 'mở web '+website 
                    else :
                        return 'mở web '+website 
                    
    # mở cài đặt 
    with open('Resource/requestCMD.json', encoding='utf-8') as file:
        dataSetting = json.load(file)
    for app, phrases in dataSetting.items():
            for p in phrases[0]:
                if p in request and phrases[1][0] in request:
                    return app
    # ứng dụng và chức năng trên máy 
    with open('Resource/requestFunction.json', encoding='utf-8') as file:
        dataFunction= json.load(file)
    for function, phrases in dataFunction.items():
            if len(phrases[1]) != 0 :
                for p in phrases[0]:
                    if p in request :
                        for idx in phrases[1]:
                            if idx in request:
                                numbers = re.findall(r'\d+', request)
                                number =  [int(num) for num in numbers]
                                return f"{function} {number}".replace("[", "").replace("]", "")
            else :
                for p in phrases[0]:
                    if p in request :
                        return function
    with open('Resource/requestFolder.json', encoding='utf-8') as file:
        dataFunction= json.load(file)
    for function, phrases in dataFunction.items():
            if len(phrases[1]) != 0 :
                for p in phrases[0]:
                    if p in request :
                        for idx in phrases[1]:
                            if idx in request:
                                folder_name = request.split('mục')[1]
                                if 'ổ c' in request:
                                    cd = 'C'
                                if 'ổ d' in request:
                                    cd = 'D'   
                                if 'ổ e' in request:
                                    cd = 'E'
                                return cd+" thư mục"+folder_name
    with open('Resource/requestweather.json', encoding='utf-8') as file:
        dataFunction= json.load(file)
    for function, phrases in dataFunction.items():
            if len(phrases[1]) != 0 :
                for p in phrases[0]:
                    if p in request :
                        for idx in phrases[1]:
                            if idx.lower() in request:
                                return "thời tiết "+idx
    with open('Resource/requestApp.json', encoding='utf-8') as file:
            dataSetting = json.load(file)
    for app, phrases in dataSetting.items():
                for p in phrases[0]:
                    if p in request:
                        return p + request.split(p)[1]

    return "Error"
                    
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))
while True:
    request = input('Nhập message: ')
    request = request.lower()
    message = AnalysisSound(request) +" Message "+request
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print("Tin nhắn từ server:", data)
client_socket.close()


