import os
import time
import fnmatch
from comtypes import CLSCTX_ALL

lstApp = ['winword.exe','chrome.exe','powerpnt.exe']
lstappuser = ['word','google','powerpoint']
#mở nhiều app trên máy tính
def open_application_multi(text):
    text = text.lower()
    for user_app, actual_app in zip(lstappuser, lstApp):
        if user_app in text:
            text = text.replace(user_app, actual_app)
    
    lst = []
    
    for txt in lstApp:
        if txt in text:
            lst.append(txt)
    print(lst)
    for app in lst:
        open_application(app)
        time.sleep(5)
#mở 1 app
def open_application(text):
    applications_folder = "C:\Program Files" 
    for root, dirs, files in os.walk(applications_folder):
        for file in files:
            if fnmatch.fnmatch(file.lower(), f'*{text.lower()}*'):
                os.startfile(os.path.join(root, file))