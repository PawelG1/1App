import mysql.connector

  
dataBase = mysql.connector.connect(
    host = "172.28.96.170",
    user = "root",
    port = "3306",
    database = "zaglowka")
         
mycursor = dataBase.cursor()

comm = "SELECT * FROM pos_stored WHERE id = 2"
mycursor.execute(comm)
result = mycursor.fetchone()

data = {
    "rudder": result[0],
    "navi_lights": result[2],
    "motor ": result[3],
    "anchor": result[4],
    "boom_angle": result[5]
}


print(data)