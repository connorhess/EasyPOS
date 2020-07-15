import sqlite3
from tkinter import *
from tkinter import filedialog
import time
import random
from tkinter import messagebox
from openpyxl import Workbook
from openpyxl import load_workbook
import tempfile
import os
from functools import partial
from prettytable import PrettyTable
from tkinter.font import Font
from os.path import join as pjoin
import Error
from tkinter import ttk


conn = sqlite3.connect('Shop_Database.db')
c = conn.cursor()

def PASS(Table,NO):
    TableNumberGenerate(Table,NO)

def Config1():
    c.execute('''CREATE TABLE IF NOT EXISTS Tables(Item_PLU REAL, Item_Name TEXT, Item_Price INT, QTY INT, FPrice INT, Table_No INT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Starters(Item_PLU REAL, Item_Name TEXT, Item_Price REAL, Menu INT)''')

def TableNumberAdd(B1,B2,B3,B4,TableNO,B6):
    c.execute('''INSERT INTO Tables(Item_PLU, Item_Name, Item_Price, QTY, Table_No, FPrice) VALUES(?, ? ,? ,? ,? ,?)''',(B1, B2, B3, B4, TableNO, B6))
    conn.commit()


def ItemAdd(B1,B2,B3,B4):
    c.execute('''INSERT INTO Starters(Item_PLU, Item_Name, Item_Price, Menu) VALUES(?, ? ,? ,?)''',(B1, B2, B3, B4))
    conn.commit()

def Generate_Tab(Page):
    pass

def Generate_Button(Name):
    pass

def donothing():
    pass

def RSYS(Logged_In, Page):
    Page_main = Tk()
    Page_main.title("Item Database")
    Page_main.configure(background="#BEBEBE")
    Page_main.attributes("-fullscreen", True)
    Page_main.attributes("-topmost", True)
    Page_main.update_idletasks()

    toolbar = Frame(Page_main, height=100, width=(Page_main.winfo_width()), bg="#E9E9E9")
    toolbar.grid(row=0,column=0)

    Body = Frame(Page_main, height=(Page_main.winfo_height()-100), width=(Page_main.winfo_width()), bg="#E9E9E9")
    Body.grid_propagate(0)
    Body.grid(row=1,column=0)

    tabControl = ttk.Notebook(Page)
    U = 0
    c.execute("SELECT * FROM Cashiers")
    for User in c.fetchall():
        U += 1
        if U == 1:
            tab1 = ttk.Frame(tabControl)
            tabControl.add(tab1, text=(User[1]))
        elif U == 2:
            tab2 = ttk.Frame(tabControl)
            tabControl.add(tab2, text=(User[1]))
        elif U == 3:
            tab3 = ttk.Frame(tabControl)
            tabControl.add(tab3, text=(User[1]))
        elif U == 4:
            tab4 = ttk.Frame(tabControl)
            tabControl.add(tab4, text=(User[1]))
        elif U == 5:
            tab5 = ttk.Frame(tabControl)
            tabControl.add(tab5, text=(User[1]))




    tabControl.pack(expand=1, fill="both")
    Page_main.mainloop()

if __name__ == '__main__':
    RSYS("Connor", "Page1")
