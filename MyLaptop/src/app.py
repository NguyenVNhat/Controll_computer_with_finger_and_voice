import eel
import os
import threading
from queue import Queue
import time

class ChatBot:
    started = False
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
    @eel.expose
    def getUserInput(msg):
        ChatBot.userinputQueue.put(msg)
        print(msg)
    
    @staticmethod
    def close():
        ChatBot.started = False

    @staticmethod
    def setUserInput(msg):
        eel.setUserInput(msg)

    @staticmethod
    def getMessageFromClient(user_input):
            with lock:  
                ChatBot.setUserInputPython(user_input)

    @staticmethod
    def setUserInputPython(msg):
        ChatBot.userinputQueue.put(msg)
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
                      position=(10,100),
                      disable_cache=True,
                      close_callback=ChatBot.close_callback)
            ChatBot.started = True

            while ChatBot.started:
                try:
                    eel.sleep(10.0)
                except:
                    break
        except:
            pass

if __name__ == "__main__":
    ChatBot.start()
