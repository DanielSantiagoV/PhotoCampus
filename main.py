from menu import menu_principal, pedir_opcion
from registrar import registrar_servicios_fotograficos
from datos import *

cargar_datos("fotografia.json")

while True:
    menu_principal()
    opc = pedir_opcion()
    match opc:
        case 1:
            registrar_servicios_fotograficos()
        case 2:
            print("Modificar")
        case 3:
            print("Eliminar")
        case 4:
            print("Saliendo...")
            break
