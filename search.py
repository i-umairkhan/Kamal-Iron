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

background_img = PhotoImage(file = f"Images\SearchBackground.png")
background = canvas.create_image(
    499, 79,
    image=background_img)


name = Entry(bd=0, bg="#C4C4C4", highlightthickness=0)
name.place(x=493, y=70, width=213, height=28)

def showname():
    df = pd.read_csv("Csv\\customers.csv")
    df = pd.DataFrame(df)
    df.sort_values(['DateTime'],ascending=False,inplace=True)
    for i in range(len(df)):
        if(df.loc[i,"Name"]==name.get()):
            df = pd.DataFrame(df[df["Name"]==name.get()])
            CustomerDate = df.iloc[0,1]
            CustomerName = df.iloc[0,2]
            CustomerAddress = df.iloc[0,3]
            CustomerPhone1 = int(df.iloc[0,4])
            CustomerPhone2 = df.iloc[0,5]
            CustomerTotal = int(df.iloc[0,6])
            CustomerRecived = int(df.iloc[0,7])
            CustomerRemaning = int(df.iloc[0,8])
            CustomerDueDate = df.iloc[0,9]
            break
    
    global dataDate,dataName,dataAddress,dataPhone1,dataPhone2,dataTotal,dataRecived,dataRemaning,dataDueDate,nouser
    
    nouser = Label(window,text= "NO RECORD FOUND !!!",background="#ffffff",font="height=20")
    if(df.loc[i,"Name"]!=name.get()):
        CustomerDate = " "
        CustomerName = " "
        CustomerAddress = " "
        CustomerPhone1 = " "
        CustomerPhone2 = " "
        CustomerTotal = " "
        CustomerRecived = " "
        CustomerRemaning = " "
        CustomerDueDate = " "
        nouser.place(x=465,y=220)

    
    dataDate = Label(window,text= CustomerDate,background="#ffffff",font="height=20")
    dataDate.place(x=57,y=211)

    dataName = Label(window,text= CustomerName,background="#ffffff",font="height=20")
    dataName.place(x=57,y=169)

    dataAddress = Label(window,text= CustomerAddress,background="#ffffff",font="height=20")
    dataAddress.place(x=157,y=169)

    dataPhone1 = Label(window,text= CustomerPhone1,background="#ffffff",font="height=20")
    dataPhone1.place(x=274,y=169)

    dataPhone2 = Label(window,text= CustomerPhone2,background="#ffffff",font="height=20")
    dataPhone2.place(x=394,y=169)

    dataTotal = Label(window,text= CustomerTotal,background="#ffffff",font="height=20")
    dataTotal.place(x=514,y=169)

    dataRecived = Label(window,text= CustomerRecived,background="#ffffff",font="height=20")
    dataRecived.place(x=606,y=169)

    dataRemaning = Label(window,text= CustomerRemaning,background="#ffffff",font="height=20")
    dataRemaning.place(x=722,y=169)

    dataDueDate = Label(window,text= CustomerDueDate,background="#ffffff",font="height=20")
    dataDueDate.place(x=860,y=169)



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
    name.delete(0,END)
    nouser.destroy()

SearchButton = Button(window,text="Search",command=showname,padx=8,pady=5,background="#797766",fg="#ffffff")
SearchButton.place(x=733,y=70)


ClearButton = Button(window,text="Clear",command=clearfun,padx=8,pady=5,background="#797766",fg="#ffffff")
ClearButton.place(x=814,y=70)


window.resizable(False, False)
window.mainloop()
