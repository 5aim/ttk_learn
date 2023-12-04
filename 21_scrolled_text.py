from tkinter import *
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
import ttkbootstrap as tb
import tkinter as tk

class AppDelegate:
    def applicationSupportsSecureRestorableState_(self, app):
        return True

########################################
###        Created a Function        ###


########################################
###          Root Setting            ###
root = tb.Window(themename="darkly") # 윈도우 데모
root.title('') # 창 제목
root.iconbitmap('./ttk.png') # 창 아이콘
root.geometry('500x350') # 창 사이즈


########################################
###         scrolled text            ###
my_text = ScrolledText(root, height=20, width=110, wrap=WORD, autohide=True, bootstyle="dark")
my_text.pack(pady=15)


########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

