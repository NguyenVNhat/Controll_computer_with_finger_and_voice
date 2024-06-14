import math
import pygame
import numpy as np
import pyautogui
import comtypes
import time

def initialize_com():
    comtypes.CoInitialize()

def uninitialize_com():
    comtypes.CoUninitialize()

def control_computer(lmList):
    pygame.init()
    initialize_com()
    try:
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = interface.QueryInterface(IAudioEndpointVolume)
        #volume.GetMute()
        #volume.GetMasterVolumeLevel()
        volRange = volume.GetVolumeRange()
        print(f"Volrange: {volRange}")
        minvol = volRange[0]
        maxvol = volRange[1]

        widthFrame = 1280
        heightFrame = 720
        fingerId = [4, 8, 12, 16, 20]  # Các điểm ngón tay
        if len(lmList) != 0:
            mangngontay = []
            for id in range(1, 5):
                if lmList[fingerId[id]][2] < lmList[fingerId[id] - 1][2]:
                    mangngontay.append(1)
                else:
                    mangngontay.append(0)
            songontay = mangngontay.count(1)

            if int(songontay) == 1:
                print('Di chuyen chuot')
                pointx, pointy = lmList[8][1], lmList[8][2]
                
                # Lấy thông tin về màn hình
                screen_info = pygame.display.Info()
                screen_width = screen_info.current_w - 100
                screen_height = screen_info.current_h - 100
                pX = int((screen_width // widthFrame) * pointx)
                pY = int((screen_height // heightFrame) * pointy)

                try:
                    if 0 <= pX < screen_width and 0 <= pY < screen_height:
                        pyautogui.moveTo(pX, pY)
                except pyautogui.FailSafeException:
                    print("The mouse cursor is out of the screen boundaries.")

            elif int(songontay) == 2:
                x0, y0 = lmList[8][1], lmList[8][2]
                x1, y1 = lmList[4][1], lmList[4][2]
                length = math.hypot(x1 - x0, y1 - y0)
                if length < 20:
                    print('Kich chuot trai')
                    pyautogui.click(button='left')
                    
                x2, y2 = lmList[12][1], lmList[12][2]
                length2 = math.hypot(x1 - x2, y1 - y2)
                if length2 < 20:
                    print('kich chuot phai')
                    pyautogui.click(button='right')
                    

            elif int(songontay) == 3:
                print('thay doi vol')
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]
                length = math.hypot(x2 - x1, y2 - y1)
                vol = np.interp(length, [19, 150], [minvol, maxvol])
                text = int(np.interp(length, [19, 150], [0, 100]))
                
                try:
                    pyautogui.moveTo(50, 150 + vol * 3)  # Simulate moving the volume slider
                    pyautogui.click()  # Simulate clicking on the volume slider
                except pyautogui.FailSafeException:
                    print("The mouse cursor is out of the screen boundaries.")
    
            # cv2.putText(frame,f"{str(text)}",(100,200),3,3,(0,255,0),3)
            elif int(songontay) == 4:
                pyautogui.scroll(-100)
                # Chờ 1 giây
                time.sleep(1)
            elif int(songontay) == 5:
                pyautogui.scroll(100)
                # Chờ 1 giây
                time.sleep(1)
    
    
    
    finally:
        uninitialize_com()
