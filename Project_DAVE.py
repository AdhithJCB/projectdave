import tkinter
from tkinter import messagebox
import os  
# hide main window
root = tkinter.Tk()
root.withdraw()
yeet = 0
# message box display

while (yeet < 10):
    yeet = yeet + 1
    messagebox.showwarning("Warning","GET OFF AND BE PRODUCTIVE")
else:
    os.system("taskkill /f /im MinecraftLauncher.exe")
    os.system("taskkill /f /im javaw.exe")