import json
import os
import shutil
from datetime import datetime
from utilidades.herramientas import mostrar_mensaje_error, mostrar_mensaje_exito, crear_carpeta_si_no_existe

# Crear carpeta para respaldos
CARPETA_RESPALDOS = "respaldos"
crear_carpeta_si_no_existe(CARPETA_RESPALDOS)

# Diccionario para almacenar los datos
fotografia = {}

# Actualizar la ruta del archivo JSON
ARCHIVO_JSON = "datos/fotografia.json"

def cargar_datos(archivo=ARCHIVO_JSON):
    """
    Carga datos desde un archivo JSON.
    """
    datos = {}
    try:
        if os.path.exists(archivo):
            with open(archivo, 'r', encoding='utf-8') as file:
                datos = json.load(file)
        else:
            mostrar_mensaje_info(f"📝 El archivo {archivo} no existe. Se creará al guardar datos.")
    except Exception as e:
        mostrar_mensaje_error(f"❌ Error al cargar los datos: {str(e)}")
        datos = {}

    if archivo == ARCHIVO_JSON:
        fotografia.update(datos)
    
    return datos

def guardar_datos(datos, archivo=ARCHIVO_JSON):
    """
    Guarda datos en un archivo JSON y crea una copia de respaldo.
    """
    try:
        # Guardar el archivo principal
        datos_a_guardar = json.dumps(datos, indent=4, ensure_ascii=False)
        with open(archivo, 'w', encoding='utf-8') as file:
            file.write(datos_a_guardar)
        
        # Crear una copia de respaldo con fecha y hora
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_base = os.path.splitext(os.path.basename(archivo))[0]
        archivo_respaldo = os.path.join(CARPETA_RESPALDOS, f"{nombre_base}_{timestamp}.json")
        
        with open(archivo_respaldo, 'w', encoding='utf-8') as file:
            file.write(datos_a_guardar)
            
        mostrar_mensaje_exito(f"✅ Datos guardados correctamente en {archivo}")
        return True
    
    except Exception as e:
        mostrar_mensaje_error(f"❌ Error al guardar los datos: {str(e)}")
        return False

def obtener_datos_fotografia():
    """
    Devuelve una copia del diccionario de fotografía.
    """
    return fotografia.copy()

def actualizar_fotografia(datos_nuevos):
    """
    Actualiza el diccionario de fotografía completo.
    """
    fotografia.clear()
    fotografia.update(datos_nuevos)
    return guardar_datos(fotografia, ARCHIVO_JSON) 