from interfaz_usuario.menu import mostrar_menu_principal, pedir_opcion
from interfaz_usuario.gestor_interfaz import (
    registrar_servicio,
    listar_servicios,
    modificar_servicio,
    eliminar_servicio,
    buscar_servicios,
    mostrar_estadisticas,
    exportar_catalogo,
    mostrar_ayuda
)
from almacenamiento.gestor_datos import cargar_datos
from utilidades.herramientas import mostrar_mensaje_error, mostrar_mensaje_info
import os

# Crear carpetas necesarias
if not os.path.exists("exportaciones"):
    os.makedirs("exportaciones")

# Cargar datos al iniciar
cargar_datos("fotografia.json")

def main():
    """
    Función principal que ejecuta el programa.
    """
    while True:
        mostrar_menu_principal()
        try:
            opcion = pedir_opcion()
        except ValueError:
            mostrar_mensaje_error("❌ Error: Debe ingresar una opción válida.")
            continue
            
        if opcion == 1:
            registrar_servicio()
        elif opcion == 2:
            listar_servicios()
        elif opcion == 3:
            modificar_servicio()
        elif opcion == 4:
            eliminar_servicio()
        elif opcion == 5:
            buscar_servicios()
        elif opcion == 6:
            mostrar_estadisticas()
        elif opcion == 7:
            exportar_catalogo()
        elif opcion == 8:
            mostrar_ayuda()
        elif opcion == 9:
            mostrar_mensaje_info("🚪 Saliendo del sistema. ¡Gracias por usar PhotoCampus!")
            break
        else:
            mostrar_mensaje_error("❌ Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        mostrar_mensaje_info("\n🚪 Programa interrumpido. ¡Gracias por usar PhotoCampus!")
    except Exception as e:
        mostrar_mensaje_error(f"❌ Error inesperado: {str(e)}")
