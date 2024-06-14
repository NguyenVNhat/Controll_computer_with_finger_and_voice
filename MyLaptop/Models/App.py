import os
import time
import fnmatch
from comtypes import CLSCTX_ALL
import subprocess
import logging
logging.basicConfig(level=logging.WARNING)
import pyautogui
import time
import re

def OpenApp(query):
    pyautogui.press('win')
    time.sleep(1) 
    pyautogui.write(query)
    time.sleep(1)
    pyautogui.press('enter')

def find_directories(root_folder, pattern):
    found_directories = []
    for root, dirs, files in os.walk(root_folder):
        for directory in dirs:
            if pattern.search(directory): 
                found_directories.append(os.path.join(root, directory))
    return found_directories

def open_folder_path(path):
    try:
        subprocess.Popen(f'explorer "{path}"')
    except Exception as e:
        print(f"Lỗi: {e}")

def open_folder(foldername):
    foldername = foldername.strip()
    root_folders = ["C:\\","D:\\","E:\\"]
    for root_folder in root_folders:
        pattern = re.compile(foldername, re.IGNORECASE)  
        result = find_directories(root_folder, pattern)
        for directory in result:
            open_folder_path(directory)
