import sys
sys.path.insert(0,'Model')

import json
import socket
def AnalysisSound():
    request = input('Nhập message: ')
    request = request.lower()
    # mở website
    with open('Resource/requestWebsite.json', encoding='utf-8') as file:
        data = json.load(file)

    for website, phrases in data.items():
        if website in request:
            for p in phrases[0]:
                if p in request and phrases[1][0]:
                    if len(phrases[2]) != 0:
                        HasCancel = False
                        Cancel = ''
                        for cancel in phrases[2]:
                            if cancel in request:
                                print(cancel)
                                HasCancel = True
                                Cancel = cancel
                        if HasCancel :
                            return 'mở '+website+" và tìm kiếm" + request.split(Cancel)[1]
                        else :
                            return 'mở web '+website
                    
    # mở cài đặt 
    with open('Resource/requestCMD.json', encoding='utf-8') as file:
        dataSetting = json.load(file)
    for app, phrases in dataSetting.items():
        for p in phrases[0]:
            if p in request and phrases[1][0] in request:
                return app
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))
message = AnalysisSound()
client_socket.send(message.encode())
data = client_socket.recv(1024).decode()
print("Tin nhắn từ server:", data)
client_socket.close()
            

