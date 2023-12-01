from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import tkinter as tk

class AppDelegate:
    def applicationSupportsSecureRestorableState_(self, app):
        return True

########################################
###        Created a Function        ###
global counter
counter =20
def clicker():
    global counter
    if counter <= 100:
        my_meter.configure(amountuser=counter)
        counter+=5
        my_button.configure(text=f"Click Me {my_meter.amountusedvar.get()}")

def stepup():
    my_meter.step(10)

def stepdown():
    my_meter.step(-10)

########################################
###          Root Setting            ###
root = tb.Window(themename="darkly") # 윈도우 데모
root.title('') # 창 제목
root.iconbitmap('./ttk.png') # 창 아이콘
root.geometry('500x350') # 창 사이즈


########################################
###             Meters               ###
my_meter = tb.Meter(
    root,
    bootstyle="danger",
    subtext="Tkinter Learned",
    interactive=True,
    textright='%',
    metertype="full",
    stripethickness=10,
    metersize=200,
    padding=50,
    amountused=0,
    amounttotal=100,
    subtextstyle="light"
    # and more in API
    )
my_meter.pack(pady=50)

my_button = tb.Button(root, text="Click Me 5", command=clicker)
my_button.pack(pady=20)

my_button2 = tb.Button(root, text="Step Up", command=stepup)
my_button2.pack(pady=20)

my_button3 = tb.Button(root, text="Step Down", command=stepdown)
my_button3.pack(pady=20)

########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

