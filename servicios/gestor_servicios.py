from typing import Dict, List, Optional
from modelo_datos.servicio_fotografico import ServicioFotografico
from almacenamiento.gestor_datos import obtener_datos_fotografia, guardar_datos, actualizar_fotografia
from utilidades.herramientas import mostrar_mensaje_exito, mostrar_mensaje_error, mostrar_mensaje_info

class GestorServicios:
    """
    Clase que gestiona los servicios fotográficos.
    """
    
    @staticmethod
    def generar_id() -> str:
        """
        Genera un ID único para un nuevo servicio.
        """
        datos = obtener_datos_fotografia()
        return f"F-{len(datos) + 1:03d}"
    
    @staticmethod
    def obtener_todos_servicios() -> Dict[str, ServicioFotografico]:
        """
        Obtiene todos los servicios fotográficos.
        """
        datos = obtener_datos_fotografia()
        servicios = {}
        
        for id_servicio, datos_servicio in datos.items():
            servicios[id_servicio] = ServicioFotografico.desde_dict(id_servicio, datos_servicio)
            
        return servicios
    
    @staticmethod
    def obtener_servicio_por_id(id_servicio: str) -> Optional[ServicioFotografico]:
        """
        Obtiene un servicio por su ID.
        """
        datos = obtener_datos_fotografia()
        if id_servicio in datos:
            return ServicioFotografico.desde_dict(id_servicio, datos[id_servicio])
        return None
    
    @staticmethod
    def agregar_servicio(servicio: ServicioFotografico) -> bool:
        """
        Agrega un nuevo servicio.
        """
        datos = obtener_datos_fotografia()
        datos[servicio.id] = servicio.a_dict()
        return guardar_datos(datos, "fotografia.json")
    
    @staticmethod
    def modificar_servicio(servicio: ServicioFotografico) -> bool:
        """
        Modifica un servicio existente.
        """
        datos = obtener_datos_fotografia()
        if servicio.id not in datos:
            mostrar_mensaje_error(f"❌ El servicio con ID {servicio.id} no existe.")
            return False
        
        datos[servicio.id] = servicio.a_dict()
        return guardar_datos(datos, "fotografia.json")
    
    @staticmethod
    def eliminar_servicio(id_servicio: str) -> bool:
        """
        Elimina un servicio por su ID.
        """
        datos = obtener_datos_fotografia()
        if id_servicio not in datos:
            mostrar_mensaje_error(f"❌ El servicio con ID {id_servicio} no existe.")
            return False
        
        del datos[id_servicio]
        return guardar_datos(datos, "fotografia.json")
    
    @staticmethod
    def buscar_servicios(criterio: str, valor: str) -> List[ServicioFotografico]:
        """
        Busca servicios según un criterio y valor.
        """
        servicios = GestorServicios.obtener_todos_servicios()
        resultados = []
        
        for servicio in servicios.values():
            if criterio == "nombre" and valor.lower() in servicio.nombre.lower():
                resultados.append(servicio)
            elif criterio == "evento" and valor.lower() in servicio.evento.lower():
                resultados.append(servicio)
            elif criterio == "duracion" and valor.lower() in servicio.duracion.lower():
                resultados.append(servicio)
        
        return resultados 