from menu import menu_principal, pedir_opcion

while True:
    menu_principal()
    opc = pedir_opcion()
    match opc:
        case 1:
            print("Registrar servicios fotograficos")
        case 2:
            print("Modificar")
        case 3:
            print("Eliminar")
        case 4:
            print("Saliendo...")
            break
