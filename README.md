# Sistema de Apoyos (Stack y Queue)

## Descripción del Proyecto

Este proyecto implementa un sistema web en Python usando Flask que gestiona un "Sistema de Apoyos" utilizando dos estructuras de datos fundamentales:

- **Cola (Queue)**: Para la entrega de tarjetas de apoyo (simula personas esperando su tarjeta)
- **Pila (Stack)**: Para el historial de apoyos recibidos (simula apoyos que se pueden "deshacer")

## Estructura del Proyecto

```
proyecto/
├── app.py                 # Aplicación principal Flask
├── README.md             # Documentación del proyecto
├── models/               # Directorio de modelos de datos
│   ├── pila.py          # Implementación de la clase PilaApoyos
│   └── cola.py          # Implementación de la clase ColaTarjetas
└── templates/            # Directorio de plantillas HTML
    ├── menu.html         # Plantilla del menú principal
    ├── cola.html         # Plantilla para gestión de cola
    └── pila.html         # Plantilla para gestión de pila
```

## Funcionalidades

### 1. Menú Principal (`/` o `/menu`)
- Interfaz principal que permite elegir entre:
  - **Entregar Tarjetas** (Cola)
  - **Historial de Apoyos** (Pila)

### 2. Gestión de Cola (`/cola`)
- **Agregar Persona**: Formulario para encolar personas en la cola
- **Procesar Tarjeta**: Botón para desencolar y entregar tarjeta a la primera persona
- **Visualización**: Muestra la cola actual con estadísticas

### 3. Gestión de Pila (`/pila`)
- **Agregar Apoyo**: Formulario para empilar apoyos al historial
- **Remover Apoyo**: Botón para desempilar el último apoyo (deshacer)
- **Visualización**: Muestra la pila actual con indicador de tope

## Clases TDA Implementadas

### PilaApoyos (`models/pila.py`)
```python
class PilaApoyos:
    def empilar(apoyo)      # Agregar apoyo a la pila
    def desempilar()        # Remover y retornar último apoyo
    def esta_vacia()        # Verificar si la pila está vacía
    def mostrar_pila()      # Retornar lista de apoyos
    def obtener_tamano()    # Retornar número de elementos
```

### ColaTarjetas (`models/cola.py`)
```python
class ColaTarjetas:
    def encolar(persona)    # Agregar persona a la cola
    def desencolar()        # Remover y retornar primera persona
    def esta_vacia()        # Verificar si la cola está vacía
    def mostrar_cola()      # Retornar lista de personas
    def obtener_tamano()    # Retornar número de elementos
```

## Tecnologías Utilizadas

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3, Bootstrap 5, Font Awesome
- **Estructuras de Datos**: Lista (implementación de Pila y Cola)

## Instalación y Ejecución

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd proyecto
   ```

2. **Instalar Flask** (si no está instalado)
   ```bash
   pip install flask
   ```

3. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

4. **Abrir en el navegador**
   ```
   http://localhost:5000
   ```

## Características de la Interfaz

### Diseño Responsivo
- Interfaz adaptativa para diferentes tamaños de pantalla
- Diseño moderno con gradientes y animaciones CSS
- Iconografía intuitiva con Font Awesome

### Experiencia de Usuario
- Mensajes informativos para cada acción
- Botones deshabilitados cuando no hay elementos
- Visualización clara del estado de las estructuras
- Navegación intuitiva entre secciones

### Características Visuales
- **Cola**: Fondo rojo/naranja, elementos se muestran horizontalmente
- **Pila**: Fondo verde/turquesa, elementos se muestran verticalmente con indicador de tope
- **Menú**: Fondo púrpura/azul con opciones claramente diferenciadas

## Funcionamiento de las Estructuras

### Cola (FIFO - First In, First Out)
- Las personas se agregan al final de la cola
- Las tarjetas se entregan a la primera persona en la cola
- Simula un sistema de atención por orden de llegada

### Pila (LIFO - Last In, First Out)
- Los apoyos se agregan al tope de la pila
- Solo se puede remover el último apoyo agregado
- Simula un sistema de "deshacer" o historial reversible

## Autor

Desarrollado como proyecto de Estructuras de Datos para demostrar la implementación práctica de estructuras de datos fundamentales en una aplicación web.

## Licencia

Este proyecto es de uso educativo y demostrativo. 