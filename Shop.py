import sqlite3
from tkinter import *
from tkinter import filedialog
import time
import random
import RSYSS
import Till
from functools import partial
import sys
import xlsxwriter
from prettytable import PrettyTable
import os
import tempfile
import SETUP
import webbrowser
from idle_time import IdleMonitor
from tkinter import messagebox
import Error
from datetime import datetime, timedelta


#not Built In
from openpyxl import Workbook
from openpyxl import load_workbook

x = PrettyTable()


button_1 = "Beers & Ciders"
button_2 = "wine/per Glass"
button_3 = "Soft Drinks"
button_4 = "Gin"
button_5 = "Spirits"
button_6 = "Whiskey"
button_7 = "Brandy"



try:
    filepath="CRJ.xlsx"
    # load demo.xlsx 
    wb=load_workbook(filepath)
    Previous_Value = 1
except:
    # set file path
    filepath="CRJ.xlsx"
    # load demo.xlsx
    wb=Workbook()
    # save workbook 
    wb.save(filepath)
    Previous_Value = 1


##a1 = (row[0])
##b1 = 14 - (len(a))
##print (a1 + (" " * b1) + "|")

SET = SETUP

GEN = RSYSS
GEN.Config1()



TimeDate = (time.strftime("%H:%M--%d/%m/%Y"))

DEF1 = "0000"

NAME1 = "Admin"
PASS1 = "99562281"
NAME2 = "Cashier 1"
PASS2 = DEF1
NAME3 = "Cashier 2"
PASS3 = DEF1
Time2 = (time.strftime("%H:%M"))
DATE = (time.strftime("%m-%Y"))

print (time.strftime("%H:%M"))
print (time.strftime("%d/%m/%Y"))
print (random.randint(1,1000000000))

conn = sqlite3.connect('Shop_Database.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS CRJ(ID REAL,Date REAL, Description TEXT, Amount RAEL, Bank RAEL, Item TEXT, QTY TEXT, Payment_Type TEXT, Cashier TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS Product_List(Code INT, Price REAL, Item TEXT, Cost_Price REAL)''')
c.execute('''CREATE TABLE IF NOT EXISTS Customer_List(Code REAL, Name TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS MenuS(Menu_Name TEXT, Menu_Number RAEL)''')



##try:
##    c.execute("SELECT * FROM Settings")
##    for row in c.fetchall():
####        print("H")
##        pass
##except:
##    SET.FIRSTTIME()

##Bbb1 = "1"
##Bbb2 = "1"
##Bbb3 = "1"
##c.execute('''INSERT INTO CRJ(PLU, Name, Price) VALUES(?, ? ,?)''',(Bbb1, Bbb2, Bbb3))
##conn.commit()


c.execute("SELECT * FROM Starters")
for row in c.fetchall():
    print(row)




print ("=" * 70)

AZ = PrettyTable()

c.execute("SELECT * FROM Product_List")
#DA22 = c.fetchall()
for row in c.fetchall():
    print(row)
    AZ.field_names = ["ID", "Price", "Name", "Cost Price"]
    E = (row)
    AZ.add_row((E))

print(AZ)

global LEVL

LEVL = 1


def FTW():
    c.execute('''DROP TABLE Settings''')
    conn.commit()
    SET.FIRSTTIME()

def LEV1():
    global LEVL
    LEVL = 1
    RUN1()

def LEV2():
    global LEVL
    LEVL = 2
    RUN1()

def LEV3():
    global LEVL
    LEVL = 3
    RUN1()



def RUN1():
    Page1 = Tk()
    Page1.title("Shop Database")
    Page1.configure(background="cadet blue")
    Page1.attributes("-fullscreen", True)
    Page1.iconbitmap('Till.ico')


#=========================================================#Add_User#==================================================================

    def Add_User():
        Add_user = Tk()
        Add_user.title("Shop Database")
        Add_user.configure(background="cadet blue")
        Add_user.attributes("-fullscreen", True)

        Label(Add_user, text="Name", bd=2).place(x=1,y=1)
        User_Name = Entry(Add_user, bd=2)
        User_Name.place(x=100,y=1)
        
        def Commit_user():
            if len(User_Name) <= 0:
                MsgBox_004 = messagebox.showerror ('ERROR',Error.Error_004,icon = Error.Error_icon)
            elif len(User_Password) <= 0:
                MsgBox_005 = messagebox.showerror ('ERROR',Error.Error_005,icon = Error.Error_icon)
            elif User_Role == None:
                MsgBox_006 = messagebox.showerror ('ERROR',Error.Error_006,icon = Error.Error_icon)
            else:
                Till.add_account("Name","1234",2)

