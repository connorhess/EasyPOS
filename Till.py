import sqlite3
from tkinter import *
from tkinter import filedialog
import time
import random
from prettytable import PrettyTable
from functools import partial
import sys
import os
from datetime import timedelta
import datetime
import Error
from tkinter import messagebox

print(type(str(str(('9')) + " x " + str(('y')))))

x = PrettyTable()
x2 = PrettyTable()

TimeDate = (time.strftime("%H:%M--%d/%m/%Y"))

DEF1 = "0000"

NAME1 = "Admin"
PASS1 = "99562281"
NAME2 = "Cashier 1"
PASS2 = DEF1
NAME3 = "Cashier 2"
PASS3 = DEF1
TIME = (time.strftime("%H:%M"))
DATE = (time.strftime("%d-%m-%Y"))
Day = (time.strftime("%d"))
Month = (time.strftime("%m"))
Year = (time.strftime("%Y"))

print (time.strftime("%H:%M"))
print (time.strftime("%d/%m/%Y"))
print (random.randint(1,1000000000))


conn = sqlite3.connect('Shop_Database.db')
c = conn.cursor()


def delete_scale(Name):
    c.execute('''DELETE FROM Scale WHERE Name=?''',(Name,))
    conn.commit()

def add_scale(Code,Name,Price_per_kg):
    c.execute('''INSERT INTO Scale(Code, Name, Price_per_kg) VALUES(? ,? ,?)''',(Code, Name, Price_per_kg))
    conn.commit()


def delete_account(Name):
    c.execute('''DELETE FROM Cashiers WHERE Name=?''',(Name,))
    conn.commit()

def add_account(Name="admin",Password="1234",Perm=1):
    ID = random.randint(1,1000000000)
    c.execute('''INSERT INTO Cashiers(ID, Name, Password, Permision) VALUES(?, ? ,? ,?)''',(ID, Name, Password, Perm))
    conn.commit()

x.field_names = ["Code", "Name", "Price","Weight"]
x2.field_names = ["Code", "Name", "Price"]

def Cart1(Logged_In="admin"):
    sqlite3.connect('Shop_Database.db')
    Page3 = Tk()
    Page3.title("Cart")
    Page3.configure(background="grey")
    Page3.attributes("-fullscreen", True)
    Page3.attributes('-topmost', True)
    Sale_ID = random.randint(1,1000000000)

    global count
    count = 0

    text3 = Text(Page3, bd=8, width=60)    
    c.execute("SELECT * FROM Product_List")
    DA22 = c.fetchall()
    for row in DA22:
        x2.add_row([(row[0]), (row[2]), (row[1])])

    text3.insert(INSERT, x2)
    text3.place(x=650,y=1)

    text = Text(Page3, bd=8, width=60)
    
    e6 = Entry(Page3, bd=2,)
    e6.place(x=510,y=1)

    def Clear_Cart():
