#!usr/bin/python3
# selectData.py

import sqlite3 as lit
 
db = lit.connect('dns_search.db')
 
with db:
    cur = db.cursor()
    selectquery = "SELECT * FROM users"
    cur.execute(selectquery)
 
    rows = cur.fetchall()
 
    for data in rows:
        print(data)