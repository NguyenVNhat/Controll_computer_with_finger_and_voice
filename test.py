import subprocess
import tkinter as tk
import os

def show_wifi_networks():
    result = subprocess.check_output('cmd /c "netsh wlan show networks"', shell=True, text=True)
    networks = result.splitlines()
    root = tk.Tk()
    root.title("WiFi Networks")
    listbox = tk.Listbox(root, width=80, height=20)
    for network in networks:
        listbox.insert(tk.END, network)
    listbox.pack(expand=True, fill="both")

    root.mainloop()
    return networks

def getlistNameWifi():
    listWF = show_wifi_networks()
    init = 4
    lstWF = []
    while init < len(listWF) :
        nameWF = (listWF[init])
        lstWF.append(nameWF[9:])
        init += 5
    return lstWF

def connectWF():
    lstWF = getlistNameWifi()
    number  = int(input('Nhập fw : '))
    name_of_router = lstWF[number-1]
    os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')

connectWF()
    

