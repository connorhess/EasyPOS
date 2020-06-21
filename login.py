import sqlite3
#import tkinter
from tkinter import *
import Shop
import SETUP
import Error
from tkinter import messagebox



R = Shop

conn = sqlite3.connect('Shop_Database.db')
c = conn.cursor()

try:
    c.execute("SELECT * FROM Settings")
    for row in c.fetchall():
        pass
except:
    SETUP.FIRSTTIME()


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
        e1.delete(1.0, 1000.0)
        
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
        print(User)
        c.execute("SELECT * FROM Cashiers WHERE Name = ?",(User,))
        for row in c.fetchall():
            Password = str(e1.get())
            A = (row[2])
            if Password == A:
                print("Password OK")
                Login_page.destroy()
                if (row[3]) == 1.0:
                    R.LEV1()
                elif (row[3]) == 2.0:
                    R.LEV2()
                elif (row[3]) == 3.0:
                    R.LEV3()
            else:
                print("NO")
                MsgBox_002 = messagebox.showerror ('ERROR',Error.Error_002,icon = Error.Error_icon)

    Button(Login_page, text="Done", width=10, height=1, bg="blue", fg="white", command=ENTER, bd=2).place(x=180+X_Distance,y=560)


