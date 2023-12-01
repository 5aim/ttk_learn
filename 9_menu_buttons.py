from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import tkinter as tk

class AppDelegate:
    def applicationSupportsSecureRestorableState_(self, app):
        return True

########################################
###        Created a Function        ###
def stuff(x):
    my_label.config(bootstyle=x)
    my_label.config(text=f"You Selected: {x}")

########################################
###          Root Setting            ###
root = tb.Window(themename="darkly") # 윈도우 데모
root.title('') # 창 제목
root.iconbitmap('./ttk.png') # 창 아이콘
root.geometry('500x350') # 창 사이즈


########################################
###          Menu Button             ###
my_menu = tb.Menubutton(root, bootstyle="warning", text="Things !")
my_menu.pack(pady=50)

###        Create Basic Menu         ###
inside_menu = tb.Menu(my_menu)

###   Add Items To Our Inside Menu   ###
item_var = StringVar()
for x in ['primary', 'secondary', 'danger', 'info', 'outline primary', 'outline secondary', 'outline danger', 'outline info']:
    inside_menu.add_radiobutton(label=x, variable=item_var, command=lambda x=x: stuff(x))

###   Associate the inside menu with the menubutton   ###
my_menu['menu'] = inside_menu

my_label = tb.Label(root, text="")
my_label.pack(pady=40)

########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

