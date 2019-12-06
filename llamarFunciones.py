import os
import time
import CrecuperarTodoTabla
import BinsertarFilas
import DactualizarNombre
import interface
import FborrarFilas
import EbuscarNombreTelefono
import sound

os.system('cls')  #tratando de limpiar la pantalla, pero no recuerdo bien.
time.sleep(2)

interface.seleccion_menu1()

while True:
    print("")
    seleccione = input("[7] Volver al menu inicial\nSeleccione del menu: ")

    if seleccione == '1':
        sound.sound8HadouKen()
        BinsertarFilas.insertarDatos()

    elif seleccione == '2':
        sound.soun4JujuJAja()
        CrecuperarTodoTabla.recuperarTodo()

    elif seleccione == '3':
        sound.soun3Austin()
        EbuscarNombreTelefono.bucarPornombreOtelefono()

    elif seleccione == '4':
        sound.sound6Guille()
        DactualizarNombre.actualizarNombre()

    elif seleccione == '5':
        sound.soun4JujuJAja()
        FborrarFilas.eliminarNumOrden1()

    elif seleccione == '7':
        interface.seleccion_menu1()
        sound.sound7ShoryuKen()
    elif seleccione == '6':
        sound.soun2fishim()
        break
    else:
        print("Ingrese solo datos del MENU")

