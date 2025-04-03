from datos import fotografia, cargar_datos, guardar_datos
from datos import cargar_datos

def registrar_servicios_fotograficos():
    id = f"F-(len(fotografia)+1:03d)"
    
    nombre = input("ingrese el nombre del paquete fotografico: ")
    precio = float(input("ingrese el precio del paquete fotografico: "))

    while True:
        tipo = int(input("Elija tipo de evento segun corresponda:\n1. Boda\n2. Retrato\n3. Producto"))
        if tipo == 1:
            evento = "Boda"
            break
        elif tipo == 2:
            evento = "Retrato"
            break
        elif tipo == 3:
            evento = "Producto"
            break
        else:
            print("Opción no válida. Intente nuevamente.")

    duracion = int(input("Ingrese la duración del servicio en horas: "))
    fotografia = {
        "ID": id,
        "nombre": nombre,
        "precio": precio,
        "evento": evento,
        "duracion": duracion
    }

    print("Servicio fotográfico registrado con éxito.")
    

    def modificar_servicio():
        """Modifica un pedido existente"""
        fotografia = cargar_datos("fotografia.json")

        if not fotografia:
            print("\n⚠ No hay pedidos registrados")
            return

        codigo = input("\nIngrese el código del pedido a editar: ")
        nombre = input("Ingrese el nombre del paquete fotográfico: ")
        precio = float(input("Ingrese el precio del paquete fotográfico: "))

        while True:
            tipo = int(input("Elija tipo de evento según corresponda:\n1. Boda\n2. Retrato\n3. Producto"))

            if tipo == 1:
                evento = "Boda"
                break
            elif tipo == 2:
                evento = "Retrato"
                break
            elif tipo == 3:
                evento = "Producto"
                break
            else:
                print("Opción no válida. Intente nuevamente.")

        duracion = int(input("Ingrese la duración del servicio en horas: "))
        fotografia = {
            "ID": codigo,
            "nombre": nombre,
            "precio": precio,
            "evento": evento,
            "duracion": duracion
        }



