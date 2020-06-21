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


__author__ = 'Connor Hess'
__copyright__ = 'Copyright (C) 2020, Connor Hess'
__credits__ = ['Connor Hess']
__license__ = 'The MIT License (MIT)'
__version__ = (0.75)
__maintainer__ = 'Connor Hess'
__email__ = 'hessconnor41@gmail.com'
__status__ = 'Alpha'



def Update():
    pass

def Update_manager():
    response = requests.get('https://github.com/connorhess/EasyPOS/blob/master/version.txt')
    print(response)
    data = response.text
    print(data)
##    if float(data) > __version__:
##        MsgBox = messagebox.askquestion ('Warning','Are you sure you want to Delete All\nThis will delete everything and can not be undone',icon = 'warning')
##        if MsgBox == 'yes':
##            Update()
##        else:
##            import login
##            login.Login_Page()



Update_manager()