#=========================================================#Remove_User#==================================================================



#=========================================================#Add_To_Scale#==================================================================



#=========================================================#Remove_from_scale#==================================================================



#=========================================================#Sales Info#==================================================================



#=========================================================#TicketSYS#==================================================================


    def TicketSYS():
        TS = Tk()
        TS.title("Shop Database")
        TS.geometry("1980x1080")

        def OCSV():
            filedialog.askopenfilename(initialdir = "/",title = "select file",filetypes = (("CSV files",".csv"),("all files",".")))

            

        def DN():
            pass

##        F9 = Frame(TS, width=150, height=30, bd=2, bg="light grey", relief="raise")
##        F9.place(x=1,y=1)

        menubar = Menu(TS)
        filemenu = Menu(menubar, tearoff=0)

        filemenu.add_command(label="Open csv", command=OCSV)
        filemenu.add_command(label="New", command=DN)
        filemenu.add_command(label="Open", command=DN)
        filemenu.add_command(label="Close", command=DN)

        filemenu.add_separator()
        menubar.add_cascade(label="File", menu=filemenu)


        TS.configure(background="cadet blue", menu=menubar)



#=========================================================#Help#==================================================================

    def Help():
##        top = Tk()
##        top.title("Shop Database")
##        top.configure(background="cadet blue")
##        top.geometry("1980x1080")

        
        new = 2 # open in a new tab, if possible



        ## open an HTML file on my own (Windows) computer
    
        webbrowser.open("file://C:/Users/conno/OneDrive/Desktop/Shop/Help page/Website.html",new=new)
##        webbrowser.open("file://C:/Users/conno/OneDrive/Desktop/Shop/Python totaurials.docx",new=new)


    

#=========================================================#restorant items#===========================================================

    def Add_Menu1():
        PageAM = Tk()
        PageAM.title("Shop Database")
        PageAM.configure(background="grey")
        PageAM.geometry("650x500")
        PageAM.attributes('-topmost', True)


        Label(PageAM, text="Name", bd=2).place(x=1,y=1)
        Label(PageAM, text="Price", bd=2).place(x=1,y=26)
        Label(PageAM, text="Delete PLU", bd=2).place(x=1,y=90)
        Label(PageAM, text="PLU", bd=2).place(x=280,y=1)
        
        AM1 = Entry(PageAM, bd=2)
        AM1.place(x=100,y=1)
##        AM1.insert(0,"NULL")
        AM2 = Entry(PageAM, bd=2)
        AM2.place(x=100,y=26)
