from menu import menu_principal, pedir_opcion
from registrar import registrar_servicios_fotograficos , modificar

while True:
    menu_principal()
    opc = pedir_opcion()
    match opc:
        case 1:
            print("Registrar servicios fotograficos")
        case 2:
            modificar()
        case 3:
            print("Eliminar")
        case 4:
            print("Saliendo...")
            break

