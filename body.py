from tkinter import *
#from PIL import ImageTK, Image
import sqlite3

root = Tk()
root.title('Brudownik')
root.geometry('800x400')

# Database

conn = sqlite3.connect('ubrania.db')

# Create cursor

c = conn.cursor()

# Create table

c.execute("""CREATE TABLE IF NOT EXISTS addresses (
        id integer,
        typ_ubrania text,
        numer_ubrania integer,
        data_wydania integer,
        data_oddania integer,
        data_zwrotu integer
        )""")

# Create Submit Function For database
def submit():
        conn = sqlite3.connect('ubrania.db')
        c = conn.cursor

        # Insret Into Table

        c.execute("INSERT INTO addresses VALUES (:nuemr, :ubranie, :nuemr_ubr")

        # Comit Changers
        
        conn.commit()
        
        # Close Connection
        
        conn.close()
        
        # Clean Wiget

        numer.delete(0, END)
        ubranie.delete(0, END)
        numer_ubr.delete(0, END)
        data_w.delete(0, END)
        data_od.delete(0, END)
        data_zwr.delete(0, END)

# Create View function For database

def View():

        conn = sqlite3.connect('ubrania.db')
        
        c = conn.cursor

        c.execute("SELECT * FROM ubrania.db")

        rows = c.fetchall()    

        for row in rows:

                print(row) 

                tree.insert("", tk.END, values=row)        

        c.close()

numer = Entry(root, width=30)
numer.grid(row=0, column=1, padx=20)

ubranie = Entry(root, width=30)
ubranie.grid(row=1, column=1)

numer_ubr = Entry(root, width=30)
numer_ubr.grid(row=2, column=1)

data_w = Entry(root, width=30)
data_w.grid(row=3, column=1)

data_od = Entry(root, width=30)
data_od.grid(row=4, column=1)

data_zwr = Entry(root, width=30)
data_zwr.grid(row=5, column=1)

#Create Text Box Lablels

numer_label = Label(root, text='id')
numer_label.grid(row=0, column=0,)

ubranie_label = Label(root, text='Typ ubrania')
ubranie_label.grid(row=1, column=0)

numer_ubr_label = Label(root, text='Numer ubrania')
numer_ubr_label.grid(row=2, column=0)

data_w_label = Label(root, text='Data wydania ubrania')
data_w_label.grid(row=3, column=0)

data_od_label = Label(root, text='Data oddania do prania')
data_od_label.grid(row=4, column=0)

data_zwr_label = Label(root, text='Data zwrotu z pralni')
data_zwr_label.grid(row=5, column=0)

# Create Submit Butto

submit_btn = Button(root, text="Dodaj ubranie", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create View Butto

view_btn = tk.Button(text="Pokaż ubrnia", command=View)

view_btn.pack(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Commit Changes
conn.commit()
# Run App
root.mainloop()