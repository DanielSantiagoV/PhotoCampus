from dataclasses import dataclass, asdict
from typing import Dict, Any

@dataclass
class ServicioFotografico:
    """
    Clase que representa un servicio fotográfico.
    """
    id: str
    nombre: str
    precio: float
    evento: str
    duracion: str
    
    @classmethod
    def desde_dict(cls, id: str, datos: Dict[str, Any]) -> 'ServicioFotografico':
        """
        Crea una instancia de ServicioFotografico desde un diccionario.
        """
        return cls(
            id=id,
            nombre=datos.get('nombre', ''),
            precio=datos.get('precio', 0.0),
            evento=datos.get('evento', ''),
            duracion=datos.get('duracion', '')
        )
    
    def a_dict(self) -> Dict[str, Any]:
        """
        Convierte la instancia a un diccionario.
        """
        return {
            'nombre': self.nombre,
            'precio': self.precio,
            'evento': self.evento,
            'duracion': self.duracion
        }
    
    def __str__(self) -> str:
        """
        Representación en cadena del servicio fotográfico.
        """
        return (
            f"ID: {self.id}\n"
            f"Nombre: {self.nombre}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Tipo de Evento: {self.evento}\n"
            f"Duración: {self.duracion}"
        ) 