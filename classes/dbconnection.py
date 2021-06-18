import sqlite3

from sqlite3 import Error

def sql():
    try:
        con = sqlite3.connect("../database/rushhour.db")
        con.row_factory = sqlite3.Row
        db = con.cursor()
        return db
    except Error:
        print(Error)