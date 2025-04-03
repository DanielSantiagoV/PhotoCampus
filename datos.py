import json

fotografia = {}

def cargar_datos(archivo):
    datos = {}
    try:
        with open(archivo, 'r') as file:
            datos = json.load(file)
    except Exception:
        print("Error al cargar los datos.")
        datos = None

    if archivo == "fotografia.json":
        fotografia.update(datos)

def guardar_datos(datos, archivo ):
    try:
        datos_a_guardar = json.dumps(datos, indent=4)
        with open(archivo, 'w') as file:
            file.write(datos_a_guardar)
    
    except Exception:
        print("Error al guardar los datos.")

        