##        AM2.insert(0,"NULL")
        AM3 = Entry(PageAM, bd=2)
        AM3.place(x=100,y=90)

        AM4 = Entry(PageAM, bd=2)
        AM4.place(x=310,y=1)

        var4 = IntVar()
        var4.set(1)

        def ER():
            print(var4.get())
        
        Radio_x = 500
        X1 = 250
        X2 = 1
        button_number = 1

        Current_value = 1
        print('Previous_Value: ' + str(Previous_Value))

        def Value_update_1(Name,Valuee):
            f3= open("Previous_Value.txt","w")
            Current_value = Valuee
            Previous_Value = Current_value
            f3.write(str(Current_value))
            print('Previous_Value_after_Button: ' + str(Previous_Value))
            print('Current_value: ' + str(Current_value))
            f3.close()
            Button(PageAM, text="Add", width=20, height=1, fg="white", bg="green", command=partial(Add_Menu2,Current_value), bd=2).place(x=1,y=55)




        c.execute("SELECT * FROM MenuS ORDER BY Menu_Number ASC")
        for row in c.fetchall():
            row_0 = (row[0])
            row_1 = (row[1])
            if button_number == 1:
                R1 = Radiobutton(PageAM, text=(row[0]), variable=var4, value=1, command=partial(Value_update_1,row_0,row_1))
                R1.place(x=Radio_x,y=X2)
                button_number = button_number + 1
                X2 = X2 + 30
            elif button_number == 2:
                R2 = Radiobutton(PageAM, text=(row[0]), variable=var4, value=2, command=partial(Value_update_1,row_0,row_1))
                R2.place(x=Radio_x,y=X2)
                button_number = button_number + 1
                X2 = X2 + 30
            elif button_number == 3:
                R3 = Radiobutton(PageAM, text=(row[0]), variable=var4, value=3, command=partial(Value_update_1,row_0,row_1))
                R3.place(x=Radio_x,y=X2)
                button_number = button_number + 1
                X2 = X2 + 30
            elif button_number == 4:
                R4 = Radiobutton(PageAM, text=(row[0]), variable=var4, value=4, command=partial(Value_update_1,row_0,row_1))
                R4.place(x=Radio_x,y=X2)
                button_number = button_number + 1
                X2 = X2 + 30
            elif button_number == 5:
                R5 = Radiobutton(PageAM, text=(row[0]), variable=var4, value=5, command=partial(Value_update_1,row_0,row_1))
                R5.place(x=Radio_x,y=X2)
                button_number = button_number + 1
                X2 = X2 + 30
            elif button_number == 6:
                R6 = Radiobutton(PageAM, text=(row[0]), variable=var4, value=6, command=partial(Value_update_1,row_0,row_1))
                R6.place(x=Radio_x,y=X2)
                button_number = button_number + 1
                X2 = X2 + 30
            elif button_number == 7:
                R7 = Radiobutton(PageAM, text=(row[0]), variable=var4, value=7, command=partial(Value_update_1,row_0,row_1))
                R7.place(x=Radio_x,y=X2)
                button_number = button_number + 1
                X2 = X2 + 30
                
            elif button_number == 8:
                R8 = Radiobutton(PageAM, text=(row[0]), variable=var4, value=8, command=partial(Value_update_1,row_0,row_1))
                R8.place(x=Radio_x,y=X2)
                button_number = button_number + 1
                X2 = X2 + 30
            elif button_number == 9:
                R9 = Radiobutton(PageAM, text=(row[0]), variable=var4, value=9, command=partial(Value_update_1,row_0,row_1))
                R9.place(x=Radio_x,y=X2)
                button_number = button_number + 1
                X2 = X2 + 30
            elif button_number == 10:
                R10 = Radiobutton(PageAM, text=(row[0]), variable=var4, value=10, command=partial(Value_update_1,row_0,row_1))
                R10.place(x=Radio_x,y=X2)
                button_number = button_number + 1
                X2 = X2 + 30
            elif button_number == 11:
                R11 = Radiobutton(PageAM, text=(row[0]), variable=var4, value=11, command=partial(Value_update_1,row_0,row_1))
                R11.place(x=Radio_x,y=X2)
                button_number = button_number + 1
                X2 = X2 + 30
            elif button_number == 12:
                R12 = Radiobutton(PageAM, text=(row[0]), variable=var4, value=12, command=partial(Value_update_1,row_0,row_1))
                R12.place(x=Radio_x,y=X2)
                button_number = button_number + 1
                X2 = X2 + 30
            elif button_number == 13:
                R13 = Radiobutton(PageAM, text=(row[0]), variable=var4, value=13, command=partial(Value_update_1,row_0,row_1))
                R13.place(x=Radio_x,y=X2)
                button_number = button_number + 1
                X2 = X2 + 30
            elif button_number == 14:
                R14 = Radiobutton(PageAM, text=(row[0]), variable=var4, value=14, command=partial(Value_update_1,row_0,row_1))
                R14.place(x=Radio_x,y=X2)
                button_number = button_number + 1
                X2 = X2 + 30

        
        


