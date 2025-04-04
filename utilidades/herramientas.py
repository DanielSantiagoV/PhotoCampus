from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import json
import os
from colorama import Fore, Style

# Crear consola para salida enriquecida
console = Console()

def mostrar_mensaje_exito(mensaje):
    """Muestra un mensaje de éxito formateado."""
    texto = Text(mensaje, style="bold green")
    console.print(Panel(texto, border_style="green"))

def mostrar_mensaje_error(mensaje):
    """Muestra un mensaje de error formateado."""
    texto = Text(mensaje, style="bold red")
    console.print(Panel(texto, border_style="red"))

def mostrar_mensaje_info(mensaje):
    """Muestra un mensaje informativo formateado."""
    texto = Text(mensaje, style="bold blue")
    console.print(Panel(texto, border_style="blue"))

def validar_entrada_numerica(mensaje, tipo=float, valor_minimo=0):
    """Valida una entrada numérica con un valor mínimo."""
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor <= valor_minimo:
                mostrar_mensaje_error(f"El valor debe ser mayor que {valor_minimo}.")
                continue
            return valor
        except ValueError:
            mostrar_mensaje_error(f"Por favor, ingrese un valor numérico válido.")

def crear_carpeta_si_no_existe(ruta):
    """Crea una carpeta si no existe."""
    if not os.path.exists(ruta):
        os.makedirs(ruta) 