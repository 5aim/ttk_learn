from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import tkinter as tk

class AppDelegate:
    def applicationSupportsSecureRestorableState_(self, app):
        return True

########################################
###        Created a Function        ###
def speak():
    my_label.config(text=f"You Typed: {my_entry.get()}")


########################################
###          Root Setting            ###
root = tb.Window(themename="darkly") # 윈도우 데모
root.title('') # 창 제목
root.iconbitmap('./ttk.png') # 창 아이콘
root.geometry('500x350') # 창 사이즈


########################################
###      Create Entry Function       ###


###       Create Entry Widget        ###
my_entry = tb.Entry(root,
                    bootstyle="success",
                    font=("Helvetica", 18),
                    foreground="#999999",
                    show="*",
                    width=5
                    )
my_entry.pack(pady=50)

###          Create Button           ###
my_button = tb.Button(root, bootstyle="danger outline", text="Click Me !", command=speak)
my_button.pack(pady=20)

###           Create Label           ###
my_label = tb.Label(root, text="")
my_label.pack(pady=20)


########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

