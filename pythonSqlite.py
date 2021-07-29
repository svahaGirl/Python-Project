#!usr/bin/python3
# Creating Tables in Python Sqlite

import sqlite3 as lit

def main():
    try:
        db = lit.connect('dns_search.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE users (id INT, Case_Number INT,name TEXT, email TEXT, DNS_Search TEXT,VirusTotal_Indicator BLOB, note TEXT, timeStamp DATETIME)"
 
        cur.execute(tablequery)
        print("Table Created Successfully")
        
    except lit.Error as e:
        print("Unable To Create Table")
 
    finally:
        db.close()
if __name__ == "__main__":
        main()

