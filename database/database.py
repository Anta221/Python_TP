import sqlite3 
import json


connection = sqlite3.connect('database/database.db')
c = connection.cursor()
    
  
#insert into information mobil scann
def insert_information(resultat):
    for device in resultat:
        c.execute("INSERT INTO information VALUES ( null , :id, :name , :rssi);", device)
        c.connection.commit()



#insert into localisation 
def insert_localisation(liste_local):
        c.execute("INSERT INTO localisation VALUES ( null , :ip, :country, :loc, :timezone);", liste_local)
        c.connection.commit()




    

#affiche les données de la base    
def select_all_():
    c.execute("SELECT * FROM information")
    rows = c.fetchall()
    for row in rows:
        print(row)
    
print(select_all_())

   




   


