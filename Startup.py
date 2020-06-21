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


from licensing.models import *
from licensing.methods import Key, Helpers


home = os.path.expanduser('~')

__author__ = 'Connor Hess'
__copyright__ = 'Copyright (C) 2020, Connor Hess'
__credits__ = ['Connor Hess']
__license__ = 'The MIT License (MIT)'
version = (0.75)
__maintainer__ = 'Connor Hess'
__email__ = 'hessconnor41@gmail.com'
__status__ = 'Alpha'

_AppName_ = 'EasyPOS'

Downloads_location = os.path.join(home, 'Downloads')

def Update():
    win32api.ShellExecute(0, 'open', '{Downloads_location}\\setup.msi', None, None, 10)

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


RSAPubKey = '''<RSAKeyValue>
<Modulus>hWaA36UiW+Xt+NEqmt6XI1+1WV+hWbi8+C1IgI4NmvNP01Gb7ZjFcUUQZQBxwXfLTvSHJlAlUlbGk26n3Z0n5wrDMIPCB/x/EbI9yIueedKJB9VHMonIpXvAT+oSdoechFvasiE1q7khGUBLfEhsnYP2Q2JbQ2hToZ4eb+LqjuVOc54RkIup1OJ+Dur+WfqN+43QpLFQoFA7ydAg6gKpmGUKTgWR3q5UhDhHwIC1xYFKVnXA3BXVXOwTVa7D5tCCO/SauoetcXwPJwO0QXa7hQAR9fUCq25sy4Nm+hFPUYTs5UAO+H10ysenUqCFddhfrSzAakZzWpAnvZyDxPb5tw==
</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>'''
auth = "WyIyMzQ5MSIsIk9MY2xicDc5dVE5OUVmc0pFcWUwU2ZNTnB1c1F1dzVkeWtVSG5sTzgiXQ=="

result = Key.activate(token=auth,\
                   rsa_pub_key=RSAPubKey,\
                   product_id=6725, \
                   key="KZUGV-POPFG-DPCDH-USUAB",\
                   machine_code=Helpers.GetMachineCode())

if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
    # an error occurred or the key is invalid or it cannot be activated
    # (eg. the limit of activated devices was achieved)
    print("The license does not work: {0}".format(result[1]))
else:
    # everything went fine if we are here!
    print("The license is valid!")
    Update_manager()





