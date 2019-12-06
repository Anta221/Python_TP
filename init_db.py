import sqlite3 
import requests
import json


try:
    connection = sqlite3.connect('database/database.db')
    c = connection.cursor()
    
    c.execute("""
    CREATE TABLE IF NOT EXISTS information (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        id text(32),
        name text(32),
        rssi text(32)
    );""")

    c.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pseudo text,
        password text
       
    );""")

    c.execute("""
    CREATE TABLE IF NOT EXISTS localisation (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip text(32),
        country text(32),
        loc text(32),
        timezone text(32)
    );""")

 


except ValueError  as e:
    print("[ERREUR]:" , e)
finally:
    c.connection.close()