##        R1 = Radiobutton(PageAM, text=button_1, variable=var4, value=1, command=ER)
##        R1.place(x=Radio_x,y=1)
##
##        R2 = Radiobutton(PageAM, text=button_2, variable=var4, value=2, command=ER)
##        R2.place(x=Radio_x,y=30)
##
##        R3 = Radiobutton(PageAM, text=button_3, variable=var4, value=3, command=ER)
##        R3.place(x=Radio_x,y=60)
##
##        R4 = Radiobutton(PageAM, text=button_4, variable=var4, value=4, command=ER)
##        R4.place(x=Radio_x,y=90)
##
##        R5 = Radiobutton(PageAM, text=button_5, variable=var4, value=5, command=ER)
##        R5.place(x=Radio_x,y=120)
##
##        R6 = Radiobutton(PageAM, text=button_6, variable=var4, value=6, command=ER)
##        R6.place(x=Radio_x,y=150)
##
##        R7 = Radiobutton(PageAM, text=button_7, variable=var4, value=7, command=ER)
##        R7.place(x=Radio_x,y=180)


        
        def Reset2():
            if len(AM3.get()) <= 0:
                MsgBox_009 = messagebox.showerror ('ERROR',Error.Error_009,icon = Error.Error_icon)
            else:
                MsgBox = messagebox.askquestion ('Warning','Are you sure you want save this Item',icon = 'warning')
                if MsgBox == 'yes':
                    B1 = AM3.get()
                    c.execute('''DELETE FROM Starters WHERE Item_PLU=?''',(B1,))
                    conn.commit()
                    PageAM.destroy()
        def Add_Menu2(Current_value):
            print("Add current: " + str(Current_value))
            Bbb1 = AM4.get()
            Bbb2 = (AM1.get()).replace (" ", "_")
            Bbb3 = str(AM2.get()) + " "
            Bbb4 = str(Current_value)
            print(Bbb4)
            if len(AM1.get()) <= 0:
                MsgBox_004 = messagebox.showerror ('ERROR',Error.Error_004,icon = Error.Error_icon)
            elif len(AM2.get()) <= 0:
                MsgBox_007 = messagebox.showerror ('ERROR',Error.Error_007,icon = Error.Error_icon)
            elif len(AM4.get()) <= 0:
                MsgBox_008 = messagebox.showerror ('ERROR',Error.Error_008,icon = Error.Error_icon)
            else:
                MsgBox = messagebox.askquestion ('Warning','Are you sure you want save this Item',icon = 'warning')
                if MsgBox == 'yes':
                    GEN.ItemAdd(Bbb1, Bbb2, Bbb3, Bbb4)
                    PageAM.destroy()

        def delete_all():
            MsgBox = messagebox.askquestion ('Warning','Are you sure you want to Delete All\nThis will delete everything and can not be undone',icon = 'warning')
            if MsgBox == 'yes':
                Lb1.delete(1, 200)
                c.execute('''DELETE FROM Starters''')
                conn.commit()
                PageAM.destroy()

        Label(PageAM, text="Add", bd=2, width=20, height=1, bg='yellow', fg='red').place(x=1,y=55)
##        Button(PageAM, text="Add", width=20, height=1, fg="white", bg="green", command=partial(Add_Menu2,Current_value), bd=2).place(x=1,y=55)
        Button(PageAM, text="delete", width=20, height=1, fg="white", bg="green", command=Reset2, bd=2).place(x=1,y=120)
        Button(PageAM, text="delete all", width=20, height=1, fg="Black", bg="Red", command=delete_all, bd=2).place(x=1,y=180)

        


#==========================================================#Income graph#=======================================================================

    def GRAPH():
        PCRJ2 = Tk()
        PCRJ2.title("Shop Database")
        PCRJ2.configure(background="green")
        PCRJ2.geometry("1980x1080")

#==========================================================#CRJ#=======================================================================
    
    def CRJ1():
