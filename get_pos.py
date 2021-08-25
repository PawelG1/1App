# get position from db --  PG
import mysql.connector

dataBase = mysql.connector.connect(
    host = "172.28.96.170",
    user = "root",
    port = "3306",
    database = "zaglowka")
         
mycursor = dataBase.cursor()

def get_pos():
    mycursor.execute("SELECT * FROM localisation")
    pos = mycursor.fetchone()
    dataBase.commit()
    return pos
