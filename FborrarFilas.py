import sqlite3

def eliminarNumOrden1():
    orden = input("Num de Orden a borrar: ")
    conexion = sqlite3.connect("AgendaTelefonica.db") #ESTABLECER CONEXION CON LA BASE DE DATOS

    sql = f"DELETE FROM agenda WHERE codigo={orden}"
    conexion.execute(sql)

    conexion.commit()
    conexion.close()





