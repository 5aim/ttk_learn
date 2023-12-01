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
###            Notebooks             ###
my_notebook = tb.Notebook(root, bootstyle="dark")
my_notebook.pack(pady=20)

tab1 = tb.Frame(my_notebook)
tab2 = tb.Frame(my_notebook)

my_label = Label(tab1, text="My Awesome Label1 !", font=("Helvetica", 18))
my_label.pack(pady=20)

my_text = Text(tab1, width=70, height=10)
my_text.pack(pady=10, padx=10)

my_button = tb.Button(tab1, text="Click Me !", bootstyle="danger outline")
my_button.pack(pady=20)

my_label2 = Label(tab2, text="My Awesome Label2 !", font=("Helvetica", 18))
my_label2.pack(pady=20)

###   Add our frames to the notebook   ###
my_notebook.add(tab1, text="Tab One")
my_notebook.add(tab2, text="Tab Two")


########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