##        GRAPH()
        def Reset1():
            MsgBox = messagebox.askquestion ('Warning','Are you sure you want clear the sales History',icon = 'warning')
            if MsgBox == 'yes':
                c.execute('''DROP TABLE CRJ''')
                conn.commit()
                c.execute('''CREATE TABLE IF NOT EXISTS CRJ(ID REAL,Date REAL, Description TEXT, Amount RAEL, Bank RAEL, Item TEXT, QTY TEXT)''')
                c.execute('''DROP TABLE Sales''')
                conn.commit()
                c.execute('''CREATE TABLE IF NOT EXISTS "Sales" (
                            "ID"	INTEGER,
                            "Date"	INTEGER,
                            "Time"	INTEGER,
                            "Item"	TEXT,
                            "Price"	INTEGER,
                            "Qty"	INTEGER,
                            "Weight" REAL)''')
                PCRJ.destroy()
                CRJ1()
                
        sqlite3.connect('Shop_Database.db')
        DATE2 = (time.strftime("%d/%m/%Y"))
        PCRJ = Tk()
        PCRJ.title("Shop Database")
        PCRJ.configure(background="green")
        PCRJ.geometry("1980x1080")
        Button(PCRJ, text="Clear", width=12, fg="white", bg="red", command=Reset1, bd=2).place(x=1,y=1)
        
        text = Text(PCRJ, width=170)

        BZ = PrettyTable()
        c.execute("SELECT * FROM CRJ")
        for row in c.fetchall():
            BZ.field_names = ["ID", "Time + Date", "Description", "Amount paid", "Bank", "Item", "QTY","Payment Type","Cashier"]
            BZB = (row)
            BZ.add_row((BZB))
        print(BZ)
        text.insert(INSERT, BZ)
        
        text.pack(side="top")

        text_I = Text(PCRJ, width=130)

        Query_Date_T = time.strftime("%d-%m-%Y")
        date1 = datetime.strptime(Query_Date_T, "%d-%m-%Y")
        modified_date = date1 + timedelta(days=-1)
        Query_Date_Y = datetime.strftime(modified_date, "%d-%m-%Y")

        BZ = PrettyTable()
        
        Total_Tenderd_Cash_Yesterday = 0.0
        Total_Meat_Yesterday = 0.0
        Total_Meat_Today = 0.0
        Total_Tenderd_Cash_Today = 0.0

        
        c.execute("SELECT * FROM Sales Where Date=?",(Query_Date_Y,))
        for row in c.fetchall():
            Total_Meat_Yesterday = float(Total_Meat_Yesterday) + float(row[6])
            Total_Tenderd_Cash_Yesterday = float(Total_Tenderd_Cash_Yesterday) + float(row[4])
        
        c.execute("SELECT * FROM Sales Where Date=?",(Query_Date_T,))
        for row in c.fetchall():
            Total_Meat_Today = float(Total_Meat_Today) + float(row[6])
            Total_Tenderd_Cash_Today = float(Total_Tenderd_Cash_Today) + float(row[4])

        BZ.field_names = ["Total Meat In KG [Yesterday]", "Total Tenderd Cash [Yesterday]", "Total Meat In KG [Today]", "Total Tenderd Cash [Today]",]
        BZ.add_row([Total_Meat_Yesterday, Total_Tenderd_Cash_Yesterday, Total_Meat_Today, Total_Tenderd_Cash_Today])
        text_I.insert(INSERT, BZ)
        
        text_I.pack(side="bottom")

        
#==========================================================#Restorant System#===================================================================

    def RSYS():
        def PASS(Table,NO):
            GEN.TableNumberGenerate(Table,NO)
        PageR = Tk()
        PageR.title("Item Database")
        PageR.configure(background="orange")
##        PageR.geometry("1100x800")
        PageR.attributes("-fullscreen", True)


        def exit_PageR():
            PageR.destroy()

        Frame1 = Frame(PageR)
        Frame1.grid(row=1,column=1)

        GEN.ROWN(Frame1,"1","Room ", "Room\n","4","5","6","7","8","9","10","11")
        
        GEN.ROWN(Frame1,"2","Room ", "Room\n","12","14","15","16","17","18","19","20")

        GEN.ROWN(Frame1,"3","Room ", "Room\n","21","22","201","202","203","204","0","0")

        GEN.ROWN(Frame1,"4","Staff ", "Room\n","1001","1002","1003","0","0","0","0","0")

##        GEN.ROWN(PageR,"5","Table ", "Table\n","41","42","43","44","45","46","47","48","49","50")

##        GEN.ROWN(PageR,"6","Table ", "Table\n","41","42","43","44","45","46","47","48","49","50")

##        GEN.ROWN(PageR,"7","Table ", "Table\n","51","52","53","54","55","56","57","58","59","60")

##        GEN.ROWN(PageR,"8","Table ", "Table\n","61","62","63","64","65","66","67","68","69","70")
    
        Button(Frame1, text='Exit', width=10, height=4, fg="black", bg="green", command=exit_PageR, bd=2).grid(row=1,column=11)
        Button(Frame1, text='Print All', width=10, height=4, fg="black", bg="green", command=GEN.print_all, bd=2).grid(row=2,column=11)

        Frame2 = Frame(PageR)
        Frame2.grid(row=2,column=1)

        Label(Frame2, text="All shots that have the option:\n  - 1 or 2\n  e.g. default is 2 shots, change it to 1 if you used 1\ndefult - 2\n\n you will be charged for the extra shot if not.\n\ncontact Bernhard/Fida/Connor for asistance if you strugel.", bd=2, fg="Red", bg="orange").grid(row=1,column=1)



