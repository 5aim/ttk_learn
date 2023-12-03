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
###           Scrollbars             ###
# Frame
my_frame = tb.Frame(root)
my_frame.pack(pady=20)

# Create A Scrollbar
my_scroll = tb.Scrollbar(my_frame, orient="vertical", bootstyle="dark round")
my_scroll.pack(side="right", fill="y")

# Create A Text Widget
my_text = Text(my_frame, width=30, height=25, yscrollcommand=my_scroll.set, wrap="none", font=("helvetica", 18))
my_text.pack()

# Config the Scrollbar
my_scroll.config(command=my_text.yview)


########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

