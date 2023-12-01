from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs import Querybox
import tkinter as tk
from datetime import date


class AppDelegate:
    def applicationSupportsSecureRestorableState_(self, app):
        return True


########################################
###        Created a Function        ###
def datey():
    # Grab the date
    my_label.config(text=f"You Picked: {my_date.entry.get()}")
    
def things():
    cal = Querybox()
    my_label.config(text=f"You Picked: {cal.get_date()}")


########################################
###          Root Setting            ###
root = tb.Window(themename="darkly") # 윈도우 데모
root.title('') # 창 제목
root.iconbitmap('./ttk.png') # 창 아이콘
root.geometry('500x350') # 창 사이즈


########################################
###            Date Entry            ###
my_date = tb.DateEntry(root, bootstyle="danger", startdate=date(2023, 10, 1), firstweekday=6)
my_date.pack(pady=50)

my_button = tb.Button(root, text="Get Date", bootstyle="danger outline", command=datey)
my_button.pack(pady=20)

my_button2 = tb.Button(root, text="Get Calendar", bootstyle="success outline", command=things)
my_button2.pack(pady=20)

my_label = tb.Label(root, text="You Picked: ")
my_label.pack(pady=20)


########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

