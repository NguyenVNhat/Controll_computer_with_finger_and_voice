import subprocess
import tkinter as tk
import os

def OpenSetting(value):
    value = value.lower()
    try:
        if 'mở cài đặt' == value:
            subprocess.run(["start", "ms-settings:"], shell=True)
        elif 'âm thanh' in value:
            subprocess.run(["start", "ms-settings:sound"], shell=True)
        elif 'display' in value:
            subprocess.run(["start", "ms-settings:display"], shell=True)
        elif 'autoplay' in value:
            subprocess.run(["start", "ms-settings:display"], shell=True)
        elif 'usb' in value:
            subprocess.run(["start", "ms-settings:usb"], shell=True)
        elif 'pen and windows ink' in value:
            subprocess.run(["start", "ms-settings:pen"], shell=True)
        elif 'touchpad' in value:
            subprocess.run(["start", "ms-settings:devices-touchpad"], shell=True)
        elif 'mobile-devices' in value:
            subprocess.run(["start", "ms-settings:mobile-devices"], shell=True)
        elif 'mouse' in value:
            subprocess.run(["start", "ms-settings:mousetouchpad"], shell=True)
        elif 'printers' in value:
            subprocess.run(["start", "ms-settings:printers"], shell=True)
        elif 'bluetooth' in value:
            subprocess.run(["start", "ms-settings:bluetooth"], shell=True)
    except Exception as e:
        print(f"An error occurred: {e}")

