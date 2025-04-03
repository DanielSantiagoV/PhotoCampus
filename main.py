from menu import menu_principal, pedir_opcion
from registrar import registrar_servicios_fotograficos, eliminar_servicio_fotografico, modificar_servicio
from datos import *

cargar_datos("fotografia.json")

while True:
    menu_principal()
    opc = pedir_opcion()
    match opc:
        case 1:
            registrar_servicios_fotograficos()
        case 2:
            modificar_servicio()
        case 3:
            eliminar_servicio_fotografico()
        case 4:
            print("Saliendo...")
            break
