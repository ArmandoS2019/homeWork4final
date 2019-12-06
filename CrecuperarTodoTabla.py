import sqlite3

def recuperarTodo():
    conexion = sqlite3.connect("AgendaTelefonica.db")
    cursor = conexion.execute("SELECT codigo,nombre,telefono FROM agenda")
    print("Orden |    Nombres                |Telefonos")
    print("--------------------------------------------")
    for fila in cursor:

        print(f"No. {fila[0]}     {fila[1]}     {fila[2]}")

    conexion.close()