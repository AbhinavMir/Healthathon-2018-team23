import sqlite3
import random
conn = sqlite3.connect('med.db')
c=conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS doctor(id INTEGER PRIMARY KEY,name TEXT,spec TEXT,adr TEXT,num INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS patients(id INTEGER PRIMARY KEY,name TEXT,wt TEXT,age TEXT,grp INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS recp(id INTEGER PRIMARY KEY,prob TEXT,diag TEXT,pres TEXT,dat date,doc text,patid integer primary key,docid integer)')

create_table()



conn.commit()
conn.close()
