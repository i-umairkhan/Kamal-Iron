from tkinter import *
import datetime
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

background_img = PhotoImage(file = f"Images\\advance.png")
background = canvas.create_image(
    499, 219,
    image=background_img)

# *** CUSTOMER INFO INPUTS ********************************

name = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
name.place(x=94, y=72, width=146, height=27)

address = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
address.place(x=336, y=72, width=146, height=27)

phone1 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
phone1.place(x=579, y=72, width=146, height=27)

phone2 = Entry(bd=0, bg="#E5E5E5", highlightthickness=0)
phone2.place(x=827, y=72, width=146, height=27)


# *********************************************************


details = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="height=20")
details.place(x=216, y=191, width=596, height=176)

amount = Entry(bd=0, bg="#E5E5E5", highlightthickness=0,font="height=20")
amount.place(x=496, y=403, width=177, height=30)


# *********************************************************


# *** DATE TIME *******************************************

date_time = datetime.datetime.now()
date_ = datetime.date.today()

# *********************************************************



# *** DATA SAVEING ****************************************

def SaveData():

    df = pd.DataFrame([[date_time,date_, name.get(),address.get(),
                        phone1.get(),phone2.get(),
                        details.get(),amount.get()
                        ]])
    df.to_csv("Csv\\advance.csv",mode='a',header=None,index=None)
    window.quit()

def SaveData2():
    df2 = pd.DataFrame([[str(date_time),date_, name.get(),address.get(),
                        phone1.get(),phone2.get(),0,0,-abs(int(amount.get())),0
                        ,0,0,0,0,0,0,0,0
                        ]])
    df2.to_csv("Csv\\customers.csv",mode='a',header=None,index=None)

# *********************************************************
def saving():
    SaveData()
    SaveData2()


# *** SAVE BUTTON ****************************************

SaveButton = Button(window,text="Save Data",command=saving,padx=20,pady=5,background="#47B759",fg="#ffffff",width=10)
SaveButton.place(x=827,y=522)

# *********************************************************


window.resizable(False, False)
window.mainloop()