##            c.execute("""DELETE * FROM Sales WHERE ID=?""",(Sale_ID,))
##            print("cleard")
##            conn.commit()
##            Page3.destroy()
        Login_page = Tk()
        Login_page.title("Login Page")
        Login_page.configure(background="cadet blue")
        Login_page.attributes("-fullscreen", True)
        Login_page.attributes('-topmost', True)


        X_Distance = 600

        F1 = Frame(Login_page, bd=8, relief="raise")
        F1.place(x=180+X_Distance,y=300)
        Label(F1, text="Password", bd=2).pack(side="top")
    ##    e1 = Text(F1, height=1, width=15)
        e1 = Entry(F1, bd=2, width=15)
        e1.pack(side="top")


        LbN1 = Listbox(F1)
        c.execute("SELECT * FROM Cashiers WHERE Permision<=2")
        for row in c.fetchall():
    ##        print(row)
    ##        print(row[1])
            Name = row[1]
            LbN1.insert(1, Name)
        
        
        def K9():
            e1.insert(INSERT, "9")
        def K8():
            e1.insert(INSERT, "8")
        def K7():
            e1.insert(INSERT, "7")
        def K6():
            e1.insert(INSERT, "6")
        def K5():
            e1.insert(INSERT, "5")
        def K4():
            e1.insert(INSERT, "4")
        def K3():
            e1.insert(INSERT, "3")
        def K2():
            e1.insert(INSERT, "2")
        def K1():
            e1.insert(INSERT, "1")
        def K0():
            e1.insert(INSERT, "0")
        def K():
            e1.insert(INSERT, ".")
        def K10():
            e1.delete(0,100)
            
        F101 = Frame(Login_page, bd=8, bg="grey", relief="raise")
        F101.place(x=X_Distance,y=300)

        scale_1 = 3

        W = 2*scale_1
        H = 1*scale_1

        Button(F101, text="9", width=W, height=H, bg="blue", fg="white", command=K9, bd=2).grid(row=1,column=2)
        Button(F101, text="8", width=W, height=H, bg="blue", fg="white", command=K8, bd=2).grid(row=1,column=1)
        Button(F101, text="7", width=W, height=H, bg="blue", fg="white", command=K7, bd=2).grid(row=1,column=0)
        Button(F101, text="6", width=W, height=H, bg="blue", fg="white", command=K6, bd=2).grid(row=2,column=2)
        Button(F101, text="5", width=W, height=H, bg="blue", fg="white", command=K5, bd=2).grid(row=2,column=1)
        Button(F101, text="4", width=W, height=H, bg="blue", fg="white", command=K4, bd=2).grid(row=2,column=0)
        Button(F101, text="3", width=W, height=H, bg="blue", fg="white", command=K3, bd=2).grid(row=3,column=2)
        Button(F101, text="2", width=W, height=H, bg="blue", fg="white", command=K2, bd=2).grid(row=3,column=1)
        Button(F101, text="1", width=W, height=H, bg="blue", fg="white", command=K1, bd=2).grid(row=3,column=0)
        Button(F101, text="0", width=W, height=H, bg="blue", fg="white", command=K0, bd=2).grid(row=4,column=1)
        Button(F101, text=".", width=W, height=H, bg="blue", fg="white", command=K, bd=2).grid(row=4,column=0)
        Button(F101, text="C", width=W, height=H, bg="blue", fg="white", command=K10, bd=2).grid(row=4,column=2)
        Label(F1, text="_______________________", bd=2).pack(side="top")
        Label(F1, text="User", bd=2).pack(side="top")
        LbN1.pack(side="top")
        def Cancel():
            Login_page.destroy()
        def ENTER():
            User = LbN1.get(LbN1.curselection())
            print(LbN1.curselection())
            print(User)
            c.execute("SELECT * FROM Cashiers WHERE Name = ?",(User,))
            for row in c.fetchall():
                Password = str(e1.get())
                A = (row[2])
                if Password == A:
                    print("Password OK")
                    c.execute('''DELETE FROM Sales WHERE ID=?''',(Sale_ID,))
                    conn.commit()
                    Login_page.destroy()
                    Login_Page()
                    Page3.destroy()
                else:
                    print("NO")

        Button(Login_page, text="Done", width=10, height=1, bg="blue", fg="white", command=ENTER, bd=2).place(x=180+X_Distance,y=560)
        Button(Login_page, text="Cancel", width=10, height=1, bg="blue", fg="white", command=Cancel, bd=2).place(x=100+X_Distance,y=560)

    def ADD1():
        sqlite3.connect('Shop_Database.db')
        Add1 = (e6.get())
        global count
        text.delete(1.0,100000.0)
        c.execute("SELECT * FROM Product_List WHERE Code=?",(Add1,))
        DA22 = c.fetchall()
        for row in DA22:
            x.add_row([(row[0]), (row[2]), (row[1]),"0.0"])
            Name_ADD_1 = (row[2])
            Price_ADD_1 = (row[1])
            c.execute('''INSERT INTO Sales(ID, Day, Month, Year, Time, Date, Item, Price, QTY, Weight) VALUES(?, ?, ?, ? ,? ,?, ?, ?, ?,?)''',(Sale_ID,(time.strftime("%d")), (time.strftime("%m")),(time.strftime("%Y")),(time.strftime("%H:%M")),(time.strftime("%d-%m-%Y")), Name_ADD_1, Price_ADD_1, "1", "0.000"))
            conn.commit()
            count = count + (row[1])
            text.insert(INSERT, x)

        e6.delete (0, last=100 )

    def Scale():
        sqlite3.connect('Shop_Database.db')
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13 = str(e6.get())
        Code_1 = s1+s2+s3+s4+s5+s6
        Price_1 = s8+s9+s10+ "." +s11+s12
        Code_2 = str(e6.get())
        print(Code_1)
        print(Price_1)
        global count
        text.delete(1.0,100000.0)
        c.execute("SELECT * FROM Scale WHERE Code=?",(Code_1,))
        DA22 = c.fetchall()
        for row in DA22:
            Name_ADD_1 = (row[1])
            Price_per_KG = (row[2])
            weight = round((float(Price_1)/(Price_per_KG)),3)
            x.add_row([Code_2, (row[1]), Price_1,weight])
            print(weight)
            c.execute('''INSERT INTO Sales(ID, Day, Month, Year, Time, Date, Item, Price, QTY, Weight) VALUES(?, ?, ?, ? ,? ,?, ?, ?, ?,?)''',(Sale_ID,(time.strftime("%d")), (time.strftime("%m")),(time.strftime("%Y")),(time.strftime("%H:%M")),(time.strftime("%d-%m-%Y")), Name_ADD_1, Price_1, "1", weight))
            conn.commit()
            count = count + float(Price_1)
            text.insert(INSERT, x)

        e6.delete (0, last=100 )

    TIME1 = (time.strftime("%H:%M"))
    DATE1 = (time.strftime("%d/%m/%Y"))
    def Total():
        text.insert(INSERT, "\n____________________________________________________________\n")
        text.insert(INSERT, "Cashier Name:       Time:        Date:                Total:\n")
        text.insert(INSERT, (Logged_In) + " "*(18-len(Logged_In)))
        text.insert(INSERT, (TIME1))
        text.insert(INSERT, "        ")
        text.insert(INSERT, (DATE1))
        text.insert(INSERT, "           R")
        text.insert(END, (round(count, 2)))
        text.insert(INSERT, "\nSale_ID: " + str(Sale_ID))
        print (text.get(1.0, 1000.0))       ##add to thermal printer
    text.place(x=1,y=1)
        
    def PAY():
