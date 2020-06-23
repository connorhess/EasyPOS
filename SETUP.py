import sqlite3


conn = sqlite3.connect('Shop_Database.db')
c = conn.cursor()


def Create_Tables():
    c.execute('''CREATE TABLE IF NOT EXISTS CRJ(ID REAL,Day INTEGER,Month INTEGER,Year INTEGER,Time INTEGER, Date INTEGER, Description TEXT, Amount RAEL, Bank RAEL, Item TEXT, QTY TEXT, Payment_Type TEXT, Cashier TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS "Sales" (
                            "ID"	INTEGER,
                            "Day"	INTEGER,
                            "Month"	INTEGER,
                            "Year"	INTEGER,
                            "Time"	INTEGER,
                            "Date"      INTEGER,
                            "Item"	TEXT,
                            "Price"	INTEGER,
                            "Qty"	INTEGER,
                            "Weight" REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Product_List(Code INT, Price REAL, Item TEXT, Cost_Price REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Customer_List(Code REAL, Name TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS MenuS(Menu_Name TEXT, Menu_Number RAEL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Cashiers(ID REAL, Name TEXT, Password TEXT, Permision REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Scale(Code INTEGER, Name TEXT, Price_per_kg REAL)''')
    

#SETUP.Create_Tables()


#==============================#Shop.py#==============================#
#Main Page
Lable_Place_Time_x = 1500
Lable_Place_Time_y = 30

Frame_F8_R = 1
Frame_F8_C = 0
Frame_F8_Width = 250
Frame_F8_Height = 250