#===========================================================#Delete product#===============================================================
    def Del_product():
        sqlite3.connect('Shop_Database.db')
        Page21 = Tk()
        Page21.title("Item Database")
        Page21.configure(background="grey")
        Page21.geometry("800x700")
        Page21.attributes('-topmost', True)

        def Cancel():
            Page21.destroy()

        Label(Page21, text="Code", bd=2).place(x=1,y=1)
        e1 = Entry(Page21, bd=2)
        e1.place(x=100,y=1)

        Button(Page21, text="Cancel", width=12, fg="white", bg="red", command=Cancel, bd=2).place(x=90,y=30)
        
        def data_entry1():
            if len(e1.get()) <= 0:
                MsgBox_008 = messagebox.showerror ('ERROR',Error.Error_008,icon = Error.Error_icon)
            else:
                MsgBox = messagebox.askquestion ('Warning','Are you sure you want Delete this Item',icon = 'warning')
                if MsgBox == 'yes':
                    sqlite3.connect('Shop_Database.db')
                    B1 = e1.get()
                    c.execute('''DELETE FROM Product_List WHERE Code=?''',(B1,))
                    conn.commit()
                    Page21.destroy()
                    Page1.destroy()
            
        Button(Page21, text="Delete", width=12, fg="white", bg="green", command=data_entry1, bd=2).place(x=1,y=30)

    

#==============================================================#product list#============================================================

    def P_List():
        Page22 = Tk()
        Page22.title("Item Database")
        Page22.configure(background="grey")
        Page22.geometry("800x700")
        Page22.attributes('-topmost', True)
        
        text4 = Text(Page22)
        text4.insert(INSERT, "|Code        |Price |Name                 |\n")
        
        c.execute("SELECT * FROM Product_List")
        DA22 = c.fetchall()
        for row in DA22:
            text4.insert(INSERT, (row))
            text4.insert(INSERT, "\n")
        text4.place(x=1,y=1)

    
        
#================================================================#Add Product#==========================================================

    
    def New_product():
        sqlite3.connect('Shop_Database.db')
        Page2 = Tk()
        Page2.title("Item Database")
        Page2.configure(background="grey")
        Page2.geometry("800x700")
        Page2.attributes('-topmost', True)

        def Cancel():
            Page2.destroy()

        Label(Page2, text="Code", bd=2).place(x=1,y=40)
        Label(Page2, text="Price", bd=2).place(x=1,y=20)
        Label(Page2, text="Item Name", bd=2).place(x=1,y=1)
        Label(Page2, text="Cost Price", bd=2).place(x=250,y=1)

        e1 = Entry(Page2, bd=2)
        e1.place(x=100,y=1)
        e2 = Entry(Page2, bd=2)
        e2.place(x=100,y=20)
        e3 = Entry(Page2, bd=2)
        e3.place(x=100,y=40)
        e33 = Entry(Page2, bd=2)
        e33.place(x=320,y=1)

        Button(Page2, text="Cancel", width=12, fg="white", bg="red", command=Cancel, bd=2).place(x=90,y=70)
        
        def data_entry2():
            sqlite3.connect('Shop_Database.db')
            B1 = e1.get()
            B2 = e2.get()
            B3 = e3.get()
            B4 = e33.get()
            if len(e1.get()) <= 0:
                MsgBox_009 = messagebox.showerror ('ERROR',Error.Error_009,icon = Error.Error_icon)
            elif len(e2.get()) <= 0:
                MsgBox_007 = messagebox.showerror ('ERROR',Error.Error_007,icon = Error.Error_icon)
            elif len(e3.get()) <= 0:
                MsgBox_010 = messagebox.showerror ('ERROR',Error.Error_010,icon = Error.Error_icon)
            elif len(e33.get) <= 0:
                MsgBox_011 = messagebox.showerror ('ERROR',Error.Error_011,icon = Error.Error_icon)
            else:
                MsgBox = messagebox.askquestion ('Warning','Are you sure you want save this Item',icon = 'warning')
                if MsgBox == 'yes':
                    c.execute('''INSERT INTO Product_List(Code, Price, Item, Cost_Price) VALUES(?, ? ,? ,?)''',(B3, B2, B1, B4))
                    conn.commit()
                    Page2.destroy()
                    Page1.destroy()
                    RUN1()
        Button(Page2, text="Add", width=12, fg="white", bg="green", command=data_entry2, bd=2).place(x=1,y=70)

        

