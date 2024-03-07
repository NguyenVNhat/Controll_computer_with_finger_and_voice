import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import sys
sys.path.insert(0,'Controller')
import main

class SimpleGUI:
    Status = True
    def __init__(self, master):


        self.master = master
        self.master.title("Simple GUI")
        self.master.geometry("400x200")

        self.style = ThemedStyle(master)
        self.style.set_theme("plastik")  # Chọn một chủ đề giao diện (plastik, equilux, winxpblue, ...)

        self.label = ttk.Label(master, text="Hello, Welcome to Simple GUI", font=('Helvetica', 12))
        self.label.pack(pady=20)

        self.button = ttk.Button(master, text="Bắt đầu", command=self.button_click)
        self.button.pack()

        self.button = ttk.Button(master, text="Kết thúc", command=self.button_click_1)
        self.button.pack()


    def button_click(self):
        while self.Status == True:
            request = main.getAudio()
            main.mainFunction(request)
    def button_click_1(self):
        self.Status == False
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleGUI(root)
    root.mainloop()
