# Pruebas para el campo name en la solicitud de creación de un kit de productos

# Descripción

- Este proyecto contiene un conjunto de pruebas automatizadas para verificar el correcto funcionamiento de la API de Urban.Grocers que permite la creación de kits de productos dentro de un usuario. Se utiliza pytest y requests para la automatización de pruebas.

# Documentación

- Para la documentación de la API, se recomienda utilizar apiDoc.

# Tecnologías y Técnicas Utilizadas

- Python: Lenguaje de programación principal del proyecto.

- pytest: Framework para la ejecución de pruebas automatizadas.

- PyCharm: Entorno de desarrollo utilizado para la implementación del proyecto.

- requests: Librería para realizar solicitudes HTTP.

- apiDoc: Herramienta recomendada para documentar la API.

- Principios de pruebas automatizadas: Se aplican buenas prácticas para la verificación de respuestas HTTP y validación de datos.

# Configuración del Proyecto

- Opción 1: Configuración en la Terminal

1. Clonar el repositorio:  
```
   git clone <URL_DEL_REPOSITORIO>
   ```
2. Crear un entorno virtual y activarlo:
   ```
   python -m venv venv
   source venv/bin/activate  # En MacOS/Linux
   venv\Scripts\activate  # En Windows
   ```
3. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```
### Opción 2: Configuración en PyCharm
1. Abrir PyCharm y seleccionar **Open** para abrir la carpeta del proyecto.
2. Ir a **File > Settings > Project: <nombre_del_proyecto> > Python Interpreter**.
3. Crear un nuevo entorno virtual seleccionando **Add Interpreter > Add Local Interpreter > Virtualenv**.
4. Seleccionar la opción de crear un nuevo entorno en la carpeta `venv` dentro del proyecto.
5. Instalar las dependencias abriendo la terminal en PyCharm y ejecutando:
   ```
   pip install -r requirements.txt
   ```

## Ejecución de Pruebas
### Desde la Terminal
Para ejecutar las pruebas, usa el siguiente comando:
   ```
   pytest qa-project-Urban-Grocers-app-es/create_kit_name_kit_test.py
   ```
Si cambias el nombre o la ubicación del archivo, asegúrate de actualizar la ruta en el comando de ejecución.

### Desde PyCharm
1. Abrir el archivo de prueba dentro de PyCharm.
2. Hacer clic derecho dentro del archivo y seleccionar **Run 'pytest in <archivo>'**.
3. También puedes ejecutar todas las pruebas desde la terminal integrada de PyCharm con:
   ```
   pytest
   ```
