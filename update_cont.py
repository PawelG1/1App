# update records in pos_stored structure PG
import mysql.connector

def connect_to_db(): 
    global mycursor, dataBase
    try:
        dataBase = mysql.connector.connect(
            host = "172.28.96.170",
            user = "root",
            port = "3306",
            database = "zaglowka")
         
        mycursor = dataBase.cursor()
    except:
        print("not connected")

def update_states(u_navi, u_motor, u_anchor):
      
    u_comm = "UPDATE pos_stored SET navi_lights = %s, motor = %s, anchor= %s  WHERE id = %s"
    u_comm_values = (u_navi, u_motor, u_anchor, "2")
    mycursor.execute(u_comm, u_comm_values)
    dataBase.commit()
    print(mycursor.rowcount, "|states| records affected")
    

def update_sliders(u_rudder, u_boom):
    
    u_comm = "UPDATE pos_stored SET rudder_angle = %s, boom_angle= %s  WHERE id = %s"
    u_comm_values = (u_rudder, u_boom, "2")
    mycursor.execute(u_comm, u_comm_values)
    dataBase.commit()
    print(mycursor.rowcount, "|sliders| records affected")

def exit():
    dataBase.close()

