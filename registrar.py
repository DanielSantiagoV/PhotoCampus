from datos import fotografia, guardar_datos


def registrar_servicios_fotograficos():
    id = f"F-{len(fotografia) + 1:03d}" 
    
    nombre = input("ingrese el nombre del paquete fotografico: ").capitalize()
    while True:
        try:
            precio = float(input("ingrese el precio del paquete fotografico: "))
            if precio <= 0:
                raise ValueError("El precio debe ser mayor que cero.")
            break
        except ValueError:
            print("El precio debe ser un número positivo.")
            continue
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
    while True:
        try:
            duracion = int(input("Ingrese la duración del servicio en horas: "))
            if duracion <= 0:
                raise ValueError("La duración debe ser mayor que cero.")
            break
        except ValueError:
            print("La duración debe ser un número entero positivo.")
            continue
    
    duracion = f"{str(duracion)} horas"

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
    

def modificar_servicio():
    id = input("Ingrese el ID del servicio a modificar: ")

    if id not in fotografia:
        print("ID no encontrado.")
        return
    
    nombre = input("ingrese el nombre del paquete fotografico: ").capitalize()
    while True:
        try:
            precio = float(input("ingrese el precio del paquete fotografico: "))
            if precio <= 0:
                raise ValueError("El precio debe ser mayor que cero.")
            break
        except ValueError:
            print("El precio debe ser un número positivo.")
            continue
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
    while True:
        try:
            duracion = int(input("Ingrese la duración del servicio en horas: "))
            if duracion <= 0:
                raise ValueError("La duración debe ser mayor que cero.")
            break
        except ValueError:
            print("La duración debe ser un número entero positivo.")
            continue

    fotografia[id].update({
        "nombre": nombre,
        "precio": precio,
        "evento": evento,
        "duracion": duracion
    })
    guardar_datos(fotografia, "fotografia.json")
    print("Servicio fotográfico modificado con éxito.")
        



