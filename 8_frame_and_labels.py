from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import tkinter as tk

class AppDelegate:
    def applicationSupportsSecureRestorableState_(self, app):
        return True

########################################
###        Created a Function        ###
def thing():
    pass


########################################
###          Root Setting            ###
root = tb.Window(themename="darkly") # 윈도우 데모
root.title('') # 창 제목
root.iconbitmap('./ttk.png') # 창 아이콘
root.geometry('500x350') # 창 사이즈

########################################
###         frame and labels         ###
my_frame = tb.Frame(root, bootstyle="dark")
my_frame.pack(pady=40)

my_entry = tb.Entry(my_frame, font=("Helvetica", 18))
my_entry.pack(pady=20, padx=20)

my_button = tb.Button(my_frame, text="Click me !", bootstyle="success outline", command=thing)
my_button.pack(pady=20, padx=20)

my_label = tb.Label(root, text="Hello There !", font=("Helvetica", 18), bootstyle="success")
my_label.pack(pady=20)


########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