##            Page3.destroy()
        Page4 = Tk()
        Page4.title("Shop Database")
        Page4.geometry("400x300")
        Page4.attributes('-topmost', True)
        Label(Page4, text="Total", bd=2).place(x=1,y=1)
        Label(Page4, text=(round(count, 2)), bd=2).place(x=60,y=1)
        Label(Page4, text="Cash", bd=2).place(x=1,y=30)
##            e7 = Entry(Page4, bd=2)
##            e7.place(x=60,y=30)
        text2 = Text(Page4, height=1, width=10)

        #======Numpad======#
        def K9():
            text2.insert(INSERT, "9")
        def K8():
            text2.insert(INSERT, "8")
        def K7():
            text2.insert(INSERT, "7")
        def K6():
            text2.insert(INSERT, "6")
        def K5():
            text2.insert(INSERT, "5")
        def K4():
            text2.insert(INSERT, "4")
        def K3():
            text2.insert(INSERT, "3")
        def K2():
            text2.insert(INSERT, "2")
        def K1():
            text2.insert(INSERT, "1")
        def K0():
            text2.insert(INSERT, "0")
        def K():
            text2.insert(INSERT, ".")
        def K10():
            text2.delete(1.0, 1000.0)

        F102 = Frame(Page4, bd=8, bg="grey", relief="raise")
        F102.place(x=150,y=1)

        scale_1 = 3

        W = 2*scale_1
        H = 1*scale_1

        Button(F102, text="9", width=W, height=H, bg="blue", fg="white", command=K9, bd=2).grid(row=1,column=2)
        Button(F102, text="8", width=W, height=H, bg="blue", fg="white", command=K8, bd=2).grid(row=1,column=1)
        Button(F102, text="7", width=W, height=H, bg="blue", fg="white", command=K7, bd=2).grid(row=1,column=0)
        Button(F102, text="6", width=W, height=H, bg="blue", fg="white", command=K6, bd=2).grid(row=2,column=2)
        Button(F102, text="5", width=W, height=H, bg="blue", fg="white", command=K5, bd=2).grid(row=2,column=1)
        Button(F102, text="4", width=W, height=H, bg="blue", fg="white", command=K4, bd=2).grid(row=2,column=0)
        Button(F102, text="3", width=W, height=H, bg="blue", fg="white", command=K3, bd=2).grid(row=3,column=2)
        Button(F102, text="2", width=W, height=H, bg="blue", fg="white", command=K2, bd=2).grid(row=3,column=1)
        Button(F102, text="1", width=W, height=H, bg="blue", fg="white", command=K1, bd=2).grid(row=3,column=0)
        Button(F102, text="0", width=W, height=H, bg="blue", fg="white", command=K0, bd=2).grid(row=4,column=1)
        Button(F102, text=".", width=W, height=H, bg="blue", fg="white", command=K, bd=2).grid(row=4,column=0)
        Button(F102, text="C", width=W, height=H, bg="blue", fg="white", command=K10, bd=2).grid(row=4,column=2)

        text2.place(x=60,y=30)
        
        def PAID(Payment_Type):
            EE2 = (text2.get(1.0, 1000.0))
            CHANGE = float(EE2) - float(count)
            if float(EE2) < count:
                print("error 1")
                MsgBox_001 = messagebox.showerror ('ERROR',Error.Error_001,icon = Error.Error_icon)

            else:
                Page4.destroy()
                def OK1():
                    #===========================#
                    RR1 = Sale_ID
                    Bb1 = RR1
                    Bb2 = TimeDate
                    Bb3 = "sales"
                    Bb5 = (str(round(count,2)))
                    Bb4 = (str(EE2))
                    print(Bb4)
                    print(type(Bb4))
                    Items = []
                    c.execute("SELECT * FROM Sales WHERE ID = ?",(Sale_ID,))
                    for row in c.fetchall():
                        Items.append(str(str((row[8])) + " x " + str((row[6]))))
                    Bb6 = str(Items)
