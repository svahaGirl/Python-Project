#!usr/bin/python3
# insertingData.py

import sqlite3 as lit
myuser = (
 
    (1, 101, 'Parwiz', 'par@gmail.com', 'ip: 123.245.256', 'This is a Spyware', 'note','10/12/2020'),
    (2, 102, 'John', 'john@gmail.com','pending','This is a Win32.','note','08/14/2020'),
    (3, 103, 'Bob', 'bob@gmail.com','completed','Adware','note','06/03/2020'),
    (4, 104, 'Tom', 'tom@gmail.com','next task','wannaCry Ransomware','note','07/17/2020'),
 
)
db = lit.connect('dns_search.db')
 
with db:
    cur = db.cursor()
    cur.executemany('INSERT INTO users VALUES (?,?,?,?,?,?,?,?)', myuser)
 
    print("Data Inserted Successfully")