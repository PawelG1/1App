# get position from db --  PG
import mysql.connector
state = 1
try:
    dataBase = mysql.connector.connect(
        host = "172.28.96.170",
        user = "root",
        port = "3306",
        database = "zaglowka")
         
    mycursor = dataBase.cursor(buffered=True)
except:
    state = 0
    pass

def get_pos():
    mycursor.execute("SELECT * FROM loc")
    pos = mycursor.fetchone()
    dataBase.commit()
    return pos
