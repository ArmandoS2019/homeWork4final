import sqlite3

def createDb():
    conexion = sqlite3.connect("AgendaTelefonica.db")
    try:
        #CAMPOS:
        # Name              Type
        # codigo            int primary key
        # descripcion       Text
        # Precio            Real
        conexion.execute("""CREATE TABLE agenda (
                                  codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                                  nombre TEXT UNIQUE, 
                                  telefono INTEGER
                            )""")
        print("se creo la tabla agenda")
    except sqlite3.OperationalError:
        print("La tabla agenda ya existe")
    conexion.close()


