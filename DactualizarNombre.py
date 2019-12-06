import sqlite3


def actualizarNombre():
    conexion = sqlite3.connect("AgendaTelefonica.db")  # ESTABLECER CONEXION CON LA BASE DE DATOS
    codigo1 = int(input("Selecciones NUM de ORDEN actualizar: "))
    nombre1 = str(input("Cambiele el nombre: "))

    conexion.execute('UPDATE agenda set nombre =? WHERE codigo=?', (nombre1.upper(),codigo1))

    conexion.commit()
    conexion.close()
