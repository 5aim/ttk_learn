from tkinter import *
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog
import ttkbootstrap as tb
import tkinter as tk

class AppDelegate:
    def applicationSupportsSecureRestorableState_(self, app):
        return True

########################################
###        Created a Function        ###
def cc():
    # Create Color Chooser
    my_color = ColorChooserDialog()
    
    # Show Color
    my_color.show()
    
    # Retrun Color
    colors = my_color.result
    
    # Output (.hex .hsl .rgb)
    my_label.config(text=colors.hex)
    
    # Change the bg color of our app to chosen color
    root.configure(background=colors.hex)


########################################
###          Root Setting            ###
root = tb.Window(themename="darkly") # 윈도우 데모
root.title('') # 창 제목
root.iconbitmap('./ttk.png') # 창 아이콘
root.geometry('500x350') # 창 사이즈


########################################
###            color box             ###

my_button = tb.Button(root, text="Click Me !", bootstyle="danger", command=cc)
my_button.pack(pady=40)

my_label = tb.Label(root, text="", font=("Helvetiva", 18))
my_label.pack(pady=10)


########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

