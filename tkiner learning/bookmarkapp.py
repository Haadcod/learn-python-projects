"""This is an App consisting of the manutg and premier league app which whwn clicked load or
refer to a corresponding page """
import tkinter as tk
import webbrowser
def man_united(event):
    webbrowser.open_new_tab("https://www.manutd.com")
def premier_league(event):
    webbrowser.open_new_tab("https://www.premierleague.com")
root=tk.Tk()
root.geometry("500x400")
root.title("My manchester united App")
label1=tk.Label(text="This is manchester united app",font=("Times new roman",20))
label1.grid(column=0,row=0)
button1=tk.Button(root,text="ManUtd",bg="orange")
button1.grid(column=1,row=1)
button2=tk.Button(root,text="PremierLeague",bg="blue")
button2.grid(column=3,row=1)
button1.bind("<Button-1>",man_united)
button2.bind("<Button-1>",premier_league)
#label1.pack()
root.mainloop()