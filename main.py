from menu import menu_principal, pedir_opcion
from registrar import registrar_servicios_fotograficos, eliminar_servicio_fotografico, modificar_servicio, listar_servicios_fotograficos
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
            listar_servicios_fotograficos()
        case 3:
            modificar_servicio()
        case 4:
            eliminar_servicio_fotografico()
        case 5:
            print("Saliendo...")
            break
        case _:
            print("Opción no válida. Intente nuevamente.")
            continue
