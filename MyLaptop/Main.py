import sys
sys.path.insert(0,'Models')
sys.path.insert(1,'src')
import Internet,App,Basic,CMD,ComputerFunction,GenerateNewDataWebsite
import app
import socket
import threading


def getAudio():
    return Basic.get_audio()

requestCMD = ['mở cài đặt','mở cài đặt âm thanh','mở cài đặt display''mở cài đặt autoplay','mở cài đặt usb','mở cài đặt pen and windows ink',
              'mở cài đặt touchpad','mở cài đặt mobile-devices','mở cài đặt mouse','mở cài đặt printers','mở cài đặt bluetooth','mở file explorer',
              'mở task manager','mở máy tính','mở control panel','mở quản lí ảnh','mở camera','mở lịch','mở quản lí đồng hồ','mở bản đồ','mở outlook']

allApp = ['']
def mainFunction(keyvalue):
    request = keyvalue
    if request is not None:
        request = request.lower()
        print(request)
        if 'mấy giờ' in request or 'ngày mấy' in request  :
            ComputerFunction.get_time(request)
        elif 'âm lượng' in request:
            vol = request.split('lượng',1)
            ComputerFunction.controlVolumn(int(vol[1]))
        elif 'thời tiết' in request:
            Internet.current_weather(request.split('tiết ')[1])
        elif 'độ sáng' in request:
            val = request.split('sáng',1)
            ComputerFunction.controlBrightness(int(val[1]))
        elif 'mở ứng dụng' in request:
            app = request.split('dụng',1)
            App.search_on_start_menu(app[1])
        elif 'mở web' in request:
            request = request.replace(" ","")
            web = request.split('web',1)
            Internet.open_website(web[1])
        elif 'mở youtube và tìm kiếm' in request:
            song = request.split('kiếm',1)
            Internet.play_Video(song[1])
        elif 'mở zingmp3 và tìm kiếm' in request:
            song = request.split('kiếm',1)
            Internet.play_song_mp3(song[1])
        elif 'mở google và tìm kiếm' in request:
            search = request.split('kiếm',1)
            Internet.googleSearch(search[1])
        elif 'chụp màn hình' in request:
            ComputerFunction.screenShot()
        elif 'chuyển trang' in request:
            ComputerFunction.Return_Window()
        elif 'thư mục' in request:
            CD = request[0]
            folder = request.split('mục')[1]
            ComputerFunction.find_and_open_folder(CD,folder)
        elif 'gửi email' in request:
            title = input('Nhập tiêu đề :')
            content = input('Nhập nội dung :')
            email_receive = input('Nhập email nhận :')
            Internet.send_email(title,content,email_receive)
        for item in requestCMD:
            if item in request:
                CMD.OpenSetting(item)

    else :
        print('Error')
def start_chatbot():
    app.ChatBot.start()

def receive_message_from_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            print(data)
            request = data.split('Message')[0]
            message = data.split('Message')[1]
            if "Error" in data:
                app.ChatBot.setUserInput(message)
                app.ChatBot.setAppInputMSG("Tôi không hiểu ý bạn")
            else :
                app.ChatBot.setUserInput(message)
                mainFunction(request)
                app.ChatBot.setAppInput()
                
        except ConnectionResetError:
            print("Client đã ngắt kết nối.")
            break
# ADDWEBSITE|||google driver|||https://drive.google.com/
def send_message_to_client(client_socket):
    while True:
        try:
            status = app.ChatBot.sendnewwebsite
            if status == True:
                message = app.ChatBot.newwebsite
                website = message.split("|||")[1]
                url = message.split("|||")[2]
                GenerateNewDataWebsite.addNewWebsiteURL(website,url)
                client_socket.send(message.encode())
                app.ChatBot.sendnewwebsite = False
        except ConnectionResetError:
            print("Client đã ngắt kết nối.")
            break


startChat = threading.Thread(target=start_chatbot)
startChat.start()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

print("Server đang mở ...")

client_socket, address = server_socket.accept()
print(f"Kết nối từ {address} được thành lập.")


receive_thread = threading.Thread(target=receive_message_from_client, args=(client_socket,))
receive_thread.start()

send_thread = threading.Thread(target=send_message_to_client, args=(client_socket,))
send_thread.start()

receive_thread.join()
send_thread.join()

client_socket.close()
server_socket.close()

