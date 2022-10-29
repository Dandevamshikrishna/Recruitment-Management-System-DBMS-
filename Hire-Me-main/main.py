from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import screensize
from modules.login import *

win = Tk()
def reset_win():
   win.wm_geometry("9850x850")
# root.wm_geometry("1080x700")
win.title("Hire ME")
# win.resizable(0, 0)
win.iconbitmap(r'elements\\favicon.ico')
log(win)
win.mainloop()

