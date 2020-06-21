import sqlite3
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import time
from datetime import timedelta
import datetime
from idle_time import IdleMonitor
import random
from prettytable import PrettyTable
from functools import partial
import sys
import os
import tkinter as tk
from tkinter import ttk
import requests



def Update():
    pass

def Update_manager():
    requests.get('https://raw.githubusercontent.com/vsantiago113/Tkinter-MyTestApp/master/version.txt')
    f1 = open(r"C:\Users\conno\OneDrive\Documents\GitHub\EasyPOS\version.txt", "r")
    print(f1.read())
    f2 = open("version.txt", "r")
    print(f2.read())
    if float(f1.read()) > float(f2.read()):
        MsgBox = messagebox.askquestion ('Warning','Are you sure you want to Delete All\nThis will delete everything and can not be undone',icon = 'warning')
        if MsgBox == 'yes':
            Update()
        else:
            import login
            login.Login_Page()



Update_manager()
