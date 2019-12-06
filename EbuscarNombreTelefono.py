import sqlite3

def bucarPornombreOtelefono():
    conexion = sqlite3.connect("AgendaTelefonica.db")
    codigo = input("Seleccion el codigo del nombre a presentar: ")

    cursor = conexion.execute('SELECT codigo,nombre,telefono FROM agenda WHERE codigo=?',(codigo, ))

    datos = cursor.fetchall()
    for filas in datos:
        print()
        print("AGENDA TELELEFONICA".center(60,"="))
        print(f"Num. Orden: {filas[0]} Nombre:{filas[1]} Telefono:{filas[2]}")

    conexion.close()
