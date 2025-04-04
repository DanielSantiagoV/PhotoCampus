# 📸 PhotoCampus - Sistema de Gestión de Servicios Fotográficos

Sistema para gestionar los servicios fotográficos ofrecidos por PhotoCampus, permitiendo registrar, modificar y consultar los diferentes paquetes fotográficos disponibles.

## 🚀 Características

- ✅ Registro de servicios fotográficos con nombre, precio, tipo de evento y duración
- 📋 Listado de todos los servicios disponibles en formato de tabla
- ✏️ Modificación de servicios existentes
- 🗑️ Eliminación de servicios que ya no se ofrecen
- 🔍 Búsqueda de servicios por diferentes criterios
- 📊 Estadísticas sobre los servicios registrados
- 💾 Exportación del catálogo en diferentes formatos
- 🔄 Respaldo automático de datos
- 🎨 Interfaz interactiva con Rich para mejor visualización

## 📂 Estructura del Proyecto

```
PhotoCampus/
│
├── 📁 modelo_datos/            # Modelos de datos
│   ├── __init__.py
│   └── servicio_fotografico.py # Clase para representar servicios
│
├── 📁 interfaz_usuario/        # Componentes de la interfaz de usuario
│   ├── __init__.py
│   ├── menu.py                 # Menús y opciones del sistema
│   └── gestor_interfaz.py      # Funciones de interfaz para gestionar servicios
│
├── 📁 servicios/               # Lógica de negocio
│   ├── __init__.py
│   └── gestor_servicios.py     # Gestión de servicios fotográficos
│
├── 📁 almacenamiento/          # Persistencia de datos
│   ├── __init__.py
│   └── gestor_datos.py         # Funciones para cargar y guardar datos
│
├── 📁 utilidades/              # Herramientas auxiliares
│   ├── __init__.py
│   └── herramientas.py         # Funciones de utilidad general
│
├── 📁 respaldos/               # Respaldos automáticos de datos
│
├── 📁 exportaciones/           # Archivos exportados
│
├── main.py                     # Punto de entrada principal
│
└── fotografia.json             # Archivo de datos principal
```

## 🛠️ Requisitos

- Python 3.8+
- Bibliotecas:
  - rich: Para interfaces de texto enriquecidas
  - colorama: Para colores en consola

## 📦 Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/PhotoCampus.git
   ```

2. Navega al directorio del proyecto:
   ```
   cd PhotoCampus
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## 🚀 Uso

Para iniciar el sistema, ejecuta:

```
python main.py
```

## 🗂️ Almacenamiento de Datos

Los datos se almacenan en formato JSON en el archivo `fotografia.json`. Cada vez que se realiza una modificación, se crea automáticamente una copia de respaldo en la carpeta `respaldos/`.

## 📊 Estadísticas

El sistema genera estadísticas sobre:
- Precio promedio, mínimo y máximo de los servicios
- Distribución por tipo de evento
- Distribución por duración

## 📄 Exportación

El sistema permite exportar el catálogo de servicios en:
- 📝 Formato de texto plano (.txt)
- 📊 Formato CSV (.csv)

## 🤝 Contribución

Si deseas contribuir a este proyecto, por favor:

1. Haz un Fork del proyecto
2. Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios
4. Haz commit de tus cambios (`git commit -m 'Agrega nueva funcionalidad'`)
5. Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
6. Abre un Pull Request


---

Desarrollado con ❤️ para PhotoCampus


### 📄 Creado Por:
Este Proyecto fue desarrollado por ***Daniel Santiago Vinasco - Bryan Villabona***

-------------------------------------------------------

---

### ·README_Incluye:
### ✅ ¿Qué incluye este README?
✔ 📋 Características detalladas del sistema de gestión de photocampus.  
✔ 📁 Estructura del proyecto clara y organizada para una fácil navegación.  
✔ 🖥️ Código del menú principal con opciones intuitivas para la administración.  
✔ 📊 Funciones clave como gestión de servicios , editar y eliminar.  
✔ 💾 Estructura de los JSON con ejemplos detallados de productos y pedidos.  
✔ 🚀 Instalación y uso con pasos claros para ejecutar el sistema.  
✔ 🎨 Estética profesional con emojis y formato Markdown limpio para una mejor experiencia visual.  


----------------------------------------------

- 🔥 **¡Github: https://github.com/DanielSantiagoV?tab=repositories !🚀**
- 🔥 **¡Github: https://github.com/BryanVillabona?tab=repositories ! 🚀**