##from tkinter import * # import everything from tkinter
##
##box = Tk() #Create a root window
##
##some_var = StringVar(box) #That holds a string; (the default value is an empty string)
##some_var.set("1") #here we set the value
##x = OptionMenu(box, some_var, "1", "2", "3") #OptionMenu class helps to create popmenu
##x.pack() #Pack PACKS widgets in rows or columns.
##
##












import sqlite3
from datetime import timedelta, date


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2020, 6, 1)
end_date = date(2020, 6, 30)
for single_date in daterange(start_date, end_date):
    print(single_date.strftime("%d-%m-%Y"))
    Date_query = (single_date.strftime("%d-%m-%Y"))
    Total_Day = 0
    c.execute('SELECT Date, Bank FROM CRJ WHERE Date=?',(Date_query,))
    for row in c.fetchall():
        print(row)
        Total_Day += row[1]
    xList.append(Date_query)
    yList.append(Total_Day)
Fig_plot.plot(xList,yList)





L = 0.05
B = 0.08
R = 0.94
T = 0.95
















##import sqlite3
##from tkinter import *
##from tkinter import filedialog
##from tkinter import messagebox
##import time
##from datetime import timedelta
##import datetime
##from idle_time import IdleMonitor
##import random
##from prettytable import PrettyTable
##from functools import partial
##import sys
##import os
##import Error
##import tkinter as tk
##from tkinter import ttk
##from PIL import ImageTk,Image
##import Info
##import matplotlib.pyplot as plt
##import numpy as np
##
##
##
##version = Info.i_version
##
##
##
##from matplotlib.backends.backend_tkagg import (
##    FigureCanvasTkAgg, NavigationToolbar2Tk)
### Implement the default Matplotlib key bindings.
##from matplotlib.backend_bases import key_press_handler
##from matplotlib.figure import Figure






##Page1 = Tk()
##Page1.title("Shop Database")
##Page1.configure(background="#BEBEBE")
##Page1.geometry("700x500+300+300")
##Page1.iconbitmap('Till.ico')
##Page1.attributes("-topmost", True)
##
##
##fig = Figure(figsize=(5, 4), dpi=100)
##t = np.arange(0, 3, .01)
##fig.add_subplot(111).plot([1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8])
##
##canvas = FigureCanvasTkAgg(fig, master=Page1)  # A tk.DrawingArea.
##canvas.draw()
##canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
##
##toolbar = NavigationToolbar2Tk(canvas, Page1)
##toolbar.update()
##canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
##
##
##def on_key_press(event):
##    print("you pressed {}".format(event.key))
##    key_press_handler(event, canvas, toolbar)
##
##
##canvas.mpl_connect("key_press_event", on_key_press)
##
##
##def _quit():
##    root.quit()     # stops mainloop
##    root.destroy()  # this is necessary on Windows to prevent
##                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
##
##
##button = tkinter.Button(master=Page1, text="Quit", command=_quit)
##button.pack(side=tkinter.BOTTOM)
##
##tkinter.mainloop()
## If you put root.destroy() here, it will cause an error if the window is
## closed with the window manager.


















##Keyboard shortcuts
##def on_key_press(event):
##    print("you pressed {}".format(event.key))
##    key_press_handler(event, canvas, toolbar)
##
##
##canvas.mpl_connect("key_press_event", on_key_press)










##
##
##
##
##def graph():
##    house_prices = np.random.normal(200000, 25000, 5000)
##    print(house_prices)
##    plt.hist(house_prices)
##    plt.show()
##
##graph()






















##Open_Photo = Image.open("Till.png")
##
##Resize_Photo = Open_Photo.resize((800, 800), Image.ANTIALIAS)
##
##Photo = ImageTk.PhotoImage(Resize_Photo)
##
##lable = Label(Page1, image=Photo).pack()











##import tkinter as tk
##from tk_html_widgets import HTMLLabel
##
##<img src="Till.jpg" style="width:104px;height:142px;">
##
##root = tk.Tk()
##html_label = HTMLLabel(root, html='''<img src="Till.jpg" style="width:104px;height:142px;">''')
##html_label.pack(fill="both", expand=True)
##html_label.fit_height()
##root.mainloop()
##
