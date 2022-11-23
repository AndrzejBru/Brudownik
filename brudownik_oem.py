#Import
from datetime import date
import sqlite3
connection = sqlite3.connect("brudownik.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS ubrania (numer_ubrania integer, typ_brania text, data_wczytania integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS pralnia (numer_ubrania integer, data_oddania integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS szafka (numer_ubrania integer, data_odebrania integer)")

def start():
print("..Brudnownik..")
pirnt(" 1 - Stan ubrań")
print(" 2 - Dodaj ubranie do pralni")
print(" 3 - Dodaj ubranie do szafki")

def pralnia():
print(" Podaj numer ubrania")
oddaj_ubranie = input("Podaj numer ubrania")
data = date.today()
oddane_ubranie = (oddaj_ubranie, data)
cursor.executemany("instert into pralnia values (?, ?), oddane_ubranie")

def szafka():
print(" Podaj numer ubrania")
zwrot_ubrania = input("Podaj numer ubrania")
data = date.today()
zwrocone_ubranie = (zwrot_ubrania, data)
cursor.executemany("instert into szafka values (?, ?), zwrocone_ubranie")

def stan():
cursor.execute('SELECT * FROM oddane_ubranie')
print(cursor.fetchall())
cursor.execute('SELECT * FROM zwrocone_ubranie')
print(cursor.fetchall())

connection.close()