#!usr/bin/python3
#creating sqlite connection

import sqlite3 as lit

def main():
    try:
    db = lit.connect('dns_search.db')
        print("Database created")
    
    except:
        print("failed to create database")
    finally:
        db.close()
    
    
    if __name__ == "__main__":
            main()
