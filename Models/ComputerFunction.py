import os
import time
import datetime
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from screen_brightness_control import set_brightness, get_brightness
import pyautogui
from PIL import Image
import random
import string
import subprocess
import pygetwindow as gw
import Basic

def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        Basic.speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        Basic.speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        Basic.speak("Mình chưa hiểu ý của bạn. Bạn nói lại được không?")

# điều khiển âm thanh
def controlVolumn(vol):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface.QueryInterface(IAudioEndpointVolume), POINTER(IAudioEndpointVolume))
    vol_scalar = vol / 100.0
    volume.SetMasterVolumeLevelScalar(vol_scalar, None)

# điều khiển độ sáng màn hình
def controlBrightness(value):
    new_brightness = value
    set_brightness(new_brightness)
    current_brightness = get_brightness()

def generate_random_name(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
# chụp màn hình
def screenShot():
    image = pyautogui.screenshot()
    imageFolder = 'screenShot'
    imageName = "1"
    imagePath = os.path.join(imageFolder, f'{imageName}.png')

    while os.path.exists(imagePath):
        imageName = generate_random_name()
        imagePath = os.path.join(imageFolder, f'{imageName}.png')

    image.save(imagePath)
    img = Image.open(imagePath)
    img.show()

def hide_task_manager():
    try:
        subprocess.run(["taskkill", "/fi", "imagename eq chrome.exe"])
        print("Đã ẩn Task Manager thành công.")
    except Exception as e:
        print(f"Không thể ẩn Task Manager. Lỗi: {e}")


def Return_Window():
    try:
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1) 
        pyautogui.press('enter')
    except Exception as e:
        print(f" Lỗi: {e}")

def switch_window(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)

        if window:
            window[0].activate()
        else:
            print(f"Không tìm thấy cửa sổ có tiêu đề: {window_title}")

    except Exception as e:
        print(f"Không thể chuyển đến cửa sổ: {window_title}. Lỗi: {e}")
