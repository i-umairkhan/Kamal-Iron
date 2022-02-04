from asyncio import transports
from cgitb import text
from functools import total_ordering
from tkinter import *
from numpy import gradient
import pandas as pd
import datetime

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
background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    499, 294,
    image=background_img)


# *** DATE TIME *******************************************

date_time = datetime.date.today()

# *********************************************************

# *** CUSTOMER INFO INPUTS ********************************

name = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
name.place(x=94, y=69, width=146, height=27)

address = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
address.place(x=336, y=69, width=146, height=27)

phone1 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
phone1.place(x=579, y=69, width=146, height=27)

phone2 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
phone2.place(x=827, y=69, width=146, height=27)

Labour = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
Labour.place(x=787, y=141, width=146, height=27)
Labour.insert(0,0)

Transport = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
Transport.place(x=787, y=183, width=146, height=27)
Transport.insert(0,0)

OtherAmount = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
OtherAmount.place(x=787, y=225, width=146, height=27)
OtherAmount.insert(0,0)

# *********************************************************

# *** DROP DOWN ITEMS *************************************
DropDownItems = ["Steel 1/2",
        "Steel 1/4",
        "Steel 3/8",
        "Steel 3/4",
        "Steel 5/16",
        'Steel 1"',
        'Steel 4NO',
        'Steel 8NO',
        'Steel 9NO',
        'Karachi Steel',
        "Plastic",
        "Cement",
        "Tiron",
        "Wending Wire",
        "Garder 7x4",
        "Garder 18LBS",
        "Garder 22LBS",
        "Garder 25LBS",
        ]
# *********************************************************

# *** DROP DOWNS ******************************************

item1 = StringVar()
# item1.set("Item 1")
DropDown1 = OptionMenu(window,item1,*DropDownItems)
DropDown1.place(x=42,y=175)

item2 = StringVar()
# item2.set("Item 2")
DropDown2 = OptionMenu(window,item2,*DropDownItems)
DropDown2.place(x=42,y=227)

item3 = StringVar()
# item3.set("Item 3")
DropDown3 = OptionMenu(window,item3,*DropDownItems)
DropDown3.place(x=42,y=279)

item4 = StringVar()
# item4.set("Item 4")
DropDown4 = OptionMenu(window,item4,*DropDownItems)
DropDown4.place(x=42,y=331)

item5 = StringVar()
# item4.set("Item 4")
DropDown5 = OptionMenu(window,item5,*DropDownItems)
DropDown5.place(x=42,y=383)

item6 = StringVar()
# item4.set("Item 4")
DropDown6 = OptionMenu(window,item6,*DropDownItems)
DropDown6.place(x=42,y=435)

item7 = StringVar()
# item4.set("Item 4")
DropDown7 = OptionMenu(window,item7,*DropDownItems)
DropDown7.place(x=42,y=487)

item8 = Entry(bd=0, bg="#C4C4C4", highlightthickness=0,font="hight=20")
item8.place(x=42, y=537, width=112, height=23)


# *********************************************************

# *** RATE INPUTS *****************************************

rate1 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
rate1.place(x=240, y=175, width=82, height=23)
rate1.insert(0,0)

rate2 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
rate2.place(x=240, y=227, width=82, height=23)
rate2.insert(0,0)

rate3 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
rate3.place(x=240, y=279, width=82, height=23)
rate3.insert(0,0)

rate4 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
rate4.place(x=240, y=331, width=82, height=23)
rate4.insert(0,0)

rate5 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
rate5.place(x=240, y=383, width=82, height=23)
rate5.insert(0,0)

rate6 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
rate6.place(x=240, y=435, width=82, height=23)
rate6.insert(0,0)

rate7 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
rate7.place(x=240, y=487, width=82, height=23)
rate7.insert(0,0)

rate8 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
rate8.place(x=240, y=537, width=82, height=23)
rate8.insert(0,0)

# *********************************************************

# *** WEIGHT INPUTS ***************************************

Weight1 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
Weight1.place(x=354, y=175, width=82, height=23)
Weight1.insert(0,0)

Weight2 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
Weight2.place(x=354, y=227, width=82, height=23)
Weight2.insert(0,0)

Weight3 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
Weight3.place(x=354, y=279, width=82, height=23)
Weight3.insert(0,0)

Weight4 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
Weight4.place(x=354, y=331, width=82, height=23)
Weight4.insert(0,0)

