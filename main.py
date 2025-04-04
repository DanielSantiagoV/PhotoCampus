from menu import menu_principal, pedir_opcion
from registrar import registrar_servicios_fotograficos, eliminar_servicio_fotografico, modificar_servicio
from datos import *

cargar_datos("fotografia.json")

while True:
    menu_principal()
    try:
        opc = pedir_opcion()
    except ValueError:
        print("Error: Debe ingresar una opción válida.")
        continue
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
