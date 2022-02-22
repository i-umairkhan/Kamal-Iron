import datetime
from tkinter import *

import pandas as pd

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

background_img = PhotoImage(file = f"Images\\mills.png")
background = canvas.create_image(
    499, 194,
    image=background_img)




# *** CUSTOMER INFO INPUTS ********************************
name = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
name.place(x=94, y=69, width=146, height=27)

address = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
address.place(x=336, y=69, width=146, height=27)

phone1 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
phone1.place(x=579, y=69, width=146, height=27)

phone2 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
phone2.place(x=827, y=69, width=146, height=27)

remaning = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
remaning.insert(0,0)
remaning.place(x=249, y=184, width=178, height=27)

recived = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
recived.insert(0,0)
recived.place(x=249, y=246, width=178, height=27)

dueDate = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
dueDate.insert(0,0)
dueDate.place(x=249, y=308, width=178, height=27)

# *********************************************************




# *** SEARCH FUNCTION *************************************
def searchfun():
    df = pd.read_csv("Csv\\customers.csv")
    df = pd.DataFrame(df)
    df.sort_values(['DateTime'],ascending=False,inplace=True)
    for i in range(len(df)):
        if(df.loc[i,"Name"]==name.get()):
            df = pd.DataFrame(df[df["Name"]==name.get()])
            CustomerRemaning = int(df.iloc[0,8])
            CustomerName = df.iloc[0,2]
            CustomerAddress = df.iloc[0,3]
            CustomerPhone1 = int(df.iloc[0,4])
            CustomerPhone2 = (df.iloc[0,5])
            remaning.delete(0,END)
            address.delete(0,END)
            address.insert(0,CustomerAddress)
            phone1.delete(0,END)
            phone1.insert(0,CustomerPhone1)
            phone2.delete(0,END)
            phone2.insert(0,(CustomerPhone2))
            break
    global nouser
    nouser = Label(window,text= "NO RECORD FOUND TRY AGAIN",background="#FF0000",font="height=20")
    if(df.loc[i,"Name"]!=name.get()):
        CustomerName = " "
        nouser.place(x=414,y=383)
        remaning.delete(0,END)
        CustomerRemaning = 0
    AmountRemaning =  CustomerRemaning - int(recived.get())
    remaning.insert(0,AmountRemaning)


def searchfunMill():
    df = pd.read_csv("Csv\\customers.csv")
    df = pd.DataFrame(df)
    df.sort_values(['DateTime'],ascending=False,inplace=True)
    for i in range(len(df)):
        if(df.loc[i,"Name"]==Mname.get()):
            df = pd.DataFrame(df[df["Name"]==Mname.get()])
            CustomerRemaning = int(df.iloc[0,8])
            CustomerName = df.iloc[0,2]
            CustomerAddress = df.iloc[0,3]
            CustomerPhone1 = int(df.iloc[0,4])
            Mremaning.delete(0,END)
            Maddress.delete(0,END)
            Maddress.insert(0,CustomerAddress)
            Mphone1.delete(0,END)
            Mphone1.insert(0,CustomerPhone1)
            break
    global Mnouser
    Mnouser = Label(window,text= "NO RECORD FOUND TRY AGAIN",background="#FF0000",font="height=20")
    if(df.loc[i,"Name"]!=Mname.get()):
        CustomerName = " "
        Mnouser.place(x=414,y=383)
        Mremaning.delete(0,END)
        CustomerRemaning = 0
    Mremaning.insert(0,CustomerRemaning)




def clearfun():
    name.delete(0,END)
    address.delete(0,END)
    phone1.delete(0,END)
    phone2.delete(0,END)
    recived.delete(0,END)
    remaning.delete(0,END)
    dueDate.delete(0,END)
    nouser.destroy()
    recived.insert(0,0)
    remaning.insert(0,0)
    dueDate.insert(0,0)

def clearfunMill():
    Mname.delete(0,END)
    Maddress.delete(0,END)
    Mphone1.delete(0,END)
    Mremaning.delete(0,END)
    Mnouser.destroy()
    Mremaning.insert(0,0)



# *** CLEAR BUTTON ****************************************
clear = Button(window,text="Clear",command=clearfun,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
clear.place(x=289,y=428)
# *********************************************************

# *** CLEAR BUTTON ****************************************
clear = Button(window,text="Clear",command=clearfunMill,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
clear.place(x=797,y=428)
# *********************************************************




# *** SEARCH BUTTON ***************************************
Search = Button(window,text="Search",command=searchfun,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
Search.place(x=56,y=428)
# *********************************************************

# *** SEARCH BUTTON ***************************************
SearchM = Button(window,text="Search",command=searchfunMill,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
SearchM.place(x=592,y=428)
# *********************************************************



# *** MILL INFO INPUTS ************************************
Mname = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
Mname.place(x=700, y=185, width=146, height=27)

Maddress = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
Maddress.place(x=700, y=238, width=146, height=27)

Mphone1 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
Mphone1.place(x=700, y=291, width=146, height=27)

Mremaning = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
Mremaning.insert(0,0)
Mremaning.place(x=700, y=345, width=146, height=27)

# *********************************************************


def transfer():
    amount = int(Mremaning.get()) - int(recived.get())
    Mremaning.delete(0,END)
    Mremaning.insert(0,amount)
    # recived.delete(0,END)
    # recived.insert(0,0)


# *** SEARCH BUTTON ***************************************
transferAmount = Button(window,text="Transfer",command=transfer,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
transferAmount.place(x=460,y=456)
# *********************************************************


# *** DATE TIME *******************************************

date_time = datetime.datetime.now()
date_ = datetime.date.today()

# *********************************************************

# *** SAVE FUNCTION ***************************************
def SaveData():
    df = pd.DataFrame([[date_time,date_, name.get(),address.get(),
                            phone1.get(),phone2.get(),0,
                            recived.get(),remaning.get(),dueDate.get(),
                            ("Payment Sent to " + Mname.get()),0,0,0,0,0,0,0]])
    df.to_csv("Csv\\customers.csv",mode='a',header=None,index=None)

    df2 = pd.DataFrame([[date_time,date_, Mname.get(),Maddress.get(),
                            Mphone1.get(),0,0,
                            0,Mremaning.get(),0,
                            ("Payment Sent by " + name.get()),0,0,0,0,0,0,0]])
    df2.to_csv("Csv\\customers.csv",mode='a',header=None,index=None)
        
    df3 = pd.DataFrame([[str(date_time),date_, name.get(),address.get(),
                        phone1.get(),phone2.get(),
                        " ",0
                        ]])
    df3.to_csv("Csv\\advance.csv",mode='a',header=None,index=None)
        
    df4 = pd.DataFrame([[str(date_time),date_, Mname.get(),Maddress.get(),
                        Mphone1.get(),0,
                        " ",0
                        ]])
    df4.to_csv("Csv\\advance.csv",mode='a',header=None,index=None)

    window.quit()
# *********************************************************




# *** SAVE BUTTON ****************************************

SaveButton = Button(window,text="Save Data",command=SaveData,padx=20,pady=5,background="#47B759",fg="#ffffff",width=10)
SaveButton.place(x=460,y=540)

# *********************************************************


window.resizable(False, False)
window.mainloop()
