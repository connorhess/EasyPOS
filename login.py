import sqlite3
import tkinter
from tkinter import *
import Shop
import Error
from tkinter import messagebox
import requests
import webbrowser
import win32api
import sys
import os
import Info
import Till
import random

from licensing.models import *
from licensing.methods import Key, Helpers


home = os.path.expanduser('~')

__author__ = Info.i_author
__copyright__ = Info.i_copyright
__credits__ = Info.i_credits
__license__ = Info.i_license
version = Info.i_version
__maintainer__ = Info.i_maintainer
__email__ = Info.i_email
__status__ = Info.i_status

_AppName_ = Info.i_AppName_

Downloads_location = os.path.join(home, 'Downloads')

conn = sqlite3.connect('Shop_Database.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS CRJ(ID REAL,Day INTEGER,Month INTEGER,Year INTEGER,Time INTEGER, Date INTEGER, Description TEXT, Amount RAEL, Bank RAEL, Item TEXT, QTY TEXT, Payment_Type TEXT, Cashier TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS Sales (
                        "ID"	INTEGER,
                        "Day"	INTEGER,
                        "Month"	INTEGER,
                        "Year"	INTEGER,
                        "Time"	INTEGER,
                        "Date"  INTEGER,
                        "Item"	TEXT,
                        "Price"	INTEGER,
                        "Qty"	INTEGER,
                        "Weight" REAL)''')
c.execute('''CREATE TABLE IF NOT EXISTS Product_List(Code INT, Price REAL, Item TEXT, Cost_Price REAL)''')
c.execute('''CREATE TABLE IF NOT EXISTS Customer_List(Code REAL, Name TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS MenuS(Menu_Name TEXT, Menu_Number RAEL)''')
c.execute('''CREATE TABLE IF NOT EXISTS Cashiers(ID REAL, Name TEXT, Password TEXT, Permision REAL)''')
c.execute('''CREATE TABLE IF NOT EXISTS Scale(Code INTEGER, Name TEXT, Price_per_kg REAL)''')
c.execute('''CREATE TABLE IF NOT EXISTS Settings(ID REAL, Name TEXT, Value REAL, OTHER TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS Tables(Item_PLU REAL, Item_Name TEXT, Item_Price INT, QTY INT, FPrice INT, Table_No INT)''')
c.execute('''CREATE TABLE IF NOT EXISTS Starters(Item_PLU REAL, Item_Name TEXT, Item_Price REAL, Menu INT)''')
def add_account(Name="admin",Password="1234",Perm=1):
    ID = random.randint(1,1000000000)
    c.execute('''INSERT INTO Cashiers(ID, Name, Password, Permision) VALUES(?, ? ,? ,?)''',(ID, Name, Password, Perm))
    c.execute('''INSERT INTO Settings(ID, Name, Value, OTHER) VALUES(?, ? ,? ,?)''',(1, 'VAT', 15, "True"))
    c.execute('''INSERT INTO Settings(ID, Name, Value, OTHER) VALUES(?, ? ,? ,?)''',(2, 'Details', 0, "null"))
    c.execute('''INSERT INTO Settings(ID, Name, Value, OTHER) VALUES(?, ? ,? ,?)''',(3, 'Product Key', 0, ""))
    conn.commit()
c.execute("SELECT rowid FROM Cashiers WHERE Name = ?", ("admin",))
if len(c.fetchall())==0:
    add_account()
    f = open("Key.txt", "w")
    f.close()
else:
    print("Loading")

##c.execute("SELECT * FROM Settings WHERE ID=?",(1,))
##print(str((c.fetchone())[2]))

R = Shop

try:
    import httplib
except:
    import http.client as httplib

def checkInternetHttplib(url="www.google.com", timeout=3):
    conn2 = httplib.HTTPConnection(url, timeout=timeout)
    try:
        conn2.request("HEAD", "/")
        conn2.close()
        return True
    except Exception as e:
        print(e)
        return False


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
                    R.LEV1(User)
                elif (row[3]) == 2.0:
                    R.LEV2(User)
                elif (row[3]) == 3.0:
                    R.LEV3(User)
            else:
                print("NO")
                MsgBox_002 = messagebox.showerror ('ERROR',Error.Error_002,icon = Error.Error_icon)

    Button(Login_page, text="Done", width=10, height=1, bg="blue", fg="white", command=ENTER, bd=2).place(x=180+X_Distance,y=560)
    Login_page.mainloop()


def Update():
    win32api.ShellExecute(0, 'open', '{Downloads_location}\\setup.msi', None, None, 10)

def Update_manager(TEXT="Checking for update"):
    if checkInternetHttplib() == True:
        Update_Manager = Tk()
        Update_Manager.title(TEXT)
        Update_Manager.configure(background="#BEBEBE")
        Update_Manager.attributes("-topmost", True)
        label = Label(Update_Manager, text=(TEXT+"\n\nMade By Connor Hess  V" + str(version)), fg="white", bg="gray").pack()

        response = requests.get('https://raw.githubusercontent.com/connorhess/EasyPOS/master/version.txt')
        data = response.text
        print(data)
        if float(data) > version:
            MsgBox = messagebox.askquestion ('Update!', f'{_AppName_} {version} needs to update to version {data}',icon = 'warning')
            if MsgBox == 'yes':
                webbrowser.open_new_tab('https://github.com/connorhess/EasyPOS/raw/master/'
                                                    'Update/Output/setup.exe?raw=true')
                Update_Manager.destroy()
                Update()
            else:
                Update_Manager.destroy()
                Login_Page()
        else:
            Update_Manager.destroy()
            Login_Page()
        Update_Manager.mainloop()
    elif checkInternetHttplib() == False:
        Login_Page()


RSAPubKey = '''<RSAKeyValue>
<Modulus>hWaA36UiW+Xt+NEqmt6XI1+1WV+hWbi8+C1IgI4NmvNP01Gb7ZjFcUUQZQBxwXfLTvSHJlAlUlbGk26n3Z0n5wrDMIPCB/x/EbI9yIueedKJB9VHMonIpXvAT+oSdoechFvasiE1q7khGUBLfEhsnYP2Q2JbQ2hToZ4eb+LqjuVOc54RkIup1OJ+Dur+WfqN+43QpLFQoFA7ydAg6gKpmGUKTgWR3q5UhDhHwIC1xYFKVnXA3BXVXOwTVa7D5tCCO/SauoetcXwPJwO0QXa7hQAR9fUCq25sy4Nm+hFPUYTs5UAO+H10ysenUqCFddhfrSzAakZzWpAnvZyDxPb5tw==
</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>'''
auth = "WyIyMzQ5MSIsIk9MY2xicDc5dVE5OUVmc0pFcWUwU2ZNTnB1c1F1dzVkeWtVSG5sTzgiXQ=="

def New_key():
    PageKey = Tk()
    PageKey.title("Shop Database")
    PageKey.configure(background="#BEBEBE")

    label = Label(PageKey, text="Product key", relief=RAISED)
    label.grid(row=0,column=0,sticky='e')

    KEY = Entry(PageKey, bd =5, width=30)
    KEY.grid(row=0,column=1)

##    os.remove("Key.txt")

    def Key_enter():
        Prod_Key = KEY.get()
        result = Key.activate(token=auth,\
                           rsa_pub_key=RSAPubKey,\
                           product_id=6725, \
                           key=Prod_Key,\
                           machine_code=Helpers.GetMachineCode())

        if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
            # an error occurred or the key is invalid or it cannot be activated
            # (eg. the limit of activated devices was achieved)
            print("The license does not work2: {0}".format(result[1]))
            c.execute("""UPDATE Settings SET Value=1 WHERE ID = 3""")
            conn.commit()
            PageKey.destroy()
            New_key()
        else:
            # everything went fine if we are here!
            print("The license is valid2!")
            c.execute("""UPDATE Settings SET OTHER=? AND Value=1 WHERE ID = 3""",(str(Prod_Key),))
            conn.commit()
            PageKey.destroy()
            Update_manager()
    Button(PageKey, text="Enter", command=Key_enter).grid(row=1,column=1)
    PageKey.mainloop()


if checkInternetHttplib() == True:
    try:
        c.execute("SELECT * FROM Settings WHERE ID=?",(3,))
        KEY_data = (str((c.fetchone())[3]))
        #print(KEY_data)
        result = Key.activate(token=auth,\
                           rsa_pub_key=RSAPubKey,\
                           product_id=6725, \
                           key=KEY_data,\
                           machine_code=Helpers.GetMachineCode())

        if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
            # an error occurred or the key is invalid or it cannot be activated
            # (eg. the limit of activated devices was achieved)
            print("The license does not work1: {0}".format(result[1]))
            c.execute("""UPDATE Settings SET Value=0 WHERE ID = 3""")
            conn.commit()
            New_key()
        else:
            # everything went fine if we are here!
            print("The license is valid!1")
            c.execute("""UPDATE Settings SET Value=1 WHERE ID = 3""")
            conn.commit()
            Update_manager()
    except:
        New_key()
elif checkInternetHttplib() == False:
    c.execute("SELECT * FROM Settings WHERE ID=?",(3,))
    Last_Veri = (int((c.fetchone())[2]))
    if Last_Veri >= 1:
        Update_manager()
    else:
        MsgBox_017 = messagebox.showerror ('ERROR',Error.Error_017,icon = Error.Error_icon)
