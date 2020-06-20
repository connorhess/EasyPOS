import sqlite3
from tkinter import *
import time
import random
import RSYSS
from functools import partial
import sys
import xlsxwriter
from prettytable import PrettyTable
import os
import tempfile
from tkinter import messagebox


#not Built In
from openpyxl import Workbook
from openpyxl import load_workbook

x = PrettyTable()

conn = sqlite3.connect('Shop_Database.db')
c = conn.cursor()


#=======================================================================================================First time wizzard=================================================================================#


def FIRSTTIME():
    P1 = Tk()
    P1.title("Shop Database")
    P1.configure(background="cadet blue")
    P1.geometry("700x500")
        
    Label(P1, text="Settings",bg="cadet blue" ,width=20 ,bd=2).grid(row=1,column=1)

    R = 2
    Label(P1, text="Print to Printer",width=15 ,anchor=E ,bg="cadet blue" ,bd=2).grid(row=R,column=1)
    var1 = IntVar()
    R1 = Radiobutton(P1,text="Yes",bg="cadet blue" , variable=var1, value=1)
    R1.grid(row=R,column=2)
    R2 = Radiobutton(P1,text="No",bg="cadet blue" , variable=var1, value=2)
    R2.grid(row=R,column=3)

    Label(P1, text="Admin Pin",width=15 ,anchor=E ,bg="cadet blue" ,bd=2).grid(row=3,column=1)
    AP = Entry(P1, bd=2)
    AP.grid(row=3,column=2)
    

    Label(P1, text="Managment 1 Pin",width=15 ,anchor=E ,bg="cadet blue" ,bd=2).grid(row=4,column=1)
    M1P = Entry(P1, bd=2)
    M1P.grid(row=4,column=2)
    
    Label(P1, text="Managment 2 Pin",width=15 ,anchor=E ,bg="cadet blue" ,bd=2).grid(row=5,column=1)
    M2P = Entry(P1, bd=2)
    M2P.grid(row=5,column=2)
    
    Label(P1, text="Cashier 1 Pin",width=15 ,anchor=E ,bg="cadet blue" ,bd=2).grid(row=6,column=1)
    C1P = Entry(P1, bd=2)
    C1P.grid(row=6,column=2)
    
    Label(P1, text="Cashier 2 Pin",width=15 ,anchor=E ,bg="cadet blue" ,bd=2).grid(row=7,column=1)
    C2P = Entry(P1, bd=2)
    C2P.grid(row=7,column=2)

    Label(P1, text="Restorand Buttons",width=15 ,anchor=E ,bg="cadet blue" ,bd=2).grid(row=8,column=1)
    var2 = IntVar()
    R3 = Radiobutton(P1,text="Yes",bg="cadet blue" , variable=var2, value=1)
    R3.grid(row=8,column=2)
    R4 = Radiobutton(P1,text="No",bg="cadet blue" , variable=var2, value=2)
    R4.grid(row=8,column=3)
    




    def DONE():
        c.execute('''CREATE TABLE IF NOT EXISTS Settings(ID REAL, Name TEXT, Value REAL, OTHER TEXT)''')
        conn.commit()
        c.execute('''INSERT INTO Settings(ID, Name, Value, OTHER) VALUES(?, ? ,? ,?)''',("1", "Print to Printer", (var1.get()), "N"))
        conn.commit()
        c.execute('''INSERT INTO Settings(ID, Name, Value, OTHER) VALUES(?, ? ,? ,?)''',("2", "Admin Pin", "1", (AP.get())))
        conn.commit()
        c.execute('''INSERT INTO Settings(ID, Name, Value, OTHER) VALUES(?, ? ,? ,?)''',("3", "Managment 1 Pin", "1", (M1P.get())))
        conn.commit()
        c.execute('''INSERT INTO Settings(ID, Name, Value, OTHER) VALUES(?, ? ,? ,?)''',("4", "Managment 2 Pin", "1", (M2P.get())))
        conn.commit()
        c.execute('''INSERT INTO Settings(ID, Name, Value, OTHER) VALUES(?, ? ,? ,?)''',("5", "Cashier 1 Pin", "1", (C1P.get())))
        conn.commit()
        c.execute('''INSERT INTO Settings(ID, Name, Value, OTHER) VALUES(?, ? ,? ,?)''',("6", "Cashier 2 Pin", "1", (C2P.get())))
        conn.commit()
        c.execute('''INSERT INTO Settings(ID, Name, Value, OTHER) VALUES(?, ? ,? ,?)''',("7", "Restorant Buttons", (var2.get()), "N"))
        conn.commit()
        P1.destroy()




    Button(P1, text="Done", width=10, height=1, fg="white", bg="green", command=DONE, bd=2).grid(row=100,column=1)


##FIRSTTIME()
