# Readme
## Reto ambulancias


A continuación se describe la estructura definida para la ejecución de la API.

## Crear ambulancia [POST]:

- Campos definidos (Body de la petición):
    - license_plate (String de máximo 6 caracteres)
    - zone (String)
    - id (Autogenerado)
    - status (String: ACTIVA ó INACTIVA)
    - latitude (Numero, permite decimales)
    - longitude (Numero, permite decimales)
- Al ser el ID autogenerado, se permite la creación de una ambulancia con la misma placa, ya que esta no es única
- Respuestas:
    - Exito: 
        - Codigo 201
        - message: Mensaje de confirmación.
    - Error:
        -  code: Código de error
        -  description: Descrición del error
        -  name: Nombre del error

## Obtener ambulancias activas [GET]:
- Respuestas:
    - Exito:
        - Codigo 200
        - Lista con las ambulancias activas

## Obtener ambulancias cercanas [GET]:
- Campos definidos (Body de la petición):
    - latitude (Numero, permite decimales)
    - longitude (Numero, permite decimales)
- Respuestas:
    - Exito: 
        - Codigo 200
        - Lista con las ambulancias activas ordenadas desde la más cercana hasta la más lejana.
    - Error:
        -  code: Código de error
        -  description: Descrición del error
        -  name: Nombre del error
## Instalación y ejecución

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

El proyecto ejecutará en localhost

## Postman
Descargar [Postman](https://www.postman.com/downloads/)  para la ejecución de la API. 

## Importar collection 
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/d5f2d22ffede776c3167?action=collection%2Fimport) 




