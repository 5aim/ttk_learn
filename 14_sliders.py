from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import tkinter as tk

class AppDelegate:
    def applicationSupportsSecureRestorableState_(self, app):
        return True

########################################
###        Created a Function        ###
def scaler(e):
    my_label.config(text=f"{int(my_scale.get())} %")
    # if my_scale.get() < 50:


########################################
###          Root Setting            ###
root = tb.Window(themename="darkly") # 윈도우 데모
root.title('') # 창 제목
root.iconbitmap('./ttk.png') # 창 아이콘
root.geometry('500x350') # 창 사이즈


########################################
###              Slider              ###
# Create a Scale/Slider
my_scale = tb.Scale(root, bootstyle="danger", length=200, orient="horizontal", from_=0, to=100, command=scaler)
my_scale.pack(pady=50)

my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack()


########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

