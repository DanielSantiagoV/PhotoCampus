from menu import menu_principal, pedir_opcion
from registrar import *

while True:
    menu_principal()
    opc = pedir_opcion()
    if opc == 1:
        print("Registrar servicios fotograficos")
    elif opc == 2:
        print("Modificar")
        modificar_servicio()
    elif opc == 3:
        print("Eliminar")
    elif opc == 4:
        print("Saliendo...")
        break
