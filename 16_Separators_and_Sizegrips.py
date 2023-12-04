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
root = tb.Window(themename="darkly") # 윈도우 데모
root.title('') # 창 제목
root.iconbitmap('./ttk.png') # 창 아이콘
root.geometry('500x350') # 창 사이즈


########################################
###    Separators and Sizegrips      ###
label1 = tb.Label(root, text="Label 1", bootstyle="light")
label1.pack(pady=40)

my_sep = tb.Separator(root, bootstyle="info", orient="horizontal")
my_sep.pack(fill="x", padx=20)

label2 = tb.Label(root, text="Label 2", bootstyle="light")
label2.pack(pady=40)

# Sizegrip
my_sizegrip = tb.Sizegrip(root, bootstyle="info")
my_sizegrip.pack(anchor="se", fill="both", expand=True)


########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