##                    Bb6 = (text.get(1.0, 1000.0))
                    Bb7 = 1
                    Payment_type = Payment_Type
                    c.execute('''INSERT INTO CRJ(ID, Day, Month, Year, Time, Date, Description, Amount, Bank, Item, QTY,Payment_Type,Cashier) VALUES(?, ? ,? ,? ,? ,? ,?,?,?,?,?,?,?)''',(Bb1,(time.strftime("%d")), (time.strftime("%m")),(time.strftime("%Y")),(time.strftime("%H:%M")),(time.strftime("%d-%m-%Y")), Bb3, Bb4, Bb5, Bb6, Bb7,Payment_type,Logged_In))
                    conn.commit()
                    #===========================#
                    Login_Page()
##                    Page4.destroy()
                    Page3.destroy()
                    Page5.destroy()
                Page5 = Tk()
                Page5.title("Shop Database")
                Page5.configure(background="grey")
                Page5.geometry("400x300")
                Page5.attributes('-topmost', True)

                Label(Page5, text="Change", bd=2).place(x=1,y=1)
    ##                EE1 = e7.get()
                Label(Page5, text=(CHANGE), bd=2).place(x=100,y=1)
                Button(Page5, text="OK", width=10, height=2, fg="white", bg="green", command=OK1, bd=2).place(x=1,y=70)
                
                def iprint():
                    Q = (text.get(1.0, 1000.0)) + "\n\nThank you for shopping by us.                Software Made By Connor Hess"
                    filename = tempfile.mktemp(".txt")
                    open (filename, "w").write(Q)
                    os.startfile(filename, "print")

                Button(Page5, text="Print", width=15, height=1, fg="white", bg="green", command=iprint, bd=2).place(x=1,y=140)
        def cancel5():
            Page4.destroy()

        Button(Page4, text="PAY - Card", width=20, height=1, fg="white", bg="green", command=partial(PAID,"Card"), bd=2).place(x=1,y=60)
        Button(Page4, text="PAY - Cash", width=20, height=1, fg="white", bg="green", command=partial(PAID,"Cash"), bd=2).place(x=1,y=60+25)
        Button(Page4, text="PAY - Account", width=20, height=1, fg="white", bg="green", command=partial(PAID,"Account"), bd=2).place(x=1,y=60+50)
        Button(Page4, text="Cancel", width=20, height=1, fg="white", bg="green", command=cancel5, bd=2).place(x=1,y=60+100)

    text.place(x=1,y=1)
    Button(Page3, text="Add Normal", width=12, fg="white", bg="green", command=ADD1, bd=2).place(x=510,y=25)
    Button(Page3, text="Add Scale", width=12, fg="white", bg="green", command=Scale, bd=2).place(x=510,y=50)
    Button(Page3, text="Delete_Sale", width=12, fg="white", bg="green", command=Clear_Cart, bd=2).place(x=510,y=100)
    Button(Page3, text="Total", width=15, height=1, fg="white", bg="green", command=Total, bd=2).place(x=510,y=250)
    Button(Page3, text="Pay", width=15, height=1, fg="white", bg="green", command=PAY, bd=2).place(x=510,y=275)




