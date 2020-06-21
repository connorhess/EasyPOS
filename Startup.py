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
import webbrowser
import win32api
import login


__author__ = 'Connor Hess'
__copyright__ = 'Copyright (C) 2020, Connor Hess'
__credits__ = ['Connor Hess']
__license__ = 'The MIT License (MIT)'
version = (0.75)
__maintainer__ = 'Connor Hess'
__email__ = 'hessconnor41@gmail.com'
__status__ = 'Alpha'

_AppName_ = 'EasyPOS'


def Update():
    win32api.ShellExecute(0, 'open', f'tmp\\{_AppName_}.msi', None, None, 10)

def Update_manager(TEXT="Checking for update"):
    Page1 = Tk()
    Page1.title(TEXT)
    Page1.configure(background="#BEBEBE")
    Page1.iconbitmap('Till.ico')
    Page1.attributes("-topmost", True)
    Label(Page1, text=(TEXT+"\n\nMade By Connor Hess  V" + str(version)), fg="white", bg="gray").pack()
    
    response = requests.get('https://raw.githubusercontent.com/connorhess/EasyPOS/master/version.txt')
    data = response.text
    print(data)
    if float(data) > version:
        MsgBox = messagebox.askquestion ('Update!', f'{_AppName_} {version} needs to update to version {data}',icon = 'warning')
        if MsgBox == 'yes':
            webbrowser.open_new_tab('https://github.com/connorhess/EasyPOS/raw/master/'
                                                'Update/Output/setup.msi?raw=true')
            Page1.destroy()
            Update()
        else:
            Page1.destroy()
            login.Login_Page()
    else:
        Page1.destroy()
        login.Login_Page()



Update_manager()
