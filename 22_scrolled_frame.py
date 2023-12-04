from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame
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
###         scrolled frame           ###
my_frame = ScrolledFrame(root, autohide=True, bootstyle="dark")
my_frame.pack(pady=15, padx=15, fill=BOTH, expand=YES)

# Create some buttons
for x in range(21):
    tb.Button(my_frame, bootstyle="info", text=f"Click Me ! {x}").pack(pady=20)


########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