def Login_Page():
    Login_page = Tk()
    Login_page.title("Login Page")
    Login_page.configure(background="cadet blue")
    Login_page.attributes("-fullscreen", True)
    Login_page.attributes('-topmost', True)


    X_Distance = 600

    F1 = Frame(Login_page, bd=8, relief="raise")
    F1.place(x=180+X_Distance,y=300)
    Label(F1, text="Password", bd=2).pack(side="top")
##    e1 = Text(F1, height=1, width=15)
    e1 = Entry(F1, bd=2, width=15)
    e1.pack(side="top")


    LbN1 = Listbox(F1)
    c.execute("SELECT * FROM Cashiers")
    for row in c.fetchall():
##        print(row)
##        print(row[1])
        Name = row[1]
        LbN1.insert(1, Name)
    
    
    def K9():
        e1.insert(INSERT, "9")
    def K8():
        e1.insert(INSERT, "8")
    def K7():
        e1.insert(INSERT, "7")
    def K6():
        e1.insert(INSERT, "6")
    def K5():
        e1.insert(INSERT, "5")
    def K4():
        e1.insert(INSERT, "4")
    def K3():
        e1.insert(INSERT, "3")
    def K2():
        e1.insert(INSERT, "2")
    def K1():
        e1.insert(INSERT, "1")
    def K0():
        e1.insert(INSERT, "0")
    def K():
        e1.insert(INSERT, ".")
    def K10():
        e1.delete(0,100)
        
    F101 = Frame(Login_page, bd=8, bg="grey", relief="raise")
    F101.place(x=X_Distance,y=300)

    scale_1 = 3

    W = 2*scale_1
    H = 1*scale_1

    Button(F101, text="9", width=W, height=H, bg="blue", fg="white", command=K9, bd=2).grid(row=1,column=2)
    Button(F101, text="8", width=W, height=H, bg="blue", fg="white", command=K8, bd=2).grid(row=1,column=1)
    Button(F101, text="7", width=W, height=H, bg="blue", fg="white", command=K7, bd=2).grid(row=1,column=0)
    Button(F101, text="6", width=W, height=H, bg="blue", fg="white", command=K6, bd=2).grid(row=2,column=2)
    Button(F101, text="5", width=W, height=H, bg="blue", fg="white", command=K5, bd=2).grid(row=2,column=1)
    Button(F101, text="4", width=W, height=H, bg="blue", fg="white", command=K4, bd=2).grid(row=2,column=0)
    Button(F101, text="3", width=W, height=H, bg="blue", fg="white", command=K3, bd=2).grid(row=3,column=2)
    Button(F101, text="2", width=W, height=H, bg="blue", fg="white", command=K2, bd=2).grid(row=3,column=1)
    Button(F101, text="1", width=W, height=H, bg="blue", fg="white", command=K1, bd=2).grid(row=3,column=0)
    Button(F101, text="0", width=W, height=H, bg="blue", fg="white", command=K0, bd=2).grid(row=4,column=1)
    Button(F101, text=".", width=W, height=H, bg="blue", fg="white", command=K, bd=2).grid(row=4,column=0)
    Button(F101, text="C", width=W, height=H, bg="blue", fg="white", command=K10, bd=2).grid(row=4,column=2)
    Label(F1, text="_______________________", bd=2).pack(side="top")
    Label(F1, text="User", bd=2).pack(side="top")
    LbN1.pack(side="top")


    def ENTER():
        try:
            User = LbN1.get(LbN1.curselection())
        except:
            MsgBox_003 = messagebox.showerror ('ERROR',Error.Error_003,icon = Error.Error_icon)
        print(LbN1.curselection())
        print(User)
        c.execute("SELECT * FROM Cashiers WHERE Name = ?",(User,))
        for row in c.fetchall():
            Password = str(e1.get())
            A = (row[2])
            if Password == A:
                print("Password OK")
                Login_page.destroy()
                Cart1(User)
            else:
                print("NO")
                MsgBox_002 = messagebox.showerror ('ERROR',Error.Error_002,icon = Error.Error_icon)

    Button(Login_page, text="Login", width=10, height=1, bg="blue", fg="white", command=ENTER, bd=2).place(x=180+X_Distance,y=560)



def Barcode():
    pass


##Login_Page()
