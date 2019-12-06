import sqlite3 
import requests
import json



try:
    connection = sqlite3.connect('database/database.db')
    c = connection.cursor()
    
    c.execute("""
    CREATE TABLE IF NOT EXISTS information (
        id text,
        identifiant text,
        nom text,
        rssi text
    )""")

    r = requests.get('http://swiv.outofpluto.com:5000/api/devices')

    with open("/Users/lmarlene/Desktop/Python_TP/test.json" , "wb") as f:
        data = f.write(r, json.load(f))
        #data = json.load(rf)
    print(data)

    #data = { "id": c.lastrowid ,  "identifiant": "identifiant"    , "nom": "nom3" , "rssi": "TRFH45665Tp"    }
    c.execute("INSERT INTO information VALUES ( :id, :identifiant,  :nom , :rssi)" , data)
    c.connection.commit()
    
    
    def select_all_():
        c.execute("SELECT * FROM information")
        rows = c.fetchall()
        for row in rows:
            print(row)
    
    print(select_all_())

   


except Exception  as e:
    print("[ERREUR]:" , e)
finally:
    c.connection.close()



   


