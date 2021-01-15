import sqlite3


def create_table():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("create table if not exists store (item TEXT, quantity INTEGER, price REAL)")
    con.commit()
    con.close()


def insert(item, quantity, price):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("insert into store values (?, ?, ?)", (item, quantity, price))
    con.commit()
    con.close()


def show_data():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("select * from store")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    con.commit()
    con.close()


create_table()
insert('Coffee', 2, 250.26)
show_data()