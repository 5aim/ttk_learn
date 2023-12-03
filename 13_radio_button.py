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
    my_label.config(text=f'You selected: {my_topping.get()}')


########################################
###          Root Setting            ###
root = tb.Window(themename="darkly") # 윈도우 데모
root.title('') # 창 제목
root.iconbitmap('./ttk.png') # 창 아이콘
root.geometry('500x350') # 창 사이즈


########################################
###           Radio Button           ###
# Created Radio Button List
toppings = ["Pepperoni", "Cheese", "Veggie"]

# Create A Tkinter Variable To Keep Track of everything
my_topping = StringVar()
for topping in toppings:
    tb.Radiobutton(root, bootstyle="danger", variable=my_topping, text=topping, value=topping, command=clicker).pack(pady=20)

# Create Button
my_button = tb.Button(root, text="Click Me !", bootstyle="dark outline")
my_button.pack(pady=20)

# Create Label
my_label = tb.Label(root, text="You Selected: ")
my_label.pack(pady=20)

#Create actual Radio Button Buttons
rb1 = tb.Radiobutton(root, bootstyle="info toolbutton", variable=my_topping, text="Radio Button 1", value="Radio Button 1", command=clicker)
rb1.pack(pady=20)

rb2 = tb.Radiobutton(root, bootstyle="info toolbutton outline", variable=my_topping, text="Radio Button 2", value="Radio Button 2", command=clicker)
rb2.pack(pady=20)

########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