#=================================================#Shop cart#==================================================================================
        
    def Cart1():
        Till.Login_Page()


    def ESC():
        print(DATE)
        wb=load_workbook(filepath)
        try:
            sheet = wb[DATE]
        except KeyError:
            sheet = wb.create_sheet(DATE)
        c.execute("SELECT * FROM Sales")
        for row in c.fetchall():
            sheet.append(row)
        
        wb.save(filepath)
        Page1.destroy()
    

#======================================================================================================================================================================
#========================================================================#Home Layout#=================================================================================
#======================================================================================================================================================================

    if LEVL == 1:
        Label(Page1, text="Made By Connor Hess  V1.0", bd=2, fg="white", bg="gray").place(x=1400,y=1)

    ##    F1 = Frame(Page1, width=1970, height=1070, bd=8, relief="raise")
    ##    F1.place(x=1,y=1)



        F2 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F2.place(x=1,y=1)
        
        LEVEL1 = Button(Page1, text="Barcode Cart", width=12, height=1, fg="white", bg="green", command=Cart1, bd=2).place(x=20,y=12)
        LEVEL2 = Button(Page1, text="Restorant System", width=12, height=1, fg="white", bg="green", command=RSYS, bd=2).place(x=20,y=42)




        F3 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F3.place(x=155,y=1)

        P1 = 12
        P2 = P1 + 30
        P3 = P2 + 30
        PA1 = 180
        
        LEVEL3 = Button(Page1, text="New Product", width=12, command=New_product, bd=2).place(x=PA1,y=P1)

        LEVEL4 = Button(Page1, text="Product list", width=12, height=1, fg="white", bg="green", command=P_List, bd=2).place(x=PA1,y=P2)



        F3 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F3.place(x=155 + 155,y=1)

        LEVEL5 = Button(Page1, text="CRJ", width=12, command=CRJ1, bd=2).place(x=340,y=20)

        
        F4 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F4.place(x=1,y=85)
        
        LEVEL6 = Button(Page1, text="Delete product", width=12, fg="white", bg="red", command=Del_product, bd=2).place(x=25,y=105)
        
        F5 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F5.place(x=1,y=170)

        LEVEL7 = Button(Page1, text="Add food item", width=12, height=1, fg="white", bg="green", command=Add_Menu1, bd=2).place(x=20,y=181)

        

        F6 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F6.place(x=1,y=255)

        LEVEL8 = Button(Page1, text="Help", width=12, height=1, fg="white", bg="green", command=Help, bd=2).place(x=20,y=266)
        LEVEL9 = Button(Page1, text="Create Excel Sheat", width=15, height=1, fg="white", bg="Red", command=ESC, bd=2).place(x=17,y=296)

        F7 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F7.place(x=1,y=340)

##        LEVEL10 = Button(Page1, text="First time wiz", width=12, height=1, fg="white", bg="green", command=FTW, bd=2).place(x=20,y=348)
        

        F8 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F8.place(x=1,y=425)

