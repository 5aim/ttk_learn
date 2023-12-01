from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import tkinter as tk

class AppDelegate:
    def applicationSupportsSecureRestorableState_(self, app):
        return True

########################################
###        Created a Function        ###
def starter():
    my_gauge.start()

def stoper():
    my_gauge.stop()

def incer():
    my_gauge.step(1)
    my_label.config(text=f"Position: {my_gauge.variable.get()}")

########################################
###          Root Setting            ###
root = tb.Window(themename="darkly") # 윈도우 데모
root.title('') # 창 제목
root.iconbitmap('./ttk.png') # 창 아이콘
root.geometry('500x350') # 창 사이즈


########################################
###          Flood Gauge             ###
my_gauge = tb.Floodgauge(
    root,
    bootstyle="success",
    font=("Helvetica", 18),
    mask="Pos: {}%",
    maximum=100,
    orient="horizontal",
    value=0,
    mode="determinate"
    )
my_gauge.pack(pady=50, fill=X, padx=40)

start_button = tb.Button(root, text="start", bootstyle="danger outline", command=starter)
start_button.pack(pady=20)

stop_button = tb.Button(root, text="stop", bootstyle="danger outline", command=stoper)
stop_button.pack(pady=20)

inc_button = tb.Button(root, text="inc", bootstyle="danger outline", command=incer)
inc_button.pack(pady=20)

my_label = tb.Label(root, text="Position: ")
my_label.pack(pady=20)


########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

