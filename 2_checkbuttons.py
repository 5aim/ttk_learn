from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import tkinter as tk

class AppDelegate:
    def applicationSupportsSecureRestorableState_(self, app):
        return True

def checker():
    if var1.get() == 1:
        my_label.config(text="checked !")
    else:
        my_label.config(text="unchecked !")

root = tb.Window(themename="darkly")
root.title('2. check buttons')
root.iconbitmap('./ttk.png')
root.geometry('500x350')

# Label
my_label = Label(
    text="Click the checkbutton below",
    font=("Helvetica", 18)
    )
my_label.pack(pady=(40,10))

# Check box
var1 = IntVar()
my_check = tb.Checkbutton(
    text="Check Me Out !",
    bootstyle="light",
    variable=var1,
    onvalue=1,
    offvalue=0,
    command=checker
    )
my_check.pack(pady=10)

# Tool Button
var2 = IntVar()
my_check2 = tb.Checkbutton(
    text="Tool Button !",
    bootstyle="light, toolbutton",
    variable=var2,
    onvalue=1,
    offvalue=0,
    command=checker
    )
my_check2.pack(pady=10)

# Outlines Tool Button
var3 = IntVar()
my_check3 = tb.Checkbutton(
    text="Tool Button !",
    bootstyle="light, toolbutton, outline",
    variable=var3,
    onvalue=1,
    offvalue=0,
    command=checker
    )
my_check3.pack(pady=10)

# Round Toggle Button
var4 = IntVar()
my_check4 = tb.Checkbutton(
    text="Round Toggle Button !",
    bootstyle="light, round-toggle",
    variable=var4,
    onvalue=1,
    offvalue=0,
    command=checker
    )
my_check4.pack(pady=10)

# Square Toggle Button
var5 = IntVar()
my_check5 = tb.Checkbutton(
    text="Round Toggle Button !",
    bootstyle="light, square-toggle",
    variable=var5,
    onvalue=1,
    offvalue=0,
    command=checker
    )
my_check5.pack(pady=10)



# main
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

