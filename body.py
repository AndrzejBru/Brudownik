# Podpowiedz https://www.youtube.com/watch?v=8y3JHCnVPMw


from tkinter import *
from tkinter import ttk
import tkinter.messagebox
#from PIL import ImageTK, Image
import sqlite3

root = Tk()
root.title('Brudownik')
root.geometry('850x550')

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

# Create Frames 

MainFrame = Frame(root, bg ="cadet blue")
MainFrame.grid()

TitFrame = Frame (MainFrame, bd=2, padx=60, pady=8, bg="Ghost White", relief=RIDGE )
TitFrame.pack(side=TOP)

lblTit = Label(TitFrame, font=('arial', 40, 'bold'), text="Program do ubrań", bg="Ghost White")
lblTit.grid()

Data = Frame(MainFrame, bd=1, width=700, height=400, padx=20, pady=20, relief=RIDGE, bg="red")
Data.pack(side=LEFT)

DataFrame = Frame(Data, bd=1, width=300, height=400, padx=20, pady=20, relief=RIDGE, bg="blue")
DataFrame.pack(side=LEFT)

DataView = Frame(Data,  bd=1, width=400, height=400, padx=20, pady=20, relief=RIDGE, bg="cadet blue")
DataView.pack(side=RIGHT)

# Create Submit Function For database
def submit():
        conn = sqlite3.connect('ubrania.db')
        c = conn.cursor()

        # Insret Into Table

        c.execute("INSERT INTO addresses VALUES (:numer, :ubranie, :nuemr_ubr, :data_w, :data_od, :data_zwr)",
                 {
                        'numer': numer.get(),
                        'ubranie': ubranie.get(),
                        'nuemr_ubr': numer_ubr.get(),
                        'data_w': data_w.get(),
                        'data_od': data_od.get(),
                        'data_zwr': data_zwr.get()
                 })

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
        
        c = conn.cursor()

        c.execute("SELECT * FROM addresses")

        records = c.fetchall()
        print(records)
        print_records = ''
        for record in records:
                #print_records += str(record) + str(record[5]) +"\n"
                tree.insert('', Tk.END, values=record)

        view_label = Label(DataView, text=print_records)
        view_label.grid(row=8, columnspan=2, column=0)
        conn.commit()

        conn.close()

# Możliwe błędne działanie wyświetlania tabeli DO SPRAWDZENIA

numer = Entry(DataFrame, width=30)
numer.grid(row=0, column=1, padx=20)

ubranie = Entry(DataFrame, width=30)
ubranie.grid(row=1, column=1)

numer_ubr = Entry(DataFrame, width=30)
numer_ubr.grid(row=2, column=1)

data_w = Entry(DataFrame, width=30)
data_w.grid(row=3, column=1)

data_od = Entry(DataFrame, width=30)
data_od.grid(row=4, column=1)

data_zwr = Entry(DataFrame, width=30)
data_zwr.grid(row=5, column=1)

#Create Text Box Lablels

numer_label = Label(DataFrame, text='id')
numer_label.grid(row=0, column=0)

ubranie_label = Label(DataFrame, text='Typ ubrania')
ubranie_label.grid(row=1, column=0)

numer_ubr_label = Label(DataFrame, text='Numer ubrania')
numer_ubr_label.grid(row=2, column=0)

data_w_label = Label(DataFrame, text='Data wydania ubrania')
data_w_label.grid(row=3, column=0)

data_od_label = Label(DataFrame, text='Data oddania do prania')
data_od_label.grid(row=4, column=0)

data_zwr_label = Label(DataFrame, text='Data zwrotu z pralni')
data_zwr_label.grid(row=5, column=0)

# Create ListBox $ Scrollbar Widget

#DataFrameRIGHT = Frame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=3, bg='Ghost Wite')
#DataFrameRIGHT.grid(row=0, column=3)

#scrollbar = Scrollbar(DataFrameRIGHT)
#scrollbar.grid(row=0, column=3, sticky='ns')

#studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
#studentlist = Listbox(DataView, width=41, height=20, font=('arial', 12, 'bold'), Text="HELLO")
#studentlist.grid(row=0, column=4)
#scrollbar.config(command= studentlist.yview)
columns = ('id', 'Typ ubrania', 'Numer ubrania', 'Data wydania ubrania', 'Data oddania do prania', 'Data zwrotu z pralni')
tree = ttk.Treeview(DataView, columns=columns, show='headings')
tree.heading('id', text='id')
tree.heading('Typ ubrania', text='Typ ubrania')
tree.heading('Numer ubrania', text='Numer ubrania')
tree.heading('Data wydania ubrania', text='Data wydania ubrania')
tree.heading('Data oddania do prania', text='Data oddania do prania')
tree.heading('Data zwrotu z pralni', text='Data zwrotu z pralni')


# Create Submit Butto

submit_btn = Button(DataFrame, text="Dodaj ubranie", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create View Butto

view_btn = Button(DataFrame, text="Pokaż ubrnia", command=View)
view_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Commit Changes
conn.commit()
# Run App
root.mainloop()
