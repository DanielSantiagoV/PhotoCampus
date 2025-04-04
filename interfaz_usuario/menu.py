from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from utilidades.herramientas import mostrar_mensaje_error, validar_entrada_numerica

console = Console()

def mostrar_logo():
    """
    Muestra el logo de PhotoCampus centrado en la terminal.
    """
    logo = Text("""
    ╔═══════════════════════════════════════════════════╗
    ║  📸 P H O T O C A M P U S - Servicios Fotográficos ║
    ╚═══════════════════════════════════════════════════╝
    """, style="bold blue", justify="center")
    console.print(Panel(logo, expand=False, border_style="blue"))

def mostrar_menu_principal():
    """
    Muestra el menú principal con opciones organizadas.
    """
    mostrar_logo()
    
    tabla = Table(show_header=False, expand=True, border_style="blue")
    tabla.add_column("Opción", style="cyan bold", justify="center")
    tabla.add_column("Descripción", style="white bold")
    
    opciones = [
        ("1", "📝 Registrar nuevo servicio fotográfico"),
        ("2", "📋 Listar todos los servicios fotográficos"),
        ("3", "✏️ Modificar servicio fotográfico"),
        ("4", "🗑️ Eliminar servicio fotográfico"),
        ("5", "🔍 Buscar servicios fotográficos"),
        ("6", "📊 Ver estadísticas"),
        ("7", "💾 Exportar catálogo"),
        ("8", "❓ Ayuda"),
        ("9", "🚪 Salir")
    ]
    
    for opcion, descripcion in opciones:
        tabla.add_row(opcion, descripcion)
    
    console.print(Panel(tabla, title="Menú Principal", border_style="blue", padding=(0, 2)))

def pedir_opcion(max_opcion=9):
    """
    Solicita al usuario seleccionar una opción del menú.
    """
    try:
        opcion = validar_entrada_numerica("Seleccione una opción: ", tipo=int, valor_minimo=0)
        if opcion > max_opcion:
            mostrar_mensaje_error(f"Opción no válida. Ingrese un número entre 1 y {max_opcion}.")
            return pedir_opcion(max_opcion)
        return opcion
    except Exception:
        mostrar_mensaje_error("Por favor, ingrese un número válido.")
        return pedir_opcion(max_opcion)

def mostrar_submenu_busqueda():
    """
    Muestra el submenú de búsqueda.
    """
    tabla = Table(show_header=False, expand=True, border_style="blue")
    tabla.add_column("Opción", style="cyan", justify="right")
    tabla.add_column("Descripción", style="white")
    
    tabla.add_row("1", "🔍 Buscar por nombre")
    tabla.add_row("2", "🔍 Buscar por tipo de evento")
    tabla.add_row("3", "🔍 Buscar por duración")
    tabla.add_row("4", "↩️ Volver al menú principal")
    
    console.print(Panel(tabla, title="Submenú de Búsqueda", border_style="blue")) 