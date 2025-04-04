"""
Módulo de configuración para PhotoCampus 📸
Contiene constantes, rutas y configuraciones globales para la aplicación
"""

import os
import sys
from pathlib import Path

# Definir la ruta base del proyecto
BASE_DIR = Path(__file__).parent.parent

# Rutas importantes
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_DIR = os.path.join(BASE_DIR, "src", "db")
ASSETS_DIR = os.path.join(BASE_DIR, "src", "assets")

# Nombres de archivos de datos
FOTOGRAFIA_FILE = os.path.join(DATA_DIR, "fotografia.json")

# Asegurar que los directorios necesarios existan
def ensure_directories():
    """Crea los directorios necesarios si no existen"""
    dirs = [DATA_DIR, DB_DIR, ASSETS_DIR]
    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)

# Colores para la terminal usando ANSI escape codes
class Colors:
    """Clase para manejar colores en la terminal"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Emojis frecuentemente usados
class Emojis:
    """Clase para manejar emojis en la interfaz"""
    CAMERA = "📸"
    CHECK = "✅"
    ERROR = "❌"
    MONEY = "💰"
    CLOCK = "⏱️"
    EDIT = "✏️"
    TRASH = "🗑️"
    STAR = "⭐"
    INFO = "ℹ️"
    WARNING = "⚠️"
    FOLDER = "📁"
    DOCUMENT = "📄"
    SAVE = "💾"
    CONFIG = "⚙️"
    PERSON = "👤"
    LIST = "📋"
    NEW = "🆕"
    EXIT = "🚪"

# Tipos de eventos disponibles
TIPOS_EVENTOS = {
    1: "Boda",
    2: "Retrato",
    3: "Producto",
    4: "Quinceañera",
    5: "Graduación",
    6: "Corporativo",
    7: "Evento deportivo"
}

# Versión de la aplicación
VERSION = "1.0.0" 