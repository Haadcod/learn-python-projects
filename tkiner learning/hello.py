import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root=tk.Tk()
root.title("Tkinter window demo")
root.geometry("800x700+50+50")
root.resizable(False,False)
#root.attributes('-alpha',0.5)
message=tk.Label(root,text="hello world")
message.pack()
#download button
def download_clicked():
    showinfo(title='information',message='Download button clicked!')
download_icon=tk.PhotoImage(file='C:\Users\haad\Pictures\luwobo\3.PNG')
download_button=ttk.Button(root,image=download_icon,command=download_clicked())
download_button.pack(ipadx=5,ipady=5,expand=True)
#displaying button
exit_button=ttk.Button(root,text='Exit',command=lambda :root.quit())
exit_button.pack(ipadx=5,ipady=5,expand=True)
root.mainloop()