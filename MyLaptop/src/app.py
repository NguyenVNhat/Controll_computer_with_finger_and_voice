import eel
import os
import threading
from queue import Queue
import time
import json
import numpy as np
from NPL import main as process 
import pandas
from Ai_respone import respond as chatbotRes
from Main import send_message_to_client
import queue


class ChatBot:
    newwebsite = ''
    started = False
    random = 0
    client_socket = None
    direction = 1
    queue = queue.Queue()  

    userinputQueue = Queue()

    @staticmethod
    def isUserInput():
        return not ChatBot.userinputQueue.empty()

    @staticmethod
    def popUserInput():
        return ChatBot.userinputQueue.get()

    @staticmethod
    def close_callback(route, websockets):
        exit()

    @staticmethod
    def close():
        ChatBot.started = False
    

    @staticmethod
    @eel.expose
    def getTextApp(msg):
        ChatBot.userinputQueue.put(msg)
        ans = process.mainFunction(msg)
        if ans: 
            ChatBot.setAppInput()
        else:
            anws = str(chatbotRes.getAiresponedAll(msg))
            eel.setAppInput(anws)

    @staticmethod
    @eel.expose
    def signalVoice(msg):
        ChatBot.userinputQueue.put(msg)
        send_message_to_client(ChatBot.client_socket,msg)
        
    @staticmethod
    def setAppInput():
        with open('Resource/dict_respone.json', encoding='utf-8') as file:
            data = json.load(file)
        random = ChatBot.random
        if ChatBot.random == len(data):
            ChatBot.direction = -1
        if ChatBot.random == 0:
            ChatBot.direction = 1
        eel.setAppInput(data['apprespone'][random])
        ChatBot.random += ChatBot.direction

    @staticmethod
    def setAppInputMSG(msg):
        eel.setAppInput(msg)

    # @staticmethod
    # @eel.expose
    # def setAppFrame():
    #     try:
    #         eel.setFrame()
    #     except:
    #         print('lord')

    @staticmethod
    def setUserInput(msg):
        eel.setUserInput(msg)
    @staticmethod
    def start():
        path = os.path.dirname(os.path.abspath(__file__))
        eel.init(path + r'\web', allowed_extensions=['.js', '.html'])
        try:
            eel.start('index.html', mode='chrome',
                      host='localhost',
                      port=27005,
                      block=False,
                      size=(400, 600),
                      position=(10,100),
                      disable_cache=True,
                      close_callback=ChatBot.close_callback)
            ChatBot.started = True
            ChatBot.setAppInputMSG("Hello")
            ChatBot.setAppInputMSG("Have a good day !")
            
            while ChatBot.started:
                try:
                    
                    eel.sleep(10.0)
                except:
                    break
        
        except:
            pass

if __name__ == "__main__":
    ChatBot.start()
    
