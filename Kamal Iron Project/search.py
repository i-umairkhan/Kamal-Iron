from operator import index
from pdb import Restart
from typing import Any
import pandas as pd
import datetime
from tkinter import *

window = Tk()

window.geometry("999x599")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 599,
    width = 999,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"SearchBackground.png")
background = canvas.create_image(
    499, 245,
    image=background_img)


name = Entry(bd=0, bg="#C4C4C4", highlightthickness=0)
name.place(x=493, y=70, width=320, height=28)

def showname():
    df = pd.read_csv("customers.csv")
    df = pd.DataFrame(df[df["Name"]==name.get()])
    
    CustomerDate = df.iloc[0,0]
    CustomerName = df.iloc[0,1]
    CustomerAddress = df.iloc[0,2]
    CustomerPhone1 = df.iloc[0,3]
    CustomerPhone2 = df.iloc[0,4]
    CustomerTotal = df.iloc[0,5]
    CustomerRecived = df.iloc[0,6]
    CustomerRemaning = df.iloc[0,7]
    CustomerDueDate = df.iloc[0,8]

    global dataDate,dataName,dataAddress,dataPhone1,dataPhone2,dataTotal,dataRecived,dataRemaning,dataDueDate

    dataDate = Label(window,text= CustomerDate,padx=10,pady=3,background="#ffffff",font="height=20")
    dataDate.place(x=734,y=131)

    dataName = Label(window,text= CustomerName,padx=10,pady=3,background="#ffffff",font="height=20")
    dataName.place(x=228,y=131)

    dataAddress = Label(window,text= CustomerAddress,padx=10,pady=3,background="#ffffff",font="height=20")
    dataAddress.place(x=228,y=179)

    dataPhone1 = Label(window,text= CustomerPhone1,padx=10,pady=3,background="#ffffff",font="height=20")
    dataPhone1.place(x=228,y=227)

    dataPhone2 = Label(window,text= CustomerPhone2,padx=10,pady=3,background="#ffffff",font="height=20")
    dataPhone2.place(x=228,y=275)

    dataTotal = Label(window,text= CustomerTotal,padx=10,pady=3,background="#ffffff",font="height=20")
    dataTotal.place(x=228,y=323)

    dataRecived = Label(window,text= CustomerRecived,padx=10,pady=3,background="#ffffff",font="height=20")
    dataRecived.place(x=228,y=371)

    dataRemaning = Label(window,text= CustomerRemaning,padx=10,pady=3,background="#ffffff",font="height=20")
    dataRemaning.place(x=228,y=419)

    dataDueDate = Label(window,text= CustomerDueDate,padx=10,pady=3,background="#ffffff",font="height=20")
    dataDueDate.place(x=228,y=467)

def clearfun():
    dataDate.destroy()
    dataName.destroy()
    dataAddress.destroy()
    dataPhone1.destroy()
    dataPhone2.destroy()
    dataTotal.destroy()
    dataRecived.destroy()
    dataRemaning.destroy()
    dataDueDate.destroy()


SaveButton = Button(window,text="Search",command=showname,padx=8,pady=5,background="#797766",fg="#ffffff")
SaveButton.place(x=443,y=137)


ClearButton = Button(window,text="Clear",command=clearfun,padx=8,pady=5,background="#797766",fg="#ffffff")
ClearButton.place(x=543,y=137)


window.resizable(False, False)
window.mainloop()
