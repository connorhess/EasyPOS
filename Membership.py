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

#not Built In
from openpyxl import Workbook
from openpyxl import load_workbook

x = PrettyTable()

YEAR = (time.strftime("%Y"))


def RUN1():
    Page1 = Tk()
    Page1.title("Shop Database")
    Page1.configure(background="cadet blue")
    Page1.geometry("600x400")

    X1 = 100
    Y1 = 50

    Label(Page1, text="Name:", bd=2).place(x=X1,y=Y1)
    e1 = Entry(Page1, bd=2)
    e1.place(x=X1+45,y=Y1)

    Label(Page1, text="Surname:", bd=2).place(x=X1-15,y=Y1+25)
    e2 = Entry(Page1, bd=2)
    e2.place(x=X1+45,y=Y1+25)

    Label(Page1, text="ID Number:", bd=2).place(x=X1-26,y=Y1+50)
    e3 = Entry(Page1, bd=2)
    e3.place(x=X1+45,y=Y1+50)

    Label(Page1, text="Age:", bd=2).place(x=X1+10,y=Y1+75)
    w1 = Spinbox(Page1, from_=1, to=100, width=5)
    w1.place(x=X1+45,y=Y1+75)

    Label(Page1, text="Gender:", bd=2).place(x=X1-7,y=Y1+100)
    var = IntVar()
    R1 = Radiobutton(Page1,text="Male", variable=var, value=5021)
    R1.place(x=X1+45,y=Y1+100)
    R2 = Radiobutton(Page1,text="Female", variable=var, value=2)
    R2.place(x=X1+110,y=Y1+100)


    
    def Done():
        RANDOM = random.randint(1,1000000000)
        AGE1,AGE2,AGE3,AGE4,AGE5,AGE6,GEND1,GEND2,GEND3,GEND4,DN1,DN2,DN3 = e3.get()
        GENDERIN = int(var.get())
        GENDERID = int(GEND1 + GEND2 + GEND3 + GEND4)
        IDBDAY = AGE1 + AGE2 + AGE3 + AGE4 + AGE5 + AGE6
        YEAR1,YEAR2,YEAR3,YEAR4 = YEAR
       
        DY = (AGE1 + AGE2)
        
        print((str(YEAR3) + str(YEAR4)))
        
        if (AGE1 + AGE2) > (str(YEAR3) + str(YEAR4)):
            YY = "19"
        else:
            YY = "20"
        
        IDBDYEAR = (int(str(YY) + AGE1 + AGE2))
        IDAGE = int(YEAR) - (int(str(YY) + AGE1 + AGE2))

        print(YY)

        BDATE = str(IDBDYEAR) + "/" + AGE3 + AGE4 + "/" + AGE5 + AGE6

        print(BDATE)
        
        print (IDAGE)
        print(IDBDYEAR)
        print(IDBDAY)
        print(GENDERID)
        print(GENDERIN)
        if int(w1.get()) < 18 or str(w1.get()) != str(IDAGE) or GENDERIN != GENDERID:
            print("Something is wrong")
        else:
            print("OK")

        #=================Put in DB=========================
            #Birth date         - BDATE
            #Age                - IDAGE
            #Name               - e1.get()
            #Surname            - e2.get()
            #account number     - RANDOM                print on paper
            
        filename = tempfile.mktemp(".txt")
        open (filename, "w").write(Q)
        os.startfile(filename, "print")
        
        print(BDATE)
        print (IDAGE)
        

    Button(Page1, text="Done", width=12, command=Done, bd=2).place(x=1,y=1)


RUN1()

# 7201195021081
