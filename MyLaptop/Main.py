import sys
sys.path.insert(0,'Models')
sys.path.insert(0,'NPL')
sys.path.insert(1,'src')
sys.path.insert(2,'src')
from NPL import main as process
import Internet,App,Basic,CMD,ComputerFunction
import app
import control_computer_hand
import socket
import json
import threading
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import cv2
import os
from Fingers import hand as htm
from Ai_respone import respond as chatbotRes
import requests
import mouse
import pygame
import pyautogui
import math
import time

def check_url(url):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False
def process_video_and_control_hand():
    try:
        url = 'http://192.168.128.201:4747/video'
        cap = cv2.VideoCapture(2) 
        detector=htm.handDetector(detectionCon=1)
        widthFrame = 1280
        heightFrame = 720
        fingerId= [4,8,12,16,20]
        pyautogui.FAILSAFE = False
        while True:
            ret,frame=cap.read()
            frame=detector.findHands(frame)
            heighFrame1,widthFrame1,_=frame.shape
            lmList= detector.findPosition(frame,draw=False)
            if not ret:
                print("Error reading frame")
                break

            if len(lmList)!=0:
                mangngontay=[]
                if lmList[fingerId[0]][1] <lmList[fingerId[0]-1][1] :
                    mangngontay.append(1)
                else: mangngontay.append(0)    
                
                for id in range(1,5):
                    if  lmList[fingerId[id]][2] <lmList[fingerId[id]-1][2] :  
                        mangngontay.append(1)
                    else:
                        mangngontay.append(0)      
                songontay=mangngontay.count(1)
                if int(songontay) == 1:
                    pointx, pointy = lmList[8][1], lmList[8][2]
                    pygame.init()
                    screen_info = pygame.display.Info()
                    screen_width = screen_info.current_w 
                    screen_height = screen_info.current_h 
                    pX = int((screen_width // widthFrame1) * pointx)
                    pY = int((screen_height // heighFrame1) * pointy)

                    try:
                        if 0 <= pX < screen_width and 0 <= pY < screen_height:
                            pyautogui.moveTo(pX, pY)
                    except pyautogui.FailSafeException:
                        print("The mouse cursor is out of the screen boundaries.")
            
                elif int(songontay)==2:
                    x0,y0 = lmList[8][1],lmList[8][2]
                    x1,y1 = lmList[4][1],lmList[4][2]
                    x2,y2 = lmList[12][1],lmList[12][2]
                    length = math.hypot(x1-x0,y1-y0)
                    length2= math.hypot(x1-x2,y1-y2)
                    if length<20:
                        mouse.click('left')
                    if length2<20 :
                        pyautogui.click(button='right')
                elif int(songontay) == 4:
                    pyautogui.scroll(-300)
                elif int(songontay) == 5:
                    pyautogui.scroll(300)            
            cv2.imshow('Frame', frame)  
            if cv2.waitKey(1) & 0xFF == ord('q'):  
                    break
                
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print("Error:", e)

def start_chatbot():
    app.ChatBot.start()


def send_message_to_client(client_socket, message):
    try:
        client_socket.send(message.encode()) 
        print(message)
    except Exception as e:
        print("Lỗi khi gửi tin nhắn cho client:", e)
        time.sleep(5)

def handle_server(client_socket):
    while True:
        print("Bắt đầu xử lý")
        data = client_socket.recv(1024).decode()
        if data:
            print(data)
            if data == 'Listenning...' or data == 'Finish' or data == 'Tôi chưa nhận được yêu cầu từ bạn':
                app.ChatBot.setAppInputMSG(data)
            else :
                app.ChatBot.setUserInput(data)
                ans = process.mainFunction(data)
                if ans : 
                    app.ChatBot.setAppInput()
                else :
                    anws = str(chatbotRes.getAiresponedAll(data))
                    app.ChatBot.setAppInputMSG(anws)
        else:
            print("Dữ liệu nhận được từ client không hợp lệ.")
            time.sleep(5)


def start_socket_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.128.161'
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server đang lắng nghe tại {}:{}".format(host, port))

    while True:
        try:
            chatbot_thread = threading.Thread(target=start_chatbot)
            chatbot_thread.start()
            client_socket, client_address = server_socket.accept()
            app.ChatBot.client_socket = client_socket
            print("Kết nối từ:", client_address)
            camera_thread = threading.Thread(target=process_video_and_control_hand)
            camera_thread.start()
            handle_server(client_socket)
        
        except:
            print('Out')
            start_socket_server()  
if __name__ == "__main__":

    socket_server_thread = threading.Thread(target=start_socket_server)
    socket_server_thread.start()

