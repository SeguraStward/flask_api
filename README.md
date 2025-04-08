# Flask API para usuarios aleatorios

Este proyecto es una API en Flask que genera 75 usuarios aleatorios utilizando la API de **RandomUser.me**. La API responde con una lista de usuarios en formato JSON.

## Requisitos

Antes de empezar, necesitas tener instalados los siguientes programas:

- **Python 3.6+**: Asegúrate de tener una versión reciente de Python instalada en tu sistema.
- **Pip**: El gestor de paquetes de Python.
- **Flask**: El framework web que usaremos para crear la API.

## Pasos de Instalación

### 1. Instalar Python

Si no tienes Python instalado, sigue estos pasos:

- **Windows**:
  1. Ve a la [página oficial de Python](https://www.python.org/downloads/).
  2. Descarga la versión más reciente de Python para Windows.
  3. Durante la instalación, asegúrate de marcar la opción **"Add Python to PATH"**.
  
### 2. Crear un entorno virtual

Un entorno virtual te permite aislar las dependencias del proyecto. Para crear uno:

1. Abre la terminal o línea de comandos.
2. Navega al directorio de tu proyecto.
3. Ejecuta el siguiente comando para crear un entorno virtual:

   **Windows**:
   ```bash
   py -3 -m venv .venv
   .venv\Scripts\activate
   pip install Flask Flask-cors
   pip install flask requests

