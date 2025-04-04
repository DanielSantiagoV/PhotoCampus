"""
Controlador para la gestión de servicios fotográficos
Implementa la lógica de negocio relacionada con los servicios
"""

from pathlib import Path
import sys

# Agregar la ruta del proyecto al sistema
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.db.database import (obtener_todos_servicios, obtener_servicio, 
                           agregar_servicio, actualizar_servicio, 
                           eliminar_servicio, generar_id, buscar_servicios)
from src.config import TIPOS_EVENTOS, Emojis

class ServicioController:
    """Controlador para la gestión de servicios fotográficos"""
    
    @staticmethod
    def registrar_servicio(nombre, precio, tipo_evento, duracion, descripcion=None):
        """
        Registra un nuevo servicio fotográfico
        
        Args:
            nombre (str): Nombre del paquete fotográfico
            precio (float): Precio del servicio
            tipo_evento (int): Tipo de evento (1-7)
            duracion (int): Duración en horas
            descripcion (str, optional): Descripción del servicio
            
        Returns:
            tuple: (bool, str) - (Éxito, Mensaje)
        """
        # Validaciones
        if not nombre or not nombre.strip():
            return False, f"{Emojis.ERROR} El nombre no puede estar vacío"
            
        if precio <= 0:
            return False, f"{Emojis.ERROR} El precio debe ser mayor que cero"
            
        if tipo_evento not in TIPOS_EVENTOS:
            return False, f"{Emojis.ERROR} Tipo de evento no válido"
            
        if duracion <= 0:
            return False, f"{Emojis.ERROR} La duración debe ser mayor que cero"
        
        # Generar ID
        id = generar_id()
        
        # Crear datos del servicio
        datos_servicio = {
            "nombre": nombre.strip().capitalize(),
            "precio": precio,
            "evento": TIPOS_EVENTOS[tipo_evento],
            "duracion": f"{duracion} horas",
            "fecha_registro": ServicioController.obtener_fecha_actual()
        }
        
        # Agregar descripción si existe
        if descripcion:
            datos_servicio["descripcion"] = descripcion.strip()
        
        # Agregar servicio
        if agregar_servicio(id, datos_servicio):
            return True, f"{Emojis.CHECK} Servicio fotográfico registrado con éxito. ID: {id}"
        else:
            return False, f"{Emojis.ERROR} Error al registrar el servicio fotográfico"
    
    @staticmethod
    def modificar_servicio(id, nombre=None, precio=None, tipo_evento=None, duracion=None, descripcion=None):
        """
        Modifica un servicio fotográfico existente
        
        Args:
            id (str): ID del servicio a modificar
            nombre (str, optional): Nuevo nombre
            precio (float, optional): Nuevo precio
            tipo_evento (int, optional): Nuevo tipo de evento
            duracion (int, optional): Nueva duración
            descripcion (str, optional): Nueva descripción
            
        Returns:
            tuple: (bool, str) - (Éxito, Mensaje)
        """
        # Verificar que el servicio exista
        servicio = obtener_servicio(id)
        if not servicio:
            return False, f"{Emojis.ERROR} No existe un servicio con el ID: {id}"
        
        # Preparar datos a actualizar
        datos_actualizar = {}
        
        if nombre is not None and nombre.strip():
            datos_actualizar["nombre"] = nombre.strip().capitalize()
            
        if precio is not None and precio > 0:
            datos_actualizar["precio"] = precio
        elif precio is not None:
            return False, f"{Emojis.ERROR} El precio debe ser mayor que cero"
            
        if tipo_evento is not None:
            if tipo_evento in TIPOS_EVENTOS:
                datos_actualizar["evento"] = TIPOS_EVENTOS[tipo_evento]
            else:
                return False, f"{Emojis.ERROR} Tipo de evento no válido"
                
        if duracion is not None:
            if duracion > 0:
                datos_actualizar["duracion"] = f"{duracion} horas"
            else:
                return False, f"{Emojis.ERROR} La duración debe ser mayor que cero"
                
        if descripcion is not None:
            datos_actualizar["descripcion"] = descripcion.strip()
        
        # Si no hay datos que actualizar
        if not datos_actualizar:
            return False, f"{Emojis.INFO} No se han proporcionado datos para actualizar"
        
        # Agregar fecha de modificación
        datos_actualizar["fecha_modificacion"] = ServicioController.obtener_fecha_actual()
        
        # Actualizar servicio
        if actualizar_servicio(id, datos_actualizar):
            return True, f"{Emojis.CHECK} Servicio fotográfico modificado con éxito"
        else:
            return False, f"{Emojis.ERROR} Error al modificar el servicio fotográfico"
    
    @staticmethod
    def eliminar_servicio(id):
        """
        Elimina un servicio fotográfico
        
        Args:
            id (str): ID del servicio a eliminar
            
        Returns:
            tuple: (bool, str) - (Éxito, Mensaje)
        """
        # Verificar que el servicio exista
        if not obtener_servicio(id):
            return False, f"{Emojis.ERROR} No existe un servicio con el ID: {id}"
        
        # Eliminar servicio
        if eliminar_servicio(id):
            return True, f"{Emojis.CHECK} Servicio fotográfico eliminado con éxito"
        else:
            return False, f"{Emojis.ERROR} Error al eliminar el servicio fotográfico"
    
    @staticmethod
    def listar_servicios():
        """
        Obtiene todos los servicios fotográficos
        
        Returns:
            dict: Diccionario con todos los servicios
        """
        return obtener_todos_servicios()
    
    @staticmethod
    def obtener_servicio(id):
        """
        Obtiene un servicio fotográfico por su ID
        
        Args:
            id (str): ID del servicio
            
        Returns:
            dict: Datos del servicio o None si no existe
        """
        return obtener_servicio(id)
    
    @staticmethod
    def buscar_servicios(criterio, valor):
        """
        Busca servicios que coincidan con un criterio y valor
        
        Args:
            criterio (str): Campo por el cual buscar (nombre, evento, etc.)
            valor: Valor a buscar
            
        Returns:
            dict: Diccionario con los servicios que coinciden
        """
        return buscar_servicios(criterio, valor)
    
    @staticmethod
    def obtener_fecha_actual():
        """
        Obtiene la fecha y hora actual en formato legible
        
        Returns:
            str: Fecha y hora actual
        """
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    @staticmethod
    def validar_tipo_evento(tipo):
        """
        Valida si un tipo de evento es válido
        
        Args:
            tipo (int): Tipo de evento a validar
            
        Returns:
            bool: True si es válido, False si no
        """
        return tipo in TIPOS_EVENTOS
    
    @staticmethod
    def obtener_tipos_eventos():
        """
        Obtiene los tipos de eventos disponibles
        
        Returns:
            dict: Diccionario con los tipos de eventos
        """
        return TIPOS_EVENTOS 