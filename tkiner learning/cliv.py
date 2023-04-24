import tkinter as tk
from tkinter import ttk
root=tk.Tk()
def onclick():
    print("You clicked right!")
click_button=ttk.Button(root,text="clickMe",command=onclick())
click_button.pack(ipadx=5,ipady=5)
root.mainloop()