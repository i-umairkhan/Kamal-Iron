from tkinter import *
import datetime
from tkinter import ttk
import pandas as pd
from operator import ge


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

background_img = PhotoImage(file = f"Images\main.png")
background = canvas.create_image(
    499, 300,
    image=background_img)

# *********************************************************
def advance():
    advancePage = Toplevel()

    advancePage.geometry("999x599")
    advancePage.configure(bg = "#ffffff")
    canvas = Canvas(
        advancePage,
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

    name = Entry(advancePage,bd=0, bg="#E5E5E5", highlightthickness=0)
    name.place(x=94, y=72, width=146, height=27)

    address = Entry(advancePage,bd=0, bg="#E5E5E5", highlightthickness=0)
    address.place(x=336, y=72, width=146, height=27)

    phone1 = Entry(advancePage,bd=0, bg="#E5E5E5", highlightthickness=0)
    phone1.place(x=579, y=72, width=146, height=27)

    phone2 = Entry(advancePage,bd=0, bg="#E5E5E5", highlightthickness=0)
    phone2.place(x=827, y=72, width=146, height=27)


    # *********************************************************


    details = Entry(advancePage,bd=0, bg="#E5E5E5", highlightthickness=0,font="height=20")
    details.place(x=216, y=191, width=596, height=176)

    amount = Entry(advancePage,bd=0, bg="#E5E5E5", highlightthickness=0,font="height=20")
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
        advancePage.quit()

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

    SaveButton = Button(advancePage,text="Save Data",command=saving,padx=20,pady=5,background="#47B759",fg="#ffffff",width=10)
    SaveButton.place(x=827,y=522)

    # *********************************************************


    advancePage.resizable(False, False)
    advancePage.mainloop()

advanceButton = Button(window,text="Click",command=advance,padx=20,pady=5,background="#1A3B60",fg="#ffffff",width=10)
advanceButton.place(x=528,y=169)
# *********************************************************

# *********************************************************
def entry():
    entryPage = Toplevel()

    entryPage.geometry("999x599")
    entryPage.configure(bg = "#ffffff")
    # *** CANVAS **********************************************
    canvas = Canvas(
        entryPage,
        bg = "#ffffff",
        height = 599,
        width = 999,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    # *** BACKGROUD IMAGE *************************************
    background_img = PhotoImage(file = f"Images\\CustomerEntry.png")
    background = canvas.create_image(
        499, 294,
        image=background_img)


    # *** DATE TIME *******************************************

    date_time = datetime.datetime.now()
    date_ = datetime.date.today()

    # *********************************************************

    # *** CUSTOMER INFO INPUTS ********************************

    name = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    name.place(x=94, y=69, width=146, height=27)

    address = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    address.place(x=336, y=69, width=146, height=27)

    phone1 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    phone1.place(x=579, y=69, width=146, height=27)

    phone2 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    phone2.place(x=827, y=69, width=146, height=27)


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
            "Labour",
            "Transport"
            ]
    # *********************************************************

    # *** DROP DOWNS ******************************************

    item1 = StringVar()
    # item1.set("Item 1")
    DropDown1 = OptionMenu(entryPage,item1,*DropDownItems)
    DropDown1.place(x=42,y=175)

    item2 = StringVar()
    # item2.set("Item 2")
    DropDown2 = OptionMenu(entryPage,item2,*DropDownItems)
    DropDown2.place(x=42,y=227)

    item3 = StringVar()
    # item3.set("Item 3")
    DropDown3 = OptionMenu(entryPage,item3,*DropDownItems)
    DropDown3.place(x=42,y=279)

    item4 = StringVar()
    # item4.set("Item 4")
    DropDown4 = OptionMenu(entryPage,item4,*DropDownItems)
    DropDown4.place(x=42,y=331)

    item5 = StringVar()
    # item4.set("Item 4")
    DropDown5 = OptionMenu(entryPage,item5,*DropDownItems)
    DropDown5.place(x=42,y=383)

    item6 = StringVar()
    # item4.set("Item 4")
    DropDown6 = OptionMenu(entryPage,item6,*DropDownItems)
    DropDown6.place(x=42,y=435)

    item7 = StringVar()
    # item4.set("Item 4")
    DropDown7 = OptionMenu(entryPage,item7,*DropDownItems)
    DropDown7.place(x=42,y=487)


    item8 = Entry(entryPage,bd=0, bg="#C4C4C4", highlightthickness=0,font="hight=20")
    item8.place(x=42, y=537, width=112, height=23)


    # *********************************************************

    # *** RATE INPUTS *****************************************

    rate1 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate1.place(x=240, y=175, width=82, height=23)
    rate1.insert(0,0)

    rate2 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate2.place(x=240, y=227, width=82, height=23)
    rate2.insert(0,0)

    rate3 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate3.place(x=240, y=279, width=82, height=23)
    rate3.insert(0,0)

    rate4 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate4.place(x=240, y=331, width=82, height=23)
    rate4.insert(0,0)

    rate5 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate5.place(x=240, y=383, width=82, height=23)
    rate5.insert(0,0)

    rate6 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate6.place(x=240, y=435, width=82, height=23)
    rate6.insert(0,0)

    rate7 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate7.place(x=240, y=487, width=82, height=23)
    rate7.insert(0,0)

    rate8 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate8.place(x=240, y=537, width=82, height=23)
    rate8.insert(0,0)

    # *********************************************************

    # *** WEIGHT INPUTS ***************************************

    Weight1 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight1.place(x=354, y=175, width=82, height=23)
    Weight1.insert(0,0)

    Weight2 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight2.place(x=354, y=227, width=82, height=23)
    Weight2.insert(0,0)

    Weight3 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight3.place(x=354, y=279, width=82, height=23)
    Weight3.insert(0,0)

    Weight4 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight4.place(x=354, y=331, width=82, height=23)
    Weight4.insert(0,0)

    Weight5 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight5.place(x=354, y=383, width=82, height=23)
    Weight5.insert(0,0)

    Weight6 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight6.place(x=354, y=435, width=82, height=23)
    Weight6.insert(0,0)

    Weight7 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight7.place(x=354, y=487, width=82, height=23)
    Weight7.insert(0,0)

    Weight8 = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight8.place(x=354, y=537, width=82, height=23)
    Weight8.insert(0,0)

    # *********************************************************

    # *** TOTAL FUNCTION  *************************************
    remaning = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    def CalcTotal():
        total1 = Label(entryPage,text= (int(rate1.get()) * int(Weight1.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total1.place(x=460,y=175)

        total2 = Label(entryPage,text= (int(rate2.get()) * int(Weight2.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total2.place(x=460,y=227)

        total3 = Label(entryPage,text= (int(rate3.get()) * int(Weight3.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total3.place(x=460,y=279)

        total4 = Label(entryPage,text= (int(rate4.get()) * int(Weight4.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total4.place(x=460,y=331)

        total5 = Label(entryPage,text= (int(rate5.get()) * int(Weight5.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total5.place(x=460,y=383)

        total6 = Label(entryPage,text= (int(rate6.get()) * int(Weight6.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total6.place(x=460,y=435)

        total7 = Label(entryPage,text= (int(rate7.get()) * int(Weight7.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total7.place(x=460,y=487)

        total8 = Label(entryPage,text= (int(rate8.get()) * int(Weight8.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total8.place(x=460,y=537)
        
        GrandTotal = (float(rate1.get()) * float(Weight1.get()))+(float(rate2.get()) * float(Weight2.get()))+(float(rate3.get()) * float(Weight3.get()))+(float(rate4.get()) * float(Weight4.get()))+(float(rate5.get()) * float(Weight5.get()))+(float(rate6.get()) * float(Weight6.get()))+(float(rate7.get()) * float(Weight7.get()))+(float(rate8.get()) * float(Weight8.get()))

        Grand = Label(entryPage,text=int(GrandTotal),padx=10,pady=3,background="#C4C4C4",font="height=10")
        Grand.place(x=700,y=305)

        remaning.delete(0,END)
        remaningAmount = float(GrandTotal) - int(recived.get()) + int(CustomerRemaning)
        remaning.insert(0,remaningAmount)
        remaning.place(x=710, y=449, width=178, height=27)

        if(remaningAmount>0):
            clerarAdvance()

        
    # *********************************************************

    # *** TOTAL BUTTON ****************************************

    TotalButton = Button(entryPage,text="Total",command=CalcTotal,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
    TotalButton.place(x=615,y=522)

    # *********************************************************

    # *** PAYMENT INFO INPUTS *********************************

    recived = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    recived.insert(0,0)
    recived.place(x=700, y=377, width=178, height=27)


    dueDate = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    dueDate.insert(0,0)
    dueDate.place(x=855, y=13, width=100, height=27)

    Advance = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Advance.insert(0,0)
    Advance.place(x=700, y=137, width=100, height=27)


    # *********************************************************

    # *** DATA SAVEING ****************************************

    def SaveData():
        total =((float(rate1.get()) * float(Weight1.get()))+(float(rate2.get()) * float(Weight2.get()))+(float(rate3.get()) * float(Weight3.get()))+(float(rate4.get()) * float(Weight4.get()))+(float(rate5.get()) * float(Weight5.get()))+(float(rate6.get()) * float(Weight6.get()))+(float(rate7.get()) * float(Weight7.get()))+(float(rate8.get()) * float(Weight8.get())))
        df = pd.DataFrame([[str(date_time),date_, name.get(),address.get(),
                            phone1.get(),phone2.get(),
                            total,
                            recived.get(),remaning.get(),str(dueDate.get()),
                            (item1.get(),Weight1.get(),rate1.get()),
                            (item2.get(),Weight2.get(),rate2.get()),
                            (item3.get(),Weight3.get(),rate3.get()),
                            (item4.get(),Weight4.get(),rate4.get()),
                            (item5.get(),Weight5.get(),rate5.get()),
                            (item6.get(),Weight6.get(),rate6.get()),
                            (item7.get(),Weight7.get(),rate7.get()),
                            (item8.get(),Weight8.get(),rate8.get()),
                            ]])
        df.to_csv("Csv\\customers.csv",mode='a',header=None,index=None)

        df2 = pd.DataFrame([[str(date_time),date_, name.get(),address.get(),
                            phone1.get(),phone2.get(),
                            details.get(),Advance.get()
                            ]])
        df2.to_csv("Csv\\advance.csv",mode='a',header=None,index=None)
        entryPage.quit()

    # *********************************************************


    # *** SAVE BUTTON ****************************************

    SaveButton = Button(entryPage,text="Save Data",command=SaveData,padx=20,pady=5,background="#47B759",fg="#ffffff",width=10)
    SaveButton.place(x=827,y=522)

    # *********************************************************

    # *** SEARCH FUNCTION *************************************

    def searchfun():
        df = pd.read_csv("Csv\\customers.csv")
        df = pd.DataFrame(df)
        df.sort_values(['DateTime'],ascending=False,inplace=True)
        for i in range(len(df)):
            if(df.loc[i,"Name"]==name.get()):
                df = pd.DataFrame(df[df["Name"]==name.get()])
                global CustomerRemaning
                CustomerRemaning = int(df.iloc[0,8])
                CustomerAddress = df.iloc[0,3]
                CustomerPhone1 = int(df.iloc[0,4])
                CustomerPhone2 = (df.iloc[0,5])
                remaning.delete(0,END)
                remaning.insert(0,CustomerRemaning)
                address.delete(0,END)
                address.insert(0,CustomerAddress)
                phone1.delete(0,END)
                phone1.insert(0,CustomerPhone1)
                phone2.delete(0,END)
                phone2.insert(0,(CustomerPhone2))
                break
            else:
                CustomerRemaning = 0
                address.delete(0,END)
                phone1.delete(0,END)
                phone2.delete(0,END)




    def searchfun2():
        global customerAdvance , customerAdvanceDetails,details
        df = pd.read_csv("Csv\\advance.csv")
        df = pd.DataFrame(df)
        df.sort_values(['DateTime'],ascending=False,inplace=True)
        for i in range(len(df)):
            if(df.loc[i,"Name"]==name.get()):
                df = pd.DataFrame(df[df["Name"]==name.get()])
                customerAdvance = int(df.iloc[0,7])
                customerAdvanceDetails = (df.iloc[0,6])
                Advance.delete(0,END)
                Advance.insert(0,(customerAdvance))
                details = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
                details.insert(0,customerAdvanceDetails)
                details.place(x=593,y=176, width=350, height=27)
                global CustomerRemaning
                CustomerAddress = df.iloc[0,3]
                CustomerPhone1 = int(df.iloc[0,4])
                CustomerPhone2 = (df.iloc[0,5])
                address.delete(0,END)
                address.insert(0,CustomerAddress)
                phone1.delete(0,END)
                phone1.insert(0,CustomerPhone1)
                phone2.delete(0,END)
                phone2.insert(0,(CustomerPhone2))
                break
            else:
                customerAdvance = 0
                customerAdvanceDetails = " "
                Advance.delete(0,END)
                Advance.insert(0,(customerAdvance))
                details = Entry(entryPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
                details.insert(0,0)
                details.place(x=593,y=176, width=100, height=27)
                address.delete(0,END)
                phone1.delete(0,END)
                phone2.delete(0,END)
        


    # *********************************************************



    def clerarAdvance():
                customerAdvance = 0
                details.delete(0,END)
                Advance.delete(0,END)
                Advance.insert(0,0)


    clr = Button(entryPage,text="Clear Advance",command=clerarAdvance,padx=20,pady=5,background="#47B759",fg="#ffffff",width=5)
    clr.place(x=885,y=241)


    # *********************************************************

    def searching():
            searchfun()
            searchfun2()


    clr = Button(entryPage,text="🔍",command=searching,padx=0,pady=1,background="#47B759",fg="#ffffff",width=5)
    clr.place(x=204,y=69)

    # *********************************************************





    entryPage.resizable(False, False)
    entryPage.mainloop()

EntryButton = Button(window,text="Click",command=entry,padx=20,pady=5,background="#1A3B60",fg="#ffffff",width=10)
EntryButton.place(x=528,y=235)

# *********************************************************

# *********************************************************

def reciving():
    recivingPage = Toplevel()

    recivingPage.geometry("999x599")
    recivingPage.configure(bg = "#ffffff")
    # *** CANVAS **********************************************
    canvas = Canvas(
        recivingPage,
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
    name = Entry(recivingPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    name.place(x=94, y=69, width=146, height=27)

    address = Entry(recivingPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    address.place(x=336, y=69, width=146, height=27)

    phone1 = Entry(recivingPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    phone1.place(x=579, y=69, width=146, height=27)

    phone2 = Entry(recivingPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    phone2.place(x=827, y=69, width=146, height=27)

    remaning = Entry(recivingPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    remaning.insert(0,0)
    remaning.place(x=500, y=224, width=178, height=27)

    recived = Entry(recivingPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    recived.insert(0,0)
    recived.place(x=500, y=286, width=178, height=27)

    dueDate = Entry(recivingPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
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
        nouser = Label(recivingPage,recivingPage,text= "NO RECORD FOUND TRY AGAIN",background="#FF0000",font="height=20")
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
    Search = Button(recivingPage,text="Search",command=searchfun,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
    Search.place(x=355,y=414)
    # *********************************************************


    # *** CLEAR BUTTON ****************************************
    clear = Button(recivingPage,text="Clear",command=clearfun,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
    clear.place(x=533,y=414)
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
                                "Payment Recived",0,0,0,0,0,0,0]])
        df.to_csv("Csv\\customers.csv",mode='a',header=None,index=None)
        
        df2 = pd.DataFrame([[str(date_time),date_, name.get(),address.get(),
                            phone1.get(),phone2.get(),
                            " ",0
                            ]])
        df2.to_csv("Csv\\advance.csv",mode='a',header=None,index=None)
        recivingPage.quit()
    # *********************************************************

    # *** SAVE BUTTON ****************************************

    SaveButton = Button(recivingPage,text="Save Data",command=SaveData,padx=20,pady=5,background="#47B759",fg="#ffffff",width=10)
    SaveButton.place(x=431,y=514)

    # *********************************************************


    recivingPage.resizable(False, False)
    recivingPage.mainloop()

RecivingButton = Button(window,text="Click",command=reciving,padx=20,pady=5,background="#1A3B60",fg="#ffffff",width=10)
RecivingButton.place(x=528,y=301)

# *********************************************************

# *********************************************************

def returning():
    returnPage = Toplevel()

    returnPage.geometry("999x599")
    returnPage.configure(bg = "#ffffff")
    canvas = Canvas(
        returnPage,
        bg = "#ffffff",
        height = 599,
        width = 999,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Images\\Returning.png")
    background = canvas.create_image(
        499, 294,
        image=background_img)



    # *** CUSTOMER INFO INPUTS ********************************

    name = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    name.place(x=94, y=69, width=146, height=27)

    address = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    address.place(x=336, y=69, width=146, height=27)

    phone1 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    phone1.place(x=579, y=69, width=146, height=27)

    phone2 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    phone2.place(x=827, y=69, width=146, height=27)


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
            "Garder 25LBS"
            ]
    # *********************************************************


    # *** DROP DOWNS ******************************************

    item1 = StringVar()
    # item1.set("Item 1")
    DropDown1 = OptionMenu(returnPage,item1,*DropDownItems)
    DropDown1.place(x=42,y=175)

    item2 = StringVar()
    # item2.set("Item 2")
    DropDown2 = OptionMenu(returnPage,item2,*DropDownItems)
    DropDown2.place(x=42,y=227)

    item3 = StringVar()
    # item3.set("Item 3")
    DropDown3 = OptionMenu(returnPage,item3,*DropDownItems)
    DropDown3.place(x=42,y=279)

    item4 = StringVar()
    # item4.set("Item 4")
    DropDown4 = OptionMenu(returnPage,item4,*DropDownItems)
    DropDown4.place(x=42,y=331)

    item5 = StringVar()
    # item4.set("Item 4")
    DropDown5 = OptionMenu(returnPage,item5,*DropDownItems)
    DropDown5.place(x=42,y=383)

    item6 = StringVar()
    # item4.set("Item 4")
    DropDown6 = OptionMenu(returnPage,item6,*DropDownItems)
    DropDown6.place(x=42,y=435)

    item7 = StringVar()
    # item4.set("Item 4")
    DropDown7 = OptionMenu(returnPage,item7,*DropDownItems)
    DropDown7.place(x=42,y=487)


    item8 = Entry(returnPage,bd=0, bg="#C4C4C4", highlightthickness=0,font="hight=20")
    item8.place(x=42, y=537, width=112, height=23)


    # *********************************************************

    # *** RATE INPUTS *****************************************

    rate1 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate1.place(x=240, y=175, width=82, height=23)
    rate1.insert(0,0)

    rate2 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate2.place(x=240, y=227, width=82, height=23)
    rate2.insert(0,0)

    rate3 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate3.place(x=240, y=279, width=82, height=23)
    rate3.insert(0,0)

    rate4 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate4.place(x=240, y=331, width=82, height=23)
    rate4.insert(0,0)

    rate5 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate5.place(x=240, y=383, width=82, height=23)
    rate5.insert(0,0)

    rate6 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate6.place(x=240, y=435, width=82, height=23)
    rate6.insert(0,0)

    rate7 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate7.place(x=240, y=487, width=82, height=23)
    rate7.insert(0,0)

    rate8 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    rate8.place(x=240, y=537, width=82, height=23)
    rate8.insert(0,0)

    # *********************************************************

    # *** WEIGHT INPUTS ***************************************

    Weight1 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight1.place(x=354, y=175, width=82, height=23)
    Weight1.insert(0,0)

    Weight2 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight2.place(x=354, y=227, width=82, height=23)
    Weight2.insert(0,0)

    Weight3 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight3.place(x=354, y=279, width=82, height=23)
    Weight3.insert(0,0)

    Weight4 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight4.place(x=354, y=331, width=82, height=23)
    Weight4.insert(0,0)

    Weight5 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight5.place(x=354, y=383, width=82, height=23)
    Weight5.insert(0,0)

    Weight6 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight6.place(x=354, y=435, width=82, height=23)
    Weight6.insert(0,0)

    Weight7 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight7.place(x=354, y=487, width=82, height=23)
    Weight7.insert(0,0)

    Weight8 = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    Weight8.place(x=354, y=537, width=82, height=23)
    Weight8.insert(0,0)

    # *********************************************************
    remaning = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    def CalcTotal():
        searchfun()
        total1 = Label(returnPage,text= (int(rate1.get()) * int(Weight1.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total1.place(x=460,y=175)

        total2 = Label(returnPage,text= (int(rate2.get()) * int(Weight2.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total2.place(x=460,y=227)

        total3 = Label(returnPage,text= (int(rate3.get()) * int(Weight3.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total3.place(x=460,y=279)

        total4 = Label(returnPage,text= (int(rate4.get()) * int(Weight4.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total4.place(x=460,y=331)

        total5 = Label(returnPage,text= (int(rate5.get()) * int(Weight5.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total5.place(x=460,y=383)

        total6 = Label(returnPage,text= (int(rate6.get()) * int(Weight6.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total6.place(x=460,y=435)

        total7 = Label(returnPage,text= (int(rate7.get()) * int(Weight7.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total7.place(x=460,y=487)

        total8 = Label(returnPage,text= (int(rate8.get()) * int(Weight8.get()) ),padx=10,pady=3,background="#C4C4C4",font="height=20")
        total8.place(x=460,y=537)
        
        GrandTotal = (float(rate1.get()) * float(Weight1.get()))+(float(rate2.get()) * float(Weight2.get()))+(float(rate3.get()) * float(Weight3.get()))+(float(rate4.get()) * float(Weight4.get()))+(float(rate5.get()) * float(Weight5.get()))+(float(rate6.get()) * float(Weight6.get()))+(float(rate7.get()) * float(Weight7.get()))+(float(rate8.get()) * float(Weight8.get())) - (float(labour.get())+float(transport.get()))

        Grand = Label(returnPage,text=int(GrandTotal),padx=10,pady=3,background="#C4C4C4",font="height=10")
        Grand.place(x=665,y=267)

        remaningAmount = int(remaning.get()) - int(GrandTotal) + int(paid.get())
        remaning.delete(0,END)
        remaning.insert(0,remaningAmount)


    # *********************************************************


        
    paid = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    paid.insert(0,0)
    paid.place(x=716, y=417, width=178, height=27)

    labour = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    labour.insert(0,0)
    labour.place(x=716, y=137, width=178, height=27)


    transport = Entry(returnPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    transport.insert(0,0)
    transport.place(x=716, y=182, width=178, height=27)

    # *** TOTAL BUTTON ****************************************

    TotalButton = Button(returnPage,text="Total",command=CalcTotal,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
    TotalButton.place(x=615,y=522)

    # *********************************************************

    # *** SEARCH FUNCTION *************************************

    def searchfun():
        df = pd.read_csv("Csv\\customers.csv")
        df = pd.DataFrame(df)
        df.sort_values(['DateTime'],ascending=False,inplace=True)
        for i in range(len(df)):
            if(df.loc[i,"Name"]==name.get()):
                df = pd.DataFrame(df[df["Name"]==name.get()])
                global CustomerRemaning
                CustomerRemaning = int(df.iloc[0,8])
                CustomerAddress = df.iloc[0,3]
                CustomerPhone1 = int(df.iloc[0,4])
                CustomerPhone2 = (df.iloc[0,5])
                remaning.delete(0,END)
                remaning.insert(0,CustomerRemaning)
                address.delete(0,END)
                address.insert(0,CustomerAddress)
                phone1.delete(0,END)
                phone1.insert(0,CustomerPhone1)
                phone2.delete(0,END)
                phone2.insert(0,(CustomerPhone2))
                break
            else:
                CustomerRemaning = 0
                address.delete(0,END)
                phone1.delete(0,END)
                phone2.delete(0,END)
        remaning.delete(0,END)
        remaning.insert(0,CustomerRemaning)
        remaning.place(x=716, y=341, width=178, height=27)



    # *********************************************************

    def searching():
            searchfun()


    searchbtn = Button(returnPage,text="🔍",command=searching,padx=0,pady=1,background="#47B759",fg="#ffffff",width=5)
    searchbtn.place(x=204,y=69)

    # *********************************************************




    # *** DATE TIME *******************************************

    date_time = datetime.datetime.now()
    date_ = datetime.date.today()

    # *********************************************************


    # *** DATA SAVEING ****************************************

    def SaveData():
        total =((float(rate1.get()) * float(Weight1.get()))+(float(rate2.get()) * float(Weight2.get()))+(float(rate3.get()) * float(Weight3.get()))+(float(rate4.get()) * float(Weight4.get()))+(float(rate5.get()) * float(Weight5.get()))+(float(rate6.get()) * float(Weight6.get()))+(float(rate7.get()) * float(Weight7.get()))+(float(rate8.get()) * float(Weight8.get())))
        df = pd.DataFrame([[str(date_time),date_, name.get(),address.get(),
                            phone1.get(),phone2.get(),
                            total,
                            paid.get(),remaning.get(),0,
                            ("Returning",item1.get(),Weight1.get(),rate1.get()),
                            (item2.get(),Weight2.get(),rate2.get()),
                            (item3.get(),Weight3.get(),rate3.get()),
                            (item4.get(),Weight4.get(),rate4.get()),
                            (item5.get(),Weight5.get(),rate5.get()),
                            (item6.get(),Weight6.get(),rate6.get()),
                            (item7.get(),Weight7.get(),rate7.get()),
                            (item8.get(),Weight8.get(),rate8.get()),
                            ]])
        df.to_csv("Csv\\customers.csv",mode='a',header=None,index=None)
        
        df2 = pd.DataFrame([[str(date_time),date_, name.get(),address.get(),
                            phone1.get(),phone2.get(),
                            " ",0
                            ]])
        df2.to_csv("Csv\\advance.csv",mode='a',header=None,index=None)
        returnPage.quit()

    # *********************************************************




    # *** SAVE BUTTON ****************************************

    SaveButton = Button(returnPage,text="Save Data",command=SaveData,padx=20,pady=5,background="#47B759",fg="#ffffff",width=10)
    SaveButton.place(x=827,y=522)

    # *********************************************************

    returnPage.resizable(False, False)
    returnPage.mainloop()

ReturningButton = Button(window,text="Click",command=returning,padx=20,pady=5,background="#1A3B60",fg="#ffffff",width=10)
ReturningButton.place(x=528,y=366)

# *********************************************************

# *********************************************************

def mill():
    
    millPage = Toplevel()

    millPage.geometry("999x599")
    millPage.configure(bg = "#ffffff")
    canvas = Canvas(
        millPage,
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
    name = Entry(millPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    name.place(x=94, y=69, width=146, height=27)

    address = Entry(millPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    address.place(x=336, y=69, width=146, height=27)

    phone1 = Entry(millPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    phone1.place(x=579, y=69, width=146, height=27)

    phone2 = Entry(millPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    phone2.place(x=827, y=69, width=146, height=27)

    remaning = Entry(millPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    remaning.insert(0,0)
    remaning.place(x=249, y=184, width=178, height=27)

    recived = Entry(millPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
    recived.insert(0,0)
    recived.place(x=249, y=246, width=178, height=27)

    dueDate = Entry(millPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
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
        nouser = Label(millPage,text= "NO RECORD FOUND TRY AGAIN",background="#FF0000",font="height=20")
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
        Mnouser = Label(millPage,text= "NO RECORD FOUND TRY AGAIN",background="#FF0000",font="height=20")
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
    clear = Button(millPage,text="Clear",command=clearfun,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
    clear.place(x=289,y=428)
    # *********************************************************

    # *** CLEAR BUTTON ****************************************
    clear = Button(millPage,text="Clear",command=clearfunMill,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
    clear.place(x=797,y=428)
    # *********************************************************




    # *** SEARCH BUTTON ***************************************
    Search = Button(millPage,text="Search",command=searchfun,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
    Search.place(x=56,y=428)
    # *********************************************************

    # *** SEARCH BUTTON ***************************************
    SearchM = Button(millPage,text="Search",command=searchfunMill,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
    SearchM.place(x=592,y=428)
    # *********************************************************



    # *** MILL INFO INPUTS ************************************
    Mname = Entry(millPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    Mname.place(x=700, y=185, width=146, height=27)

    Maddress = Entry(millPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    Maddress.place(x=700, y=238, width=146, height=27)

    Mphone1 = Entry(millPage,bd=0, bg="#E5E5E5", highlightthickness=0)
    Mphone1.place(x=700, y=291, width=146, height=27)

    Mremaning = Entry(millPage,bd=0, bg="#E5E5E5", highlightthickness=0,font="hight=20")
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
    transferAmount = Button(millPage,text="Transfer",command=transfer,padx=20,pady=5,background="#db5353",fg="#ffffff",width=10)
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

        millPage.quit()
    # *********************************************************




    # *** SAVE BUTTON ****************************************

    SaveButton = Button(millPage,text="Save Data",command=SaveData,padx=20,pady=5,background="#47B759",fg="#ffffff",width=10)
    SaveButton.place(x=460,y=540)

    # *********************************************************


    millPage.resizable(False, False)
    millPage.mainloop()


MillButton = Button(window,text="Click",command=mill,padx=20,pady=5,background="#1A3B60",fg="#ffffff",width=10)
MillButton.place(x=528,y=433)

# *********************************************************

# *********************************************************

def records():
    recordPage = Toplevel()

    recordPage.geometry("999x599")
    recordPage.configure(bg = "#ffffff")
    # *** CANVAS **********************************************
    canvas = Canvas(
        recordPage,
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
    name = Entry(recordPage,bd=0, bg="#C4C4C4", highlightthickness=0)
    name.place(x=493, y=70, width=213, height=28)
    # *********************************************************

    # *** TREE VIWE *******************************************
    s = ttk.Style()
    s.theme_use('classic')
    s.configure('Treeview.Heading', background="#E5E5E5")
    tree=ttk.Treeview(recordPage,height=21)
    vsb = ttk.Scrollbar(recordPage, orient="vertical", command=tree.yview)
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
        nouser = Label(recordPage,text= "",background="#ffffff",font="height=20")
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
    SearchButton = Button(recordPage,text="Search",command=showname,padx=8,pady=5,background="#47B759",fg="#ffffff")
    SearchButton.place(x=733,y=70)
    ClearButton = Button(recordPage,text="Clear",command=clearfun,padx=8,pady=5,background="#db5353",fg="#ffffff")
    ClearButton.place(x=814,y=70)
    # *********************************************************


    recordPage.resizable(False, False)
    recordPage.mainloop()

recordButton = Button(window,text="Click",command=records,padx=20,pady=5,background="#1A3B60",fg="#ffffff",width=10)
recordButton.place(x=528,y=498)

# *********************************************************



window.resizable(False, False)
window.mainloop()
