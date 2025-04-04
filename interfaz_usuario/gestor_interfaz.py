from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from modelo_datos.servicio_fotografico import ServicioFotografico
from servicios.gestor_servicios import GestorServicios
from utilidades.herramientas import (
    mostrar_mensaje_exito, 
    mostrar_mensaje_error, 
    mostrar_mensaje_info,
    validar_entrada_numerica
)
import os
import json

console = Console()

def registrar_servicio():
    """
    Interfaz para registrar un nuevo servicio fotográfico.
    """
    console.print(Panel(Text("📝 REGISTRO DE NUEVO SERVICIO FOTOGRÁFICO", style="bold cyan"), border_style="cyan"))
    
    # Generar ID automáticamente
    id_servicio = GestorServicios.generar_id()
    console.print(f"[bold]ID asignado:[/bold] [cyan]{id_servicio}[/cyan]")
    
    # Solicitar datos del servicio
    nombre = input("Ingrese el nombre del paquete fotográfico: ").strip().capitalize()
    precio = validar_entrada_numerica("Ingrese el precio del paquete fotográfico: $", tipo=float, valor_minimo=0)
    
    # Menú para seleccionar tipo de evento
    console.print("\n[bold]Tipo de evento:[/bold]")
    tabla_eventos = Table(show_header=False, border_style="cyan")
    tabla_eventos.add_column("Opción", style="cyan", justify="right")
    tabla_eventos.add_column("Tipo", style="white")
    
    tabla_eventos.add_row("1", "💍 Boda")
    tabla_eventos.add_row("2", "👤 Retrato")
    tabla_eventos.add_row("3", "📦 Producto")
    tabla_eventos.add_row("4", "🎓 Graduación")
    tabla_eventos.add_row("5", "🏢 Corporativo")
    tabla_eventos.add_row("6", "🎉 Evento especial")
    
    console.print(tabla_eventos)
    
    # Solicitar tipo de evento
    tipos_eventos = ["Boda", "Retrato", "Producto", "Graduación", "Corporativo", "Evento especial"]
    iconos_eventos = ["💍", "👤", "📦", "🎓", "🏢", "🎉"]
    
    while True:
        opcion_evento = validar_entrada_numerica("Elija el tipo de evento: ", tipo=int, valor_minimo=0)
        if 1 <= opcion_evento <= len(tipos_eventos):
            evento = f"{iconos_eventos[opcion_evento-1]} {tipos_eventos[opcion_evento-1]}"
            break
        else:
            mostrar_mensaje_error(f"Opción no válida. Ingrese un número entre 1 y {len(tipos_eventos)}.")
    
    # Solicitar duración
    duracion_horas = validar_entrada_numerica("Ingrese la duración del servicio en horas: ", tipo=int, valor_minimo=0)
    duracion = f"{duracion_horas} horas"
    
    # Crear el servicio
    servicio = ServicioFotografico(
        id=id_servicio,
        nombre=nombre,
        precio=precio,
        evento=evento,
        duracion=duracion
    )
    
    # Mostrar resumen
    console.print("\n[bold cyan]Resumen del servicio a registrar:[/bold cyan]")
    console.print(Panel(Text(str(servicio), style="white"), border_style="cyan"))
    
    # Confirmar registro
    confirmacion = input("¿Desea confirmar el registro? (s/n): ").lower()
    if confirmacion == 's':
        if GestorServicios.agregar_servicio(servicio):
            mostrar_mensaje_exito("✅ Servicio fotográfico registrado con éxito.")
        else:
            mostrar_mensaje_error("❌ Error al registrar el servicio fotográfico.")
    else:
        mostrar_mensaje_info("ℹ️ Registro cancelado.")

