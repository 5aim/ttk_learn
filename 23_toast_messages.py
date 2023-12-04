from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.toast import ToastNotification
import tkinter as tk

class AppDelegate:
    def applicationSupportsSecureRestorableState_(self, app):
        return True

########################################
###        Created a Function        ###

def clicker():
    toast.show_toast()


########################################
###          Root Setting            ###
root = tb.Window(themename="darkly") # 윈도우 데모
root.title('') # 창 제목
root.iconbitmap('./ttk.png') # 창 아이콘
root.geometry('500x350') # 창 사이즈


########################################
###         Toast Messages           ###
toast = ToastNotification(
    title = "My Toast Title",
    message="This is a Toast Message !",
    duration=3000,
    alert=True,
    position=(-1915, 30, 'sw')
    )

my_button = tb.Button(root, text="Click Me ! ", command=clicker)
my_button.pack(pady=40)


########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

