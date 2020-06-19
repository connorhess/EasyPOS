import sqlite3
#import tkinter
from tkinter import *
import Shop
import SETUP

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
        User = LbN1.get(LbN1.curselection())
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

    Button(Login_page, text="Done", width=10, height=1, bg="blue", fg="white", command=ENTER, bd=2).place(x=180+X_Distance,y=560)


Login_Page()

##def STAFF():
##    Page10 = Tk()
##    Page10.title("Shop Database login")
##    Page10.geometry("450x200")
##    c.execute('''CREATE TABLE IF NOT EXISTS Staff_Login(Name TEXT, Password TEXT)''')
##
##    
##
##
##
##
##
##    def Admin():
##        Page14 = Tk()
##        Page14.configure(background="grey")
##        Page14.title("Shop Database login")
##        Page14.geometry("450x200")
##        Label(Page14, text="Password", bd=2).place(x=1,y=1)
##        e200 = Entry(Page14, bd=2, show='*')
##        e200.place(x=70,y=1)
##        def DONE1():
##            c.execute("SELECT * FROM Settings WHERE ID=2")
##            for row in c.fetchall():
##                AAA = (row[3])
##                Password3 = e200.get()
##                if Password3 == AAA:
##                    print ("OK")
##                    R.LEV1()
##                    Page14.destroy()
##                    Page10.destroy()
##        Button(Page14, text="OK", width=6, height=1, fg="white", bg="green", command=DONE1, bd=2).place(x=1,y=25)
##
##    def Managment1():
##        Page14 = Tk()
##        Page14.configure(background="grey")
##        Page14.title("Shop Database login")
##        Page14.geometry("450x200")
##        Label(Page14, text="Password", bd=2).place(x=1,y=1)
##        e200 = Entry(Page14, bd=2, show='*')
##        e200.place(x=70,y=1)
##        def DONE1():
##            c.execute("SELECT * FROM Settings WHERE ID=3")
##            for row in c.fetchall():
##                AAA = (row[3])
##                Password3 = e200.get()
##                if Password3 == AAA:
##                    print ("OK")
##                    R.LEV2()
##                    Page14.destroy()
##                    Page10.destroy()
##        Button(Page14, text="OK", width=6, height=1, fg="white", bg="green", command=DONE1, bd=2).place(x=1,y=25)
##
##    def Managment2():
##        Page14 = Tk()
##        Page14.configure(background="grey")
##        Page14.title("Shop Database login")
##        Page14.geometry("450x200")
##        Label(Page14, text="Password", bd=2).place(x=1,y=1)
##        e200 = Entry(Page14, bd=2, show='*')
##        e200.place(x=70,y=1)
##        def DONE1():
##            c.execute("SELECT * FROM Settings WHERE ID=4")
##            for row in c.fetchall():
##                AAA = (row[3])
##                Password3 = e200.get()
##                if Password3 == AAA:
##                    print ("OK")
##                    R.LEV2()
##                    Page14.destroy()
##                    Page10.destroy()
##        Button(Page14, text="OK", width=6, height=1, fg="white", bg="green", command=DONE1, bd=2).place(x=1,y=25)
##
##    def Cashier1():
##        Page14 = Tk()
##        Page14.configure(background="grey")
##        Page14.title("Shop Database login")
##        Page14.geometry("450x200")
##        Label(Page14, text="Password", bd=2).place(x=1,y=1)
##        e200 = Entry(Page14, bd=2, show='*')
##        e200.place(x=70,y=1)
##        def DONE1():
##            c.execute("SELECT * FROM Settings WHERE ID=5")
##            for row in c.fetchall():
##                AAA = (row[3])
##                Password3 = e200.get()
##                if Password3 == AAA:
##                    print ("OK")
##                    R.LEV3()
##                    Page14.destroy()
##                    Page10.destroy()
##        Button(Page14, text="OK", width=6, height=1, fg="white", bg="green", command=DONE1, bd=2).place(x=1,y=25)
##
##    def Cashier2():
##        Page14 = Tk()
##        Page14.configure(background="grey")
##        Page14.title("Shop Database login")
##        Page14.geometry("450x200")
##        Label(Page14, text="Password", bd=2).place(x=1,y=1)
##        e200 = Entry(Page14, bd=2, show='*')
##        e200.place(x=70,y=1)
##        def DONE1():
##            c.execute("SELECT * FROM Settings WHERE ID=6")
##            for row in c.fetchall():
##                AAA = (row[3])
##                Password3 = e200.get()
##                if Password3 == AAA:
##                    print ("OK")
##                    R.LEV3()
##                    Page14.destroy()
##                    Page10.destroy()
##        Button(Page14, text="OK", width=6, height=1, fg="white", bg="green", command=DONE1, bd=2).place(x=1,y=25)
##
##
##    
##    var = IntVar()
##    
##    def sel():
##        print(var.get())
##        if (var.get()) == 1:
##            print ("admin")
##            Admin()
##        elif (var.get()) == 2:
##            print ("Managment 1")
##            Managment1()
##        elif (var.get()) == 3:
##            print ("Managment 2")
##            Managment2()
##        elif (var.get()) == 4:
##            print ("Cashier 1")
##            Cashier1()
##        elif (var.get()) == 5:
##            print ("Cashier 2")
##            Cashier2()
##        else:
##            print ("No")
##        print(str(var.get()))
##
##       
##
##    root = Page10
##
##
##    
##    
##    R1 = Radiobutton(root, text="Admin", variable=var, value=1,
##                      command=sel)
##    R1.pack( anchor = W )
##
##    R2 = Radiobutton(root, text="Managment 1", variable=var, value=2,
##                      command=sel)
##    R2.pack( anchor = W )
##
##    R3 = Radiobutton(root, text="Managment 2", variable=var, value=3,
##                      command=sel)
##    R3.pack( anchor = W)
##
##    R4 = Radiobutton(root, text="cashier 1", variable=var, value=4,
##                      command=sel)
##    R4.pack( anchor = W)
##
##    R5 = Radiobutton(root, text="Cashier 2", variable=var, value=5,
##                      command=sel)
##    R5.pack( anchor = W)
##               
##
##        
####    #Button(Page10, text="Login", width=6, height=1, fg="white", bg="green", command=LOG1, bd=2).place(x=200,y=1)
####    Button(Page10, text="Cancel", width=6, height=1, fg="white", bg="red", command=RUN2, bd=2).place(x=200,y=25)
##    #Button(Page10, text="Create", width=6, height=1, fg="black", bg="white", command=RUN3, bd=2).place(x=200,y=50)
##
##
##
##
##    Page10.mainloop()
##
##
##
##
##
##
##
##
##STAFF()
