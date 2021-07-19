# update records in pos_stored structure 
import mysql.connector
  
dataBase = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    database = "zaglowka")
         
"""
def update(u_rudder, u_navi, u_motor, u_anchor, u_boom):
    mycursor = dataBase.cursor()

    # mycursor.execute("SELECT * FROM pos_stored")
    # result = mycursor.fetchone()
    # print(result)
    u_comm = "UPDATE pos_stored SET rudder_angle = %s, navi_lights = %s, motor = %s, anchor= %s, boom_angle= %s  WHERE id = %s"
    u_comm_values = (u_rudder, u_navi, u_motor, u_anchor, u_boom, "2")
    mycursor.execute(u_comm, u_comm_values)
    dataBase.commit()
    print(mycursor.rowcount, "records affected")
"""

def update_states(u_navi, u_motor, u_anchor):
    mycursor = dataBase.cursor()

    # mycursor.execute("SELECT * FROM pos_stored")
    # result = mycursor.fetchone()
    # print(result)
    u_comm = "UPDATE pos_stored SET navi_lights = %s, motor = %s, anchor= %s  WHERE id = %s"
    u_comm_values = (u_navi, u_motor, u_anchor, "2")
    mycursor.execute(u_comm, u_comm_values)
    dataBase.commit()
    print(mycursor.rowcount, "|states| records affected")

def update_sliders(u_rudder, u_boom):
    mycursor = dataBase.cursor()

    # mycursor.execute("SELECT * FROM pos_stored")
    # result = mycursor.fetchone()
    # print(result)
    u_comm = "UPDATE pos_stored SET rudder_angle = %s, boom_angle= %s  WHERE id = %s"
    u_comm_values = (u_rudder, u_boom, "2")
    mycursor.execute(u_comm, u_comm_values)
    dataBase.commit()
    print(mycursor.rowcount, "|sliders| records affected")