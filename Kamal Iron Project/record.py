from ntpath import join
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
background_img = PhotoImage(file = f"Images\customerRecord.png")
background = canvas.create_image(
    499, 62,
    image=background_img)

# *** CUSTOMER INFO INPUTS ********************************
name = Entry(bd=0, bg="#C4C4C4", highlightthickness=0)
name.place(x=493, y=70, width=213, height=28)
# *********************************************************

# *** TREE VIWE *******************************************
s = ttk.Style()
s.theme_use('classic')
s.configure('Treeview.Heading', background="#E5E5E5")
tree=ttk.Treeview(window,height=21)
vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
vsb.pack(side='right', fill='y')
tree["columns"]=("Date","Name","Address","Phone1","Advance","Total","Recived","Remaning","DueDate")
tree.column("#0", width=0, minwidth=0)
tree.column("Date", width=105, minwidth=105)
tree.column("Name", width=105, minwidth=105)
tree.column("Address", width=105, minwidth=105)
tree.column("Phone1", width=105, minwidth=105)
tree.column("Advance", width=105, minwidth=105)
tree.column("Total", width=105, minwidth=105)
tree.column("Recived", width=105, minwidth=105)
tree.column("Remaning", width=105, minwidth=105)
tree.column("DueDate", width=105, minwidth=105)
tree.heading("Date",text="Date")
tree.heading("Name",text="Name")
tree.heading("Address",text="Address")
tree.heading("Phone1",text="Phone1")
tree.heading("Advance",text="Advance")
tree.heading("Total",text="Total")
tree.heading("Recived",text="Recived")
tree.heading("Remaning",text="Remaning")
tree.heading("DueDate",text="DueDate")
tree.place(x=10,y=130)
# *********************************************************

# *** SHOW FUNCTION ***************************************
def showname():
    global nouser
    nouser = Label(window,text= "",background="#ffffff",font="height=20")
    df = pd.read_csv("Csv\\customers.csv")
    df = pd.DataFrame(df)
    df.sort_values(['DateTime'],ascending=True,inplace=True)
    df = df.loc[df["Name"]==name.get()]
    df2 = pd.read_csv("Csv\\advance.csv")
    df2 = pd.DataFrame(df2)
    df2.sort_values(['DateTime'],ascending=True,inplace=True)
    df2 = df2.loc[df2["Name"]==name.get()]
    global CustomerAdvance
    CustomerAdvance=0
    j = 0
    for i in range(len(df)):
            CustomerDate = df.iloc[j,1]
            CustomerName = df.iloc[j,2]
            CustomerAddress = df.iloc[j,3]
            CustomerPhone1 = int(df.iloc[j,4])
            CustomerAdvance = int(df2.iloc[j,7])
            CustomerTotal = int(df.iloc[j,6])
            CustomerRecived = int(df.iloc[j,7])
            CustomerRemaning = int(df.iloc[j,8])
            CustomerDueDate = df.iloc[j,9]
            item1 = df.iloc[j,10]
            item2 = df.iloc[j,11]
            item3 = df.iloc[j,12]
            item4 = df.iloc[j,13]
            item5 = df.iloc[j,14]
            item6 = df.iloc[j,15]
            item7 = df.iloc[j,16]
            item8 = df.iloc[j,17]
            tree.insert("",END,iid=i,open=False,values=(CustomerDate,CustomerName,CustomerAddress,
                                CustomerPhone1,CustomerAdvance,CustomerTotal,CustomerRecived,CustomerRemaning,CustomerDueDate))
            tree.insert(i,END,values=(item1,item2,item3,item4,item5,item6,item7,item8))
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
SearchButton = Button(window,text="Search",command=showname,padx=8,pady=5,background="#47B759",fg="#ffffff")
SearchButton.place(x=733,y=70)
ClearButton = Button(window,text="Clear",command=clearfun,padx=8,pady=5,background="#db5353",fg="#ffffff")
ClearButton.place(x=814,y=70)
# *********************************************************


window.resizable(False, False)
window.mainloop()