def listar_servicios():
    """
    Interfaz para listar todos los servicios fotográficos.
    """
    servicios = GestorServicios.obtener_todos_servicios()
    
    if not servicios:
        mostrar_mensaje_info("📭 No hay servicios fotográficos registrados.")
        return
    
    console.print(Panel(Text("📋 LISTADO DE SERVICIOS FOTOGRÁFICOS", style="bold cyan"), border_style="cyan"))
    
    tabla = Table(show_header=True, border_style="cyan")
    tabla.add_column("ID", style="cyan")
    tabla.add_column("Nombre", style="white")
    tabla.add_column("Precio", style="green", justify="right")
    tabla.add_column("Evento", style="yellow")
    tabla.add_column("Duración", style="blue")
    
    for servicio in servicios.values():
        tabla.add_row(
            servicio.id,
            servicio.nombre,
            f"${servicio.precio:.2f}",
            servicio.evento,
            servicio.duracion
        )
    
    console.print(tabla)
    input("\nPresione Enter para continuar...")

def modificar_servicio():
    """
    Interfaz para modificar un servicio fotográfico existente.
    """
    console.print(Panel(Text("✏️ MODIFICACIÓN DE SERVICIO FOTOGRÁFICO", style="bold yellow"), border_style="yellow"))
    
    id_servicio = input("Ingrese el ID del servicio a modificar: ").strip().upper()
    servicio = GestorServicios.obtener_servicio_por_id(id_servicio)
    
    if not servicio:
        mostrar_mensaje_error(f"❌ No se encontró un servicio con ID: {id_servicio}")
        return
    
    console.print("\n[bold yellow]Datos actuales del servicio:[/bold yellow]")
    console.print(Panel(Text(str(servicio), style="white"), border_style="yellow"))
    
    console.print("\n[bold yellow]Ingrese los nuevos datos (deje en blanco para mantener el valor actual):[/bold yellow]")
    
    # Nombre
    nombre_nuevo = input(f"Nombre [{servicio.nombre}]: ").strip()
    nombre = nombre_nuevo if nombre_nuevo else servicio.nombre
    
    # Precio
    precio_str = input(f"Precio [${servicio.precio:.2f}]: ").strip()
    try:
        precio = float(precio_str) if precio_str else servicio.precio
        if precio <= 0:
            mostrar_mensaje_error("El precio debe ser mayor que cero.")
            precio = servicio.precio
    except ValueError:
        mostrar_mensaje_error("Valor no válido para el precio.")
        precio = servicio.precio
    
    # Tipo de evento
    console.print("\n[bold]Tipo de evento actual:[/bold] " + servicio.evento)
    console.print("[bold]¿Desea cambiar el tipo de evento? (s/n):[/bold]")
    cambiar_evento = input().lower() == 's'
    
    evento = servicio.evento
    if cambiar_evento:
        # Menú para seleccionar tipo de evento
        tabla_eventos = Table(show_header=False, border_style="yellow")
        tabla_eventos.add_column("Opción", style="yellow", justify="right")
        tabla_eventos.add_column("Tipo", style="white")
        
        tabla_eventos.add_row("1", "💍 Boda")
        tabla_eventos.add_row("2", "👤 Retrato")
        tabla_eventos.add_row("3", "📦 Producto")
        tabla_eventos.add_row("4", "🎓 Graduación")
        tabla_eventos.add_row("5", "🏢 Corporativo")
        tabla_eventos.add_row("6", "🎉 Evento especial")
        
        console.print(tabla_eventos)
        
        tipos_eventos = ["Boda", "Retrato", "Producto", "Graduación", "Corporativo", "Evento especial"]
        iconos_eventos = ["💍", "👤", "📦", "🎓", "🏢", "🎉"]
        
        while True:
            opcion_evento = validar_entrada_numerica("Elija el tipo de evento: ", tipo=int, valor_minimo=0)
            if 1 <= opcion_evento <= len(tipos_eventos):
                evento = f"{iconos_eventos[opcion_evento-1]} {tipos_eventos[opcion_evento-1]}"
                break
            else:
                mostrar_mensaje_error(f"Opción no válida. Ingrese un número entre 1 y {len(tipos_eventos)}.")
    
    # Duración
    duracion_actual = servicio.duracion
    duracion_str = input(f"Duración [{duracion_actual}]: ").strip()
    if duracion_str:
        try:
            duracion_horas = int(duracion_str.split()[0])
            if duracion_horas <= 0:
                mostrar_mensaje_error("La duración debe ser mayor que cero.")
                duracion = duracion_actual
            else:
                duracion = f"{duracion_horas} horas"
        except (ValueError, IndexError):
            mostrar_mensaje_error("Valor no válido para la duración.")
            duracion = duracion_actual
    else:
        duracion = duracion_actual
    
    # Crear el servicio actualizado
    servicio_actualizado = ServicioFotografico(
        id=id_servicio,
        nombre=nombre,
        precio=precio,
        evento=evento,
        duracion=duracion
    )
    
    # Mostrar resumen
    console.print("\n[bold yellow]Resumen del servicio modificado:[/bold yellow]")
    console.print(Panel(Text(str(servicio_actualizado), style="white"), border_style="yellow"))
    
    # Confirmar modificación
    confirmacion = input("¿Desea confirmar la modificación? (s/n): ").lower()
    if confirmacion == 's':
        if GestorServicios.modificar_servicio(servicio_actualizado):
            mostrar_mensaje_exito("✅ Servicio fotográfico modificado con éxito.")
        else:
            mostrar_mensaje_error("❌ Error al modificar el servicio fotográfico.")
    else:
        mostrar_mensaje_info("ℹ️ Modificación cancelada.")