Weight5 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
Weight5.place(x=354, y=383, width=82, height=23)
Weight5.insert(0,0)

Weight6 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
Weight6.place(x=354, y=435, width=82, height=23)
Weight6.insert(0,0)

Weight7 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
Weight7.place(x=354, y=487, width=82, height=23)
Weight7.insert(0,0)

Weight8 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
Weight8.place(x=354, y=537, width=82, height=23)
Weight8.insert(0,0)

# *********************************************************

# *** TOTAL FUNCTION  *************************************



def CalcTotal():
    total1 = Label(text= (int(rate1.get()) * int(Weight1.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
    total1.place(x=460,y=175)

    total2 = Label(text= (int(rate2.get()) * int(Weight2.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
    total2.place(x=460,y=227)

    total3 = Label(text= (int(rate3.get()) * int(Weight3.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
    total3.place(x=460,y=279)

    total4 = Label(text= (int(rate4.get()) * int(Weight4.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
    total4.place(x=460,y=331)

    total5 = Label(text= (int(rate5.get()) * int(Weight5.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
    total5.place(x=460,y=383)

    total6 = Label(text= (int(rate6.get()) * int(Weight6.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
    total6.place(x=460,y=435)

    total7 = Label(text= (int(rate7.get()) * int(Weight7.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
    total7.place(x=460,y=487)

    total8 = Label(text= (int(rate8.get()) * int(Weight8.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
    total8.place(x=460,y=537)
    
    GrandTotal = (float(rate1.get()) * float(Weight1.get()))+(float(rate2.get()) * float(Weight2.get()))+(float(rate3.get()) * float(Weight3.get()))+(float(rate4.get()) * float(Weight4.get()))+(float(rate5.get()) * float(Weight5.get()))+(float(rate6.get()) * float(Weight6.get()))+(float(rate7.get()) * float(Weight7.get()))+(float(rate8.get()) * float(Weight8.get()))+float(Labour.get())+float(Transport.get())+float(OtherAmount.get())

    Grand = Label(text=GrandTotal,padx=10,pady=3,background="#C4C4C4",font="height=10")
    Grand.place(x=662,y=295)

    
# *********************************************************

# *** TOTAL BUTTON ****************************************

TotalButton = Button(window,text="Total",command=CalcTotal,padx=20,pady=5,background="#797766",fg="#ffffff")
TotalButton.place(x=885,y=385)

# *********************************************************

# *** PAYMENT INFO INPUTS *********************************

recived = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
recived.insert(0,0)
recived.place(x=592, y=394, width=178, height=27)

remaning = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
remaning.insert(0,0)
remaning.place(x=592, y=472, width=178, height=27)

dueDate = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
dueDate.place(x=592, y=547, width=178, height=27)


# *********************************************************

# *** DATA SAVEING ****************************************

def SaveData():
    total =((float(rate1.get()) * float(Weight1.get()))+(float(rate2.get()) * float(Weight2.get()))+(float(rate3.get()) * float(Weight3.get()))+(float(rate4.get()) * float(Weight4.get()))+(float(rate5.get()) * float(Weight5.get()))+(float(rate6.get()) * float(Weight6.get()))+(float(rate7.get()) * float(Weight7.get()))+(float(rate8.get()) * float(Weight8.get()))+float(Labour.get())+float(Transport.get())+float(OtherAmount.get()))
    df = pd.DataFrame([[date_time, name.get(),address.get(),
                        phone1.get(),phone2.get(),
                        total,
                        recived.get(),remaning.get(),dueDate.get(),
                        Labour.get(),
                        Transport.get(),
                        OtherAmount.get(),
                        (item1.get(),rate1.get(),Weight1.get()),
                        (item2.get(),rate2.get(),Weight2.get()),
                        (item3.get(),rate3.get(),Weight3.get()),
                        (item4.get(),rate4.get(),Weight4.get()),
                        (item5.get(),rate5.get(),Weight5.get()),
                        (item6.get(),rate6.get(),Weight6.get()),
                        (item7.get(),rate7.get(),Weight7.get()),
                        (item8.get(),rate8.get(),Weight8.get()),
                        ]])
    df.to_csv("customers.csv",mode='a',header=None,index=None)

# *********************************************************


# *** SAVE BUTTON ****************************************

SaveButton = Button(window,text="Save Data",command=SaveData,padx=8,pady=5,background="#797766",fg="#ffffff")
SaveButton.place(x=885,y=461)

# *********************************************************


window.resizable(False, False)
window.mainloop()
