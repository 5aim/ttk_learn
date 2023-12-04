from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import tkinter as tk
from ttkbootstrap.dialogs import Messagebox

class AppDelegate:
    def applicationSupportsSecureRestorableState_(self, app):
        return True

########################################
###        Created a Function        ###

def clicker():
    # Create a dialog
    # yesno, ok, okcancel, show_info, show_error, show_question, show_warning, yesnocancel, retrycancel
    # mb = Messagebox.yesno("Display Some Message Here", "Here is the Title")
    # mb = Messagebox.ok("Display Some Message Here", "Here is the Title")
    # mb = Messagebox.okcancel("Display Some Message Here", "Here is the Title")
    # mb = Messagebox.show_info("Display Some Message Here", "Here is the Title")
    # mb = Messagebox.show_error("Display Some Message Here", "Here is the Title")
    # mb = Messagebox.show_question("Display Some Message Here", "Here is the Title")
    # mb = Messagebox.show_warning("Display Some Message Here", "Here is the Title")
    mb = Messagebox.yesnocancel("Display Some Message Here", "Here is the Title")
    

    if mb == "No":
        print("no")
        my_label.config(text=f"You Clicked {mb}")
    else:
        print("yes")
        my_label.config(text=f"You Clicked {mb}")

########################################
###          Root Setting            ###
root = tb.Window(themename="darkly") # 윈도우 데모
root.title('') # 창 제목
root.iconbitmap('./ttk.png') # 창 아이콘
root.iconbitmap('./ttk.png') # 메세지 박스 아이콘
root.geometry('500x350') # 창 사이즈


########################################
###          Message Boxes           ###
my_button = tb.Button(root, text="Click Me !", bootstyle="danger", command=clicker)
my_button.pack(pady=40)

my_label = tb.Label(root, text='', font=("Helverica", 18))
my_label.pack(pady=20)



########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