def eliminar_servicio():
    """
    Interfaz para eliminar un servicio fotográfico.
    """
    console.print(Panel(Text("🗑️ ELIMINACIÓN DE SERVICIO FOTOGRÁFICO", style="bold red"), border_style="red"))
    
    id_servicio = input("Ingrese el ID del servicio a eliminar: ").strip().upper()
    servicio = GestorServicios.obtener_servicio_por_id(id_servicio)
    
    if not servicio:
        mostrar_mensaje_error(f"❌ No se encontró un servicio con ID: {id_servicio}")
        return
    
    console.print("\n[bold red]Datos del servicio a eliminar:[/bold red]")
    console.print(Panel(Text(str(servicio), style="white"), border_style="red"))
    
    # Confirmar eliminación
    confirmacion = input("¿Está seguro de que desea eliminar este servicio? (s/n): ").lower()
    if confirmacion == 's':
        if GestorServicios.eliminar_servicio(id_servicio):
            mostrar_mensaje_exito("✅ Servicio fotográfico eliminado con éxito.")
        else:
            mostrar_mensaje_error("❌ Error al eliminar el servicio fotográfico.")
    else:
        mostrar_mensaje_info("ℹ️ Eliminación cancelada.")

def buscar_servicios():
    """
    Interfaz para buscar servicios fotográficos.
    """
    from interfaz_usuario.menu import mostrar_submenu_busqueda, pedir_opcion
    
    console.print(Panel(Text("🔍 BÚSQUEDA DE SERVICIOS FOTOGRÁFICOS", style="bold blue"), border_style="blue"))
    
    while True:
        mostrar_submenu_busqueda()
        opcion = pedir_opcion(4)
        
        if opcion == 4:  # Volver al menú principal
            break
        
        criterios = {
            1: "nombre",
            2: "evento",
            3: "duracion"
        }
        
        criterio = criterios[opcion]
        valor = input(f"Ingrese el valor a buscar en {criterio}: ").strip()
        
        resultados = GestorServicios.buscar_servicios(criterio, valor)
        
        if not resultados:
            mostrar_mensaje_info(f"📭 No se encontraron servicios con {criterio} que contenga '{valor}'.")
        else:
            console.print(f"\n[bold blue]Resultados de la búsqueda ({len(resultados)} encontrados):[/bold blue]")
            
            tabla = Table(show_header=True, border_style="blue")
            tabla.add_column("ID", style="cyan")
            tabla.add_column("Nombre", style="white")
            tabla.add_column("Precio", style="green", justify="right")
            tabla.add_column("Evento", style="yellow")
            tabla.add_column("Duración", style="blue")
            
            for servicio in resultados:
                tabla.add_row(
                    servicio.id,
                    servicio.nombre,
                    f"${servicio.precio:.2f}",
                    servicio.evento,
                    servicio.duracion
                )
            
            console.print(tabla)
        
        input("\nPresione Enter para continuar...")

