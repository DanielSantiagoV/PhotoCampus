"""
Módulo para la gestión de datos en formato JSON
Proporciona funcionalidades para cargar, guardar y manipular datos
"""

import json
import os
from datetime import datetime
from pathlib import Path
import sys

# Agregar la ruta del proyecto al sistema
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.config import FOTOGRAFIA_FILE, ensure_directories, Emojis

# Estructura global para almacenar los datos
fotografia = {}
backup_filename = "backup_{}.json"

def inicializar():
    """Inicializa la base de datos asegurando que existan los directorios necesarios"""
    ensure_directories()
    cargar_datos(FOTOGRAFIA_FILE)

def cargar_datos(archivo):
    """
    Carga los datos desde un archivo JSON
    
    Args:
        archivo (str): Ruta del archivo JSON a cargar
    
    Returns:
        bool: True si la carga fue exitosa, False en caso contrario
    """
    global fotografia
    datos = {}
    
    if not os.path.exists(archivo):
        # Si el archivo no existe, creamos uno con estructura vacía
        guardar_datos({}, archivo)
        print(f"{Emojis.INFO} Archivo {archivo} no encontrado. Se ha creado uno nuevo.")
        return True
    
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            datos = json.load(file)
        
        if archivo == FOTOGRAFIA_FILE:
            fotografia.clear()
            fotografia.update(datos)
        
        return True
    except json.JSONDecodeError:
        print(f"{Emojis.ERROR} Error al decodificar el archivo JSON: {archivo}")
        return False
    except Exception as e:
        print(f"{Emojis.ERROR} Error al cargar los datos desde {archivo}: {str(e)}")
        return False

def guardar_datos(datos, archivo):
    """
    Guarda datos en un archivo JSON
    
    Args:
        datos (dict): Diccionario con los datos a guardar
        archivo (str): Ruta del archivo JSON donde guardar
    
    Returns:
        bool: True si la operación fue exitosa, False en caso contrario
    """
    try:
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(os.path.abspath(archivo)), exist_ok=True)
        
        datos_a_guardar = json.dumps(datos, indent=4, ensure_ascii=False)
        with open(archivo, 'w', encoding='utf-8') as file:
            file.write(datos_a_guardar)
        return True
    except Exception as e:
        print(f"{Emojis.ERROR} Error al guardar los datos en {archivo}: {str(e)}")
        return False

def crear_backup():
    """
    Crea una copia de seguridad de los datos actuales
    
    Returns:
        str: Nombre del archivo de backup creado o None si falló
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(os.path.dirname(FOTOGRAFIA_FILE), 
                              backup_filename.format(timestamp))
    
    if guardar_datos(fotografia, backup_file):
        print(f"{Emojis.SAVE} Backup creado en: {backup_file}")
        return backup_file
    return None

def restaurar_backup(backup_file):
    """
    Restaura los datos desde un archivo de backup
    
    Args:
        backup_file (str): Ruta del archivo de backup a restaurar
        
    Returns:
        bool: True si la restauración fue exitosa, False en caso contrario
    """
    if cargar_datos(backup_file):
        # Guardar los datos restaurados en el archivo principal
        return guardar_datos(fotografia, FOTOGRAFIA_FILE)
    return False

def obtener_todos_servicios():
    """
    Obtiene todos los servicios fotográficos
    
    Returns:
        dict: Diccionario con todos los servicios
    """
    return fotografia

def obtener_servicio(id):
    """
    Obtiene un servicio específico por su ID
    
    Args:
        id (str): ID del servicio a buscar
        
    Returns:
        dict: Datos del servicio o None si no existe
    """
    return fotografia.get(id)

def agregar_servicio(id, datos):
    """
    Agrega un nuevo servicio fotográfico
    
    Args:
        id (str): ID del nuevo servicio
        datos (dict): Datos del servicio
        
    Returns:
        bool: True si se agregó correctamente, False si ya existía
    """
    if id in fotografia:
        return False
    
    fotografia[id] = datos
    guardar_datos(fotografia, FOTOGRAFIA_FILE)
    return True

def actualizar_servicio(id, datos):
    """
    Actualiza un servicio existente
    
    Args:
        id (str): ID del servicio a actualizar
        datos (dict): Nuevos datos del servicio
        
    Returns:
        bool: True si se actualizó correctamente, False si no existía
    """
    if id not in fotografia:
        return False
    
    fotografia[id].update(datos)
    guardar_datos(fotografia, FOTOGRAFIA_FILE)
    return True

def eliminar_servicio(id):
    """
    Elimina un servicio fotográfico
    
    Args:
        id (str): ID del servicio a eliminar
        
    Returns:
        bool: True si se eliminó correctamente, False si no existía
    """
    if id not in fotografia:
        return False
    
    del fotografia[id]
    guardar_datos(fotografia, FOTOGRAFIA_FILE)
    return True

def buscar_servicios(criterio, valor):
    """
    Busca servicios que coincidan con un criterio y valor
    
    Args:
        criterio (str): Campo por el cual buscar (nombre, evento, etc.)
        valor: Valor a buscar
        
    Returns:
        dict: Diccionario con los servicios que coinciden
    """
    resultados = {}
    
    for id, servicio in fotografia.items():
        if criterio in servicio:
            # Si es búsqueda de texto, hacemos comparación insensible a mayúsculas
            if isinstance(servicio[criterio], str) and isinstance(valor, str):
                if valor.lower() in servicio[criterio].lower():
                    resultados[id] = servicio
            # Si es búsqueda numérica o exacta
            elif servicio[criterio] == valor:
                resultados[id] = servicio
    
    return resultados

def generar_id():
    """
    Genera un nuevo ID para un servicio
    
    Returns:
        str: Nuevo ID para un servicio
    """
    if not fotografia:
        return "F-001"
    
    # Extraer los números de los IDs existentes
    ids_num = [int(id.split('-')[1]) for id in fotografia.keys()]
    
    # Generar el siguiente número
    next_num = max(ids_num) + 1
    
    return f"F-{next_num:03d}" 