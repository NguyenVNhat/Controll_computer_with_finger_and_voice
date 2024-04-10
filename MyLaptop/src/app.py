import eel
import os
import threading
from queue import Queue
import time
import json
import numpy as np

class ChatBot:
    newwebsite = ''
    sendnewwebsite = False
    started = False
    random = 0
    direction = 1

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
    def getnewWebsite(msg):
        ChatBot.userinputQueue.put(msg)
        ChatBot.sendnewwebsite = True
        ChatBot.newwebsite = msg
        print(ChatBot.newwebsite)

    @staticmethod
    def startSetting(msg):
        ChatBot.userinputQueue.put(msg)
        print(msg)
        
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
                                    size=(350, 480),
                                    position=(400,100),
                                    disable_cache=True,
                                    close_callback=ChatBot.close_callback)
            ChatBot.started = True
            while ChatBot.started:
                try:
                    eel.sleep(10.0)
                except:
                    #main thread exited
                    break
        
        except:
            pass

if __name__ == "__main__":
    ChatBot.start()
