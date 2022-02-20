from operator import index
from pdb import Restart
from tkinter import ttk
from typing import Any
import pandas as pd
import datetime
from tkinter import *

window = Tk()

window.geometry("999x599")
window.configure(bg = "#ffffff")
# *** CANVAS **********************************************
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 599,
    width = 999,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

# *** BACKGROUD IMAGE *************************************
background_img = PhotoImage(file = f"Images\SearchBackground.png")
background = canvas.create_image(
    499, 79,
    image=background_img)

# *** CUSTOMER INFO INPUTS ********************************
name = Entry(bd=0, bg="#C4C4C4", highlightthickness=0)
name.place(x=493, y=70, width=213, height=28)
# *********************************************************

# *** TREE VIWE *******************************************
s = ttk.Style()
s.theme_use('classic')
s.configure('Treeview.Heading', background="#E5E5E5")
tree=ttk.Treeview(window)
vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
vsb.pack(side='right', fill='y')
tree["columns"]=("Date","Name","Address","Phone1","Phone2","Total","Recived","Remaning","DueDate")
tree.column("#0", width=0, minwidth=0)
tree.column("Date", width=105, minwidth=105)
tree.column("Name", width=105, minwidth=105)
tree.column("Address", width=105, minwidth=105)
tree.column("Phone1", width=105, minwidth=105)
tree.column("Phone2", width=105, minwidth=105)
tree.column("Total", width=105, minwidth=105)
tree.column("Recived", width=105, minwidth=105)
tree.column("Remaning", width=105, minwidth=105)
tree.column("DueDate", width=105, minwidth=105)
tree.heading("Date",text="Date")
tree.heading("Name",text="Name")
tree.heading("Address",text="Address")
tree.heading("Phone1",text="Phone1")
tree.heading("Phone2",text="Phone2")
tree.heading("Total",text="Total")
tree.heading("Recived",text="Recived")
tree.heading("Remaning",text="Remaning")
tree.heading("DueDate",text="DueDate")
tree.place(x=30,y=160)
# *********************************************************

# *** SHOW FUNCTION ***************************************
def showname():
    global nouser
    nouser = Label(window,text= "",background="#ffffff",font="height=20")
    df = pd.read_csv("Csv\\customers.csv")
    df = pd.DataFrame(df)
    df.sort_values(['DateTime'],ascending=True,inplace=True)
    j = 0;
    df = df.loc[df["Name"]==name.get()]
    for i in range(len(df)):
            CustomerDate = df.iloc[j,1]
            CustomerName = df.iloc[j,2]
            CustomerAddress = df.iloc[j,3]
            CustomerPhone1 = int(df.iloc[j,4])
            CustomerPhone2 = df.iloc[j,5]
            CustomerTotal = int(df.iloc[j,6])
            CustomerRecived = int(df.iloc[j,7])
            CustomerRemaning = int(df.iloc[j,8])
            CustomerDueDate = df.iloc[j,9]
            tree.insert("",END,values=(CustomerDate,CustomerName,CustomerAddress,
                                CustomerPhone1,CustomerPhone2,CustomerTotal,CustomerRecived,CustomerRemaning,CustomerDueDate))
            j = j+1



# *********************************************************

# *** CLEAR FUNCTION **************************************
def clearfun():
    name.delete(0,END)
    nouser.destroy()
    for i in tree.get_children():
        tree.delete(i)
# *********************************************************

# *** BUTTONS *********************************************
SearchButton = Button(window,text="Search",command=showname,padx=8,pady=5,background="#797766",fg="#ffffff")
SearchButton.place(x=733,y=70)
ClearButton = Button(window,text="Clear",command=clearfun,padx=8,pady=5,background="#797766",fg="#ffffff")
ClearButton.place(x=814,y=70)
# *********************************************************


window.resizable(False, False)
window.mainloop()
