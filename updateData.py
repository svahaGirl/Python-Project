#!usr/bin/python3
# updateData.py

import sqlite3 as lit


db = lit.connect('dns_search.db')

with db:

    newname = "updated name"
    user_id = 1

    cur = db.cursor()
    cur.execute('UPDATE users SET name = ? WHERE id = ?', (newname, user_id))
    db.commit()
    print("Data Updated Successfully")