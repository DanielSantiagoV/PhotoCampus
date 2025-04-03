from datos import *

def registrar_servicios_fotograficos():
    id = f"F-{len(fotografia) + 1:03d}" 
    
    nombre = input("ingrese el nombre del paquete fotografico: ")
    precio = float(input("ingrese el precio del paquete fotografico: "))

    while True:
        tipo = int(input("Elija tipo de evento segun corresponda:\n1. Boda\n2. Retrato\n3. Producto\nElija una opcion: "))
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
    fotografia[id] = {
        "nombre": nombre,
        "precio": precio,
        "evento": evento,
        "duracion": duracion
    }
    guardar_datos(fotografia, "fotografia.json")

    print("Servicio fotográfico registrado con éxito.")

def eliminar_servicio_fotografico():
    id = input("Ingrese el ID del servicio fotográfico a eliminar: ")
    if id in fotografia:
        del fotografia[id]
        guardar_datos(fotografia, "fotografia.json")
        print("Servicio fotográfico eliminado con éxito.")
    else:
        print("ID no encontrado.")
    

        

    
    

