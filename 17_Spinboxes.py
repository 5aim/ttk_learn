from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import tkinter as tk

class AppDelegate:
    def applicationSupportsSecureRestorableState_(self, app):
        return True

########################################
###        Created a Function        ###
def spinny():
    my_label.config(text=my_spin.get())


########################################
###          Root Setting            ###
root = tb.Window(themename="darkly") # 윈도우 데모
root.title('') # 창 제목
root.iconbitmap('./ttk.png') # 창 아이콘
root.geometry('500x350') # 창 사이즈


########################################
###            SpinBoxes             ###
# Spinbox List
stuff = ["John", "April", "Bob", "Mary"]

# Spinbox
my_spin = tb.Spinbox(root, bootstyle="success", font=("Helvetica", 18), values=stuff, state="readonly", command=spinny)
my_spin.pack(pady=20)

# Set Spinbox Dedault
my_spin.set("Choice !")

# Button
my_button = tb.Button(root, text="Click Me !", bootstyle="success outline", command=spinny)
my_button.pack(pady=20)

# Label
my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)

########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

