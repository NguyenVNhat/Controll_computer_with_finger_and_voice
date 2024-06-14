import subprocess
import tkinter as tk
import os
import logging
import json
logging.basicConfig(level=logging.WARNING)

def OpenSetting(value):
    try:
        if len(value) == 2:
            subprocess.run([value[0], value[1]], shell=True)
        else :
            subprocess.run(value, shell=True)
    except Exception as e:
        logging.warning('Error : open setting')
