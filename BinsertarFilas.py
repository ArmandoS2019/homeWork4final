import sqlite3

def insertarDatos():
    try:
        print("INGRESAR DATOS A LA AGENDA")
        nombre = input("Nombre: ")
        nombre.upper()
        telefono = int(input("Telefono: "))

        if nombre and telefono:

            print()

        conexion = sqlite3.connect("AgendaTelefonica.db") #ESTABLECER CONEXION CON LA BASE DE DATOS

        conexion.execute('''INSERT INTO agenda
                        (nombre,telefono)
                         VALUES (?,?)''',
                        (nombre.upper().ljust(12), str(telefono).rjust(12)))


        conexion.commit()
        conexion.close()
    except: print('''ALGO ESTA MAL, 
                                !*! AVISO IMPORTANTE !*!:
                 
                 1- No se permite ingresar en la agenda nombres repetidos .
                 2- Los nombres solo deben contener letras [Az-Za].
                 3- El telefono solo debe  contener numeros [0-9].
                 
                 Gracias por su compresion''')

