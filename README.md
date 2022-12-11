# Reto ambulancias

A continuación se describe la estructura e instrucciones para la ejecución de la API.

---
***Importante: Leer las notas al final del documento***

---

## Postman
Descargar [Postman](https://www.postman.com/downloads/). 

## Importar colección 
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/d5f2d22ffede776c3167?action=collection%2Fimport) 

---
# Definición de endpoints

## get_token [GET]:

1. Entrada (Query parameters):
    - user (string)
    - password (string)
2. Respuesta:
    - Exito:
        - Codigo 200
        - token: token generado
    - Error:
        -  code: Código de error
        -  description: Descrición del error
        -  name: Nombre del error

## create_ambulance [POST]:

1. Entrada (Body de la petición):
    - license_plate (String de máximo 6 caracteres)
    - zone (String)
    - id (Autogenerado)
    - status (String: ACTIVA ó INACTIVA)
    - latitude (Numero, permite decimales)
    - longitude (Numero, permite decimales)
2. Respuestas:
    - Exito: 
        - Codigo 201
        - message: Mensaje de confirmación.
    - Error:
        -  code: Código de error
        -  description: Descrición del error
        -  name: Nombre del error
3. Al ser el ID autogenerado, se permite la creación de una ambulancia con la misma placa, ya que esta no es única

## get_ambulances [GET]:
1. Respuestas:
    - Exito:
        - Codigo 200
        - Lista con las ambulancias activas

## nearby_ambulances [GET]:
1. Campos definidos (Query parameters):
    - latitude (Numero, permite decimales)
    - longitude (Numero, permite decimales)
2. Respuestas:
    - Exito: 
        - Codigo 200
        - Lista con las ambulancias activas ordenadas desde la más cercana hasta la más lejana.
    - Error:
        -  code: Código de error
        -  description: Descrición del error
        -  name: Nombre del error

---
# Instalación y ejecución

Se requiere [Python 3.11](https://www.python.org) para ejecutar.
Y se recomienda ejecutar dentro de un entorno virtual

Instalar virtualenv

```sh
pip install virtualenv
```

Crear un entorno virtual dentro del proyecto (se recomienda el nombre "env")

```sh
py -m venv env
```

Activar el entorno virtual

```sh
.\env\Scripts\activate
```

Instalar las dependencias del proyecto

```sh
pip install -r .\requirements.txt
```

Entrar a la carpeta "src"

```sh
cd .\src\ 
```

Ejecutar con Python el archivo main.py

```sh
py main.py
```
---
# Notas

1. Se creo un diccionario local con información de algunas ambulancias
2. El usuario y contraseña para la generación de token es "test"
3. Validar las variables de la colección de Postman en caso de que el programa se ejecute en un puerto diferente al parametrizado.
