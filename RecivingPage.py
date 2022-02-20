from operator import ge
from tkinter import *
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
background_img = PhotoImage(file = f"Images\\RecivingPage.png")
background = canvas.create_image(
    499, 189,
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
remaning.place(x=500, y=224, width=178, height=27)

recived = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
recived.insert(0,0)
recived.place(x=500, y=286, width=178, height=27)

dueDate = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
dueDate.insert(0,0)
dueDate.place(x=500, y=348, width=178, height=27)

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



# *********************************************************


# *** SEARCH BUTTON ***************************************

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
    # nouser.destroy()

# *********************************************************

# *** SEARCH BUTTON ***************************************
Search = Button(window,text="Search",command=searchfun,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
Search.place(x=355,y=414)
# *********************************************************


# *** CLEAR BUTTON ****************************************
clear = Button(window,text="Clear",command=clearfun,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
clear.place(x=533,y=414)
# *********************************************************

# *** DATE TIME *******************************************

date_time = datetime.datetime.now()
date_ = datetime.date.today()

# *********************************************************

# *** SAVE FUNCTION ***************************************
def SaveData():
    searchfun()
    df = pd.DataFrame([[date_time,date_, name.get(),address.get(),
                            phone1.get(),phone2.get(),0,
                            recived.get(),remaning.get(),dueDate.get(),
                            "Payment Recived",0,0,0,0,0,0,0]])
    df.to_csv("Csv\\customers.csv",mode='a',header=None,index=None)
    window.quit()
# *********************************************************

# *** SAVE BUTTON ****************************************

SaveButton = Button(window,text="Save Data",command=SaveData,padx=20,pady=5,background="#47B759",fg="#ffffff",width=10)
SaveButton.place(x=431,y=514)

# *********************************************************


window.resizable(False, False)
window.mainloop()
