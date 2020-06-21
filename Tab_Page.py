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

import Error

import tkinter as tk
from tkinter import ttk


##Page1 = Tk()
##Page1.title("Shop Database")
##Page1.configure(background="#BEBEBE")
##Page1.geometry("500x300+300+300")
##Page1.iconbitmap('Till.ico')
####Page1.attributes("-topmost", True)

import tkinter as tk
from tk_html_widgets import HTMLLabel

##<img src="Till.jpg" style="width:104px;height:142px;">

root = tk.Tk()
html_label = HTMLLabel(root, html='''<img src="Till.jpg" style="width:104px;height:142px;">''')
html_label.pack(fill="both", expand=True)
html_label.fit_height()
root.mainloop()
