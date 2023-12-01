from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import tkinter as tk

class AppDelegate:
    def applicationSupportsSecureRestorableState_(self, app):
        return True

########################################
###        Created a Function        ###
def clicker():
    my_label.config(text=f"You Clicked On {my_combo.get()} !")
    
def click_bind(e):
    my_label.config(text=f"You Clicked On {my_combo.get()} !")

########################################
###          Root Setting            ###
root = tb.Window(themename="darkly") # 윈도우 데모
root.title('4. combo boxes') # 창 제목
root.iconbitmap('./ttk.png') # 창 아이콘
root.geometry('500x350') # 창 사이즈


########################################
###          Combo Boxes             ###

my_label = tb.Label(root, text="Hello World", font=("Helverica", 18))
my_label.pack(pady=30)

###      Create Dropdown options     ###
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saterday", "Sunday"]

###          Create Combobox         ###
my_combo = tb.Combobox(root, bootstyle="light", values=days)
my_combo.pack(pady=20)

###         Set Combo Default        ###
my_combo.current(0)

###          Create a Button         ###
my_button = tb.Button(root, text="Click Me !", command=clicker, bootstyle="light")
my_button.pack(pady=20)

###         Bind the combobox        ###
my_combo.bind("<<ComboboxSelected>>", click_bind)


########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()
