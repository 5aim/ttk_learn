from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import tkinter as tk

class AppDelegate:
    def applicationSupportsSecureRestorableState_(self, app):
        return True

########################################
###        Created a Function        ###


########################################
###          Root Setting            ###
root = tb.Window(themename="darkly")
root.title('1. label_and_button')
root.iconbitmap('./ttk.png')
root.geometry('500x350')


########################################
###          Resize Button           ###

###          Button Style            ###
my_style = tb.Style()
my_style.configure('light.Outline.TButton', font=("Helvetica", 18))

my_button = tb.Button(
    style="light.Outline.TButton",
    text="Hello World",
    width=20, # 버튼 가로길이 조절 가능. 하지만 height는 없음.
    bootstyle="light"
    )
my_button.pack(pady=40)


########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