def mostrar_estadisticas():
    """
    Muestra estadísticas de los servicios fotográficos.
    """
    servicios = GestorServicios.obtener_todos_servicios()
    
    if not servicios:
        mostrar_mensaje_info("📭 No hay servicios fotográficos registrados para generar estadísticas.")
        return
    
    console.print(Panel(Text("📊 ESTADÍSTICAS DE SERVICIOS FOTOGRÁFICOS", style="bold magenta"), border_style="magenta"))
    
    # Calcular estadísticas
    total_servicios = len(servicios)
    
    # Precio promedio, mínimo y máximo
    precios = [s.precio for s in servicios.values()]
    precio_promedio = sum(precios) / len(precios)
    precio_minimo = min(precios)
    precio_maximo = max(precios)
    
    # Contar por tipo de evento
    eventos = {}
    for servicio in servicios.values():
        evento_nombre = servicio.evento.split()[-1] if " " in servicio.evento else servicio.evento
        if evento_nombre in eventos:
            eventos[evento_nombre] += 1
        else:
            eventos[evento_nombre] = 1
    
    # Contar por duración
    duraciones = {}
    for servicio in servicios.values():
        if servicio.duracion in duraciones:
            duraciones[servicio.duracion] += 1
        else:
            duraciones[servicio.duracion] = 1
    
    # Mostrar estadísticas generales
    console.print("[bold magenta]Estadísticas Generales:[/bold magenta]")
    console.print(f"Total de servicios: {total_servicios}")
    console.print(f"Precio promedio: ${precio_promedio:.2f}")
    console.print(f"Precio mínimo: ${precio_minimo:.2f}")
    console.print(f"Precio máximo: ${precio_maximo:.2f}")
    
    # Mostrar estadísticas por tipo de evento
    console.print("\n[bold magenta]Distribución por Tipo de Evento:[/bold magenta]")
    tabla_eventos = Table(show_header=True, border_style="magenta")
    tabla_eventos.add_column("Tipo de Evento", style="white")
    tabla_eventos.add_column("Cantidad", style="cyan", justify="right")
    tabla_eventos.add_column("Porcentaje", style="green", justify="right")
    
    for evento, cantidad in eventos.items():
        porcentaje = (cantidad / total_servicios) * 100
        tabla_eventos.add_row(evento, str(cantidad), f"{porcentaje:.1f}%")
    
    console.print(tabla_eventos)
    
    # Mostrar estadísticas por duración
    console.print("\n[bold magenta]Distribución por Duración:[/bold magenta]")
    tabla_duraciones = Table(show_header=True, border_style="magenta")
    tabla_duraciones.add_column("Duración", style="white")
    tabla_duraciones.add_column("Cantidad", style="cyan", justify="right")
    tabla_duraciones.add_column("Porcentaje", style="green", justify="right")
    
    for duracion, cantidad in duraciones.items():
        porcentaje = (cantidad / total_servicios) * 100
        tabla_duraciones.add_row(duracion, str(cantidad), f"{porcentaje:.1f}%")
    
    console.print(tabla_duraciones)
    
    input("\nPresione Enter para continuar...")

