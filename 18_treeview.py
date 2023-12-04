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
###            Tree view             ###

# Define Columns
columns = ("first_name", "last_name", "email")


# Create Treeview
my_tree = tb.Treeview(root, bootstyle="light", columns=columns, show="headings")
my_tree.pack(pady=20)

# Define headings
my_tree.heading("first_name", text="First Name")
my_tree.heading("last_name", text="Last Name")
my_tree.heading("email", text="Email Address")


# Create Sample Data
contacts = []

for n in range(1,20):
    contacts.append((f"First {n}", f"Last {n}", f"email {n} @ address.com"))


# Add Data To Treeview
for contact in contacts:
    my_tree.insert("", END, values=contact)


########################################
###               Main               ###
app_delegate = AppDelegate()

if __name__ == "__main__":
    root.mainloop()

