from flask import Flask, Response
import cv2
import speech_recognition as sr
import threading
import socket
import time

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print('Nhận âm thanh :')
        audio = r.listen(source, phrase_time_limit=5) 
        print('Hoàn tất :')
        try:
            text = r.recognize_google(audio, language="vi-VN") 
            print(text)
            return text
        except:
            return None 

app = Flask(__name__)
camera = cv2.VideoCapture(0)
running = True  

def gen_frames():
    while running:  
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
stop_flag = False
stop_flag_lock = threading.Lock()

def receiveMessage(client_socket):
    global stop_flag
    global stop_flag_lock
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                continue
            if b'True' in data:
                with stop_flag_lock:
                    stop_flag = True
            elif b'False' in data:
                print("Ngừng gửi tin nhắn.")
                with stop_flag_lock:
                    stop_flag = False
            else:
                continue
        except socket.error as e:
            print('Gặp lỗi khi nhận dữ liệu:', e)
            print('Đang thử lại...')
            time.sleep(1)

def sendMessage(client_socket):
    global stop_flag
    global stop_flag_lock
    try:
        while True:
            with stop_flag_lock:
                if stop_flag:
                    client_socket.send("Listenning...".encode())
                    request = get_audio()
                    while request ==  None:
                        request = get_audio()
                    request = request.lower()
                    client_socket.send("Finish".encode())
                    client_socket.send(request.encode())
            time.sleep(1) 
    except socket.error as e:
        print('Gặp lỗi khi gửi dữ liệu:', e)
        print('Đang thử lại...')
        time.sleep(1)



@app.route('/')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    client_socket.connect((host, port))
    print('Đã kết nối tới server')

    video_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5000, 'debug': False})
    receive_thread = threading.Thread(target=receiveMessage, args=(client_socket,))
    
    send_thread = threading.Thread(target=sendMessage, args=(client_socket,))
    send_thread.start()

    video_thread.start()
    receive_thread.start()

    try:
        while running:
            pass
    except KeyboardInterrupt:
        running = False
        print("Exiting...")
