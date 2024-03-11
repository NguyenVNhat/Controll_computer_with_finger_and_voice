import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import sys
sys.path.insert(0,'Controller')


class SimpleGUI:
    Status = True
    def __init__(self, master):


        self.master = master
        self.master.title("Simple GUI")
        self.master.geometry("600x600")
        self.style = ThemedStyle(master)
        self.style.set_theme("plastik")

        self.button = ttk.Button(master, text="Bắt đầu" )
        self.button.pack()

        self.button = ttk.Button(master, text="Kết thúc")
        self.button.pack()


   
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleGUI(root)
    root.mainloop()
