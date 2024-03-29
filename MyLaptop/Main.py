import sys
sys.path.insert(0,'Models')
sys.path.insert(1,'src')
import Internet,App,Basic,CMD,ComputerFunction
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
        elif 'độ sáng' in request:
            val = request.split('sáng',1)
            ComputerFunction.controlBrightness(int(val[1]))
        elif 'mở ứng dụng' in request:
            app = request.split('dụng',1)
            App.open_application_multi(app[1])
        elif 'mở web' in request:
            request = request.replace(" ","")
            web = request.split('web',1)
            Internet.open_website(web[1])
        elif 'mở youtube và tìm kiếm' in request:
            song = request.split('kiếm',1)
            Internet.play_Video(song[1])
        elif 'mở zingmp3 tìm kiếm' in request:
            song = request.split('kiếm',1)
            Internet.play_song_mp3(song[1])
        elif 'tìm kiếm trên google' in request:
            search = request.split('google',1)
            Internet.googleSearch(search[1])
        elif 'chụp màn hình' in request:
            ComputerFunction.screenShot()
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

# Hàm chạy socket server trong một luồng
def start_socket_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server đang lắng nghe tại {}:{}".format(host, port))

    while True:
        client_socket, client_address = server_socket.accept()
        print("Kết nối từ:", client_address)
        
        data = client_socket.recv(1024).decode()
        mainFunction(data)
        app.ChatBot.setUserInput(data)
        print(data)
        message = "Tin nhắn của bạn đã được nhận!"
        client_socket.send(message.encode())
        client_socket.close()

# Khởi chạy 2 luồng
if __name__ == "__main__":
    chatbot_thread = threading.Thread(target=start_chatbot)
    chatbot_thread.start()

    socket_server_thread = threading.Thread(target=start_socket_server)
    socket_server_thread.start()

