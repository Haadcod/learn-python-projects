"""Desktop application to allow user input year and calculate his age"""
import datetime
import tkinter as tk
window=tk.Tk()
window.geometry("620x780")
window.title("Desktop Age Calculator")
label1=tk.Label(text="Age calculator",font=("Times new roman",40))
label1.grid()
name=tk.Label(text="Name",font=("Times new roman",20))
name.grid(column=0,row=1)
year=tk.Label(text="Year",font=("Times new roman",20))
year.grid(column=0,row=2)
month=tk.Label(text="Month",font=("Times new roman",20))
month.grid(column=0,row=3)
date=tk.Label(text="Date",font=("Times new roman",20))
date.grid(column=0,row=4)
nameEntry=tk.Entry()
nameEntry.grid(column=1,row=1)
yearEntry=tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry=tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry=tk.Entry()
dateEntry.grid(column=1,row=4)
def getInput():
    name=nameEntry.get()
    monkey=Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))
    textArea=tk.Text(master=window,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer="Heyy {monkey)!!!.You are {age} years old!!!".format(monkey=name,age=monkey.age())
    textArea.insert(tk.END,answer)
button=tk.Button(window,text="Calculate Age",command=getInput,bg="blue")
button.grid(column=1,row=5)
class Person:
    def __init__(self,name,birthdate):
        self.name=name
        self.birthdate=birthdate
    def age(self):
        today=datetime.date.today()
        age=today.year-self.birthdate.year
        return age


window.mainloop()
