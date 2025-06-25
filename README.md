# Pruebas automatizadas: Campo "name" en creación de kits – Urban Grocers

Este proyecto contiene pruebas automatizadas del campo `name` del endpoint de creación de kits en la API de Urban Grocers. El objetivo es verificar cómo responde el sistema ante diferentes valores ingresados, tanto válidos como inválidos, de acuerdo con una lista de comprobación predefinida.

## Objetivo

Validar el comportamiento del campo `name` en la creación de kits, comprobando:
- Límites mínimos y máximos de longitud
- Inclusión de caracteres especiales, espacios y números
- Omisión del campo o tipo de dato incorrecto

## Estructura del repositorio

- `configuration.py`: configuración del entorno (URL base).
- `data.py`: contiene los valores de prueba utilizados.
- `sender_stand_request.py`: funciones que gestionan las solicitudes HTTP.
- `create_kit_name_kit_test.py`: contiene los casos de prueba automatizados.
- `.gitignore`: excluye archivos no relevantes del repositorio.
- `README.md`: este archivo con instrucciones y contexto del proyecto.

## Cómo ejecutar las pruebas

1. Clona este repositorio:
   git clone git@github.com:Dovahkiin2507/qa-project-Urban-Grocers-app-es.git

2. Instala las dependencias necesarias:
   pip install requests pytest

3. Inicia el servidor de pruebas desde la plataforma correspondiente.

4. Ejecuta las pruebas:
   pytest create_kit_name_kit_test.py

## Casos cubiertos

Se probaron nueve escenarios distintos:
1. Nombre de 1 carácter.
2. Nombre de 511 caracteres.
3. Nombre vacío.
4. Nombre de 512 caracteres.
5. Caracteres especiales.
6. Espacios incluidos.
7. Solo números.
8. Campo `name` omitido.
9. Tipo de dato incorrecto (número en lugar de string).

## Conclusiones

Este conjunto de pruebas automatizadas permite validar de forma rápida y precisa la lógica de validación del campo `name` en la API. Las pruebas fueron ejecutadas correctamente, y se confirmó que el sistema responde como se espera: acepta los valores válidos y rechaza los incorrectos con errores controlados. Este enfoque mejora la eficiencia del proceso de QA y garantiza consistencia frente a futuras actualizaciones del producto.