def exportar_catalogo():
    """
    Exporta el catálogo de servicios a diferentes formatos.
    """
    servicios = GestorServicios.obtener_todos_servicios()
    
    if not servicios:
        mostrar_mensaje_info("📭 No hay servicios fotográficos registrados para exportar.")
        return
    
    console.print(Panel(Text("💾 EXPORTAR CATÁLOGO DE SERVICIOS", style="bold green"), border_style="green"))
    
    # Crear carpeta de exportación si no existe
    carpeta_exportacion = "exportaciones"
    if not os.path.exists(carpeta_exportacion):
        os.makedirs(carpeta_exportacion)
    
    # Opciones de exportación
    console.print("[bold green]Seleccione el formato de exportación:[/bold green]")
    tabla_formatos = Table(show_header=False, border_style="green")
    tabla_formatos.add_column("Opción", style="green", justify="right")
    tabla_formatos.add_column("Formato", style="white")
    
    tabla_formatos.add_row("1", "📄 Texto plano (.txt)")
    tabla_formatos.add_row("2", "📊 CSV (.csv)")
    tabla_formatos.add_row("3", "🔙 Volver al menú principal")
    
    console.print(tabla_formatos)
    
    opcion = validar_entrada_numerica("Seleccione una opción: ", tipo=int, valor_minimo=0)
    
    if opcion == 3:  # Volver al menú principal
        return
    
    timestamp = ""  # Lo definimos para el nombre del archivo
    
    if opcion == 1:  # Texto plano
        archivo_salida = os.path.join(carpeta_exportacion, f"catalogo_servicios{timestamp}.txt")
        
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            f.write("CATÁLOGO DE SERVICIOS FOTOGRÁFICOS - PHOTOCAMPUS\n")
            f.write("=" * 50 + "\n\n")
            
            for servicio in servicios.values():
                f.write(f"ID: {servicio.id}\n")
                f.write(f"Nombre: {servicio.nombre}\n")
                f.write(f"Precio: ${servicio.precio:.2f}\n")
                f.write(f"Tipo de Evento: {servicio.evento}\n")
                f.write(f"Duración: {servicio.duracion}\n")
                f.write("-" * 30 + "\n\n")
        
        mostrar_mensaje_exito(f"✅ Catálogo exportado a {archivo_salida}")
        
    elif opcion == 2:  # CSV
        archivo_salida = os.path.join(carpeta_exportacion, f"catalogo_servicios{timestamp}.csv")
        
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            # Encabezados
            f.write("ID,Nombre,Precio,Tipo de Evento,Duración\n")
            
            # Datos
            for servicio in servicios.values():
                evento_limpio = servicio.evento.replace(",", " -")
                f.write(f"{servicio.id},{servicio.nombre},{servicio.precio:.2f},\"{evento_limpio}\",{servicio.duracion}\n")
        
        mostrar_mensaje_exito(f"✅ Catálogo exportado a {archivo_salida}")
    
    else:
        mostrar_mensaje_error("❌ Opción no válida.")

def mostrar_ayuda():
    """
    Muestra información de ayuda sobre el sistema.
    """
    console.print(Panel(Text("❓ AYUDA DEL SISTEMA", style="bold cyan"), border_style="cyan"))
    
    ayuda = """
    📸 [bold]PhotoCampus - Sistema de Gestión de Servicios Fotográficos[/bold]
    
    Este sistema le permite gestionar los servicios fotográficos ofrecidos por PhotoCampus:
    
    [bold cyan]Funciones principales:[/bold cyan]
    
    1. [bold]Registrar servicios:[/bold] Añadir nuevos paquetes fotográficos al catálogo.
    
    2. [bold]Listar servicios:[/bold] Ver todos los servicios disponibles.
    
    3. [bold]Modificar servicios:[/bold] Actualizar información de servicios existentes.
    
    4. [bold]Eliminar servicios:[/bold] Quitar servicios que ya no se ofrecen.
    
    5. [bold]Buscar servicios:[/bold] Encontrar servicios por nombre, tipo de evento o duración.
    
    6. [bold]Estadísticas:[/bold] Ver información resumida sobre los servicios.
    
    7. [bold]Exportar catálogo:[/bold] Guardar la lista de servicios en diferentes formatos.
    
    [bold cyan]Consejos:[/bold cyan]
    
    • Los IDs de los servicios se generan automáticamente.
    • Los datos se guardan automáticamente en cada operación.
    • Se crean respaldos automáticos de los datos.
    
    [bold cyan]Sobre los datos:[/bold cyan]
    
    Los datos se almacenan en un archivo JSON y se realizan copias de respaldo
    en la carpeta "respaldos" cada vez que se modifican los datos.
    """
    
    console.print(Panel(Text.from_markup(ayuda), border_style="cyan", expand=False))
    
    input("\nPresione Enter para continuar...") 