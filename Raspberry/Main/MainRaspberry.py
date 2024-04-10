import sys
sys.path.insert(0,'Model')
import re
import json
import threading
import socket
import GenerateNewDataWebsite
import speech_recognition as sr
def get_audio():
    print('start : ')
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        audio = r.listen(source, phrase_time_limit=5) 
        try:
            text = r.recognize_google(audio, language="vi-VN") 
            print(text)
            print('finish')
            return text
        except:
            return None   
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


def receive_message_from_server(client_socket):
    while True:
        try:
            response = client_socket.recv(1024).decode()
            print(response)
            website = response.split("|||")[1]
            url = response.split("|||")[2]
            GenerateNewDataWebsite.addNewWebsiteRequest(website)
        except ConnectionResetError:
            print("Server đã đóng kết nối.")
            break

def send_message_to_server(client_socket):
    while True:
        request = input("nhập :")
        request = request.lower()
        message = AnalysisSound(request)
        message = message +" Message "+request
        client_socket.send(message.encode())
        if message.lower() == 'exit':
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

receive_thread = threading.Thread(target=receive_message_from_server, args=(client_socket,))
receive_thread.start()

send_thread = threading.Thread(target=send_message_to_server, args=(client_socket,))
send_thread.start()

receive_thread.join()
send_thread.join()

client_socket.close()