##        LEVEL10 = Button(Page1, text="Ticket System", width=12, height=1, fg="white", bg="green", command=TicketSYS, bd=2).place(x=20,y=433)

        
    elif LEVL == 2:
        Label(Page1, text="Made By Connor Hess  V1.0", bd=2, fg="white", bg="gray").place(x=1400,y=1)


        Label(Page1, text="", bd=2, fg="white", bg="gray").place(x=1400,y=1)

    ##    F1 = Frame(Page1, width=1970, height=1070, bd=8, relief="raise")
    ##    F1.place(x=1,y=1)



        F2 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F2.place(x=1,y=1)
        
        LEVEL1 = Button(Page1, text="Barcode Cart", width=12, height=1, fg="white", bg="green", command=Cart1, bd=2).place(x=20,y=12)
        LEVEL2 = Button(Page1, text="Restorant System", width=12, height=1, fg="white", bg="green", command=RSYS, bd=2).place(x=20,y=42)




        F3 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F3.place(x=155,y=1)

        P1 = 12
        P2 = P1 + 30
        P3 = P2 + 30
        PA1 = 180
        
        LEVEL3 = Button(Page1, text="New Product", width=12, command=New_product, bd=2).place(x=PA1,y=P1)

        LEVEL4 = Button(Page1, text="Product list", width=12, height=1, fg="white", bg="green", command=P_List, bd=2).place(x=PA1,y=P2)



        F3 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F3.place(x=155 + 155,y=1)

        LEVEL5 = Button(Page1, text="CRJ", width=12, command=CRJ1, bd=2).place(x=340,y=20)

        
        F4 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F4.place(x=1,y=85)
        
        LEVEL6 = Button(Page1, text="Delete product", width=12, fg="white", bg="red", command=Del_product, bd=2).place(x=25,y=105)
        
        F5 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F5.place(x=1,y=170)

        LEVEL7 = Button(Page1, text="Add food item", width=12, height=1, fg="white", bg="green", command=Add_Menu1, bd=2).place(x=20,y=181)

        

        F6 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F6.place(x=1,y=255)

        LEVEL8 = Button(Page1, text="Help", width=12, height=1, fg="white", bg="green", command=Help, bd=2).place(x=20,y=266)
        LEVEL9 = Button(Page1, text="Create Excel Sheat", width=15, height=1, fg="white", bg="Red", command=ESC, bd=2).place(x=17,y=296)

        F7 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F7.place(x=1,y=340)

##        LEVEL10 = Button(Page1, text="First time wiz", width=12, state=DISABLED, height=1, fg="white", bg="green", command=FTW, bd=2).place(x=20,y=348)
        

        F8 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F8.place(x=1,y=425)

        
    elif LEVL == 3:
        Label(Page1, text="Made By Connor Hess  V1.0", bd=2, fg="white", bg="gray").place(x=1400,y=1)

    ##    F1 = Frame(Page1, width=1970, height=1070, bd=8, relief="raise")
    ##    F1.place(x=1,y=1)



        F2 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F2.place(x=1,y=1)
        
        LEVEL1 = Button(Page1, text="Barcode Cart", width=12, height=1, fg="white", bg="green", command=Cart1, bd=2).place(x=20,y=12)
        LEVEL2 = Button(Page1, text="Restorant System", width=12, height=1, fg="white", bg="green", command=RSYS, bd=2).place(x=20,y=42)




        F3 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F3.place(x=155,y=1)

        P1 = 12
        P2 = P1 + 30
        P3 = P2 + 30
        PA1 = 180
        
        LEVEL3 = Button(Page1, text="New Product", width=12, state=DISABLED, command=New_product, bd=2).place(x=PA1,y=P1)

        LEVEL4 = Button(Page1, text="Product list", width=12, height=1, fg="white", bg="green", command=P_List, bd=2).place(x=PA1,y=P2)



        F3 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F3.place(x=155 + 155,y=1)

        LEVEL5 = Button(Page1, text="CRJ", width=12, state=DISABLED, command=CRJ1, bd=2).place(x=340,y=20)

        
        F4 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F4.place(x=1,y=85)
        
        LEVEL6 = Button(Page1, text="Delete product", state=DISABLED, width=12, fg="white", bg="red", command=Del_product, bd=2).place(x=25,y=105)
        
        F5 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F5.place(x=1,y=170)

        LEVEL7 = Button(Page1, text="Add food item", state=DISABLED, width=12, height=1, fg="white", bg="green", command=Add_Menu1, bd=2).place(x=20,y=181)

        

        F6 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F6.place(x=1,y=255)

        LEVEL8 = Button(Page1, text="Help", width=12, height=1, fg="white", bg="green", command=Help, bd=2).place(x=20,y=266)
        LEVEL9 = Button(Page1, text="Create Excel Sheat", state=DISABLED, width=15, height=1, fg="white", bg="Red", command=ESC, bd=2).place(x=17,y=296)

        F7 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F7.place(x=1,y=340)

##        LEVEL10 = Button(Page1, text="First time wiz", state=DISABLED, width=12, height=1, fg="white", bg="green", command=FTW, bd=2).place(x=20,y=348)
        

        F8 = Frame(Page1, width=150, height=80, bd=8, bg="light grey", relief="raise")
        F8.place(x=1,y=425)


##RUN1()

#state=DISABLED
#========================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================


