# ShopGo — prueba técnica QA Automation Mobile

Este repositorio contiene los casos de prueba de inicio de sesión, las validaciones de contraseña y envío con sus pruebas automatizadas, un ejemplo de automatización móvil para el login y un reporte de bug sobre el carrito

## Contenido

- `Casos de prueba/AndreySanchezDelgado_CasosPrueba_PT.xlsx`: casos de prueba de login
- `shopgo/validaciones.py`: reglas de contraseña y costo de envío
- `tests/test_validaciones.py`: pruebas de las reglas con pytest
- `pages/login_page.py`: acciones y elementos de la pantalla de login mediante Page Object
- `tests/conftest.py`: fixture de ejemplo para crear y cerrar un driver de Appium
- `tests/test_login.py`: escenarios de login correcto e incorrecto
- `parte4_bug/reporte_bug.md`: reporte del problema de cantidad del carrito luego de girar el teléfono
- `NOTAS.md`: suposiciones, alcance de la verificación y uso de AI

## Preparar el entorno

Requerimientos: Python y PowerShell, asi mismo, desde la carpeta raíz del proyecto:

Ejecutar en powershell: 

1- python -m venv .venv

2- .\.venv\Scripts\Activate.ps1

3- python -m pip install -r requirements.txt

Es para crear un entorno virtual e instalar los requirements, asi mismo, si el entorno virtual ya existe, basta con activarlo e instalar las dependencias. `requirements.txt` incluye `pytest` y `Appium-Python-Client`; este último es el cliente de Python, no el servidor de Appium.

## Ejecutar las pruebas disponibles

Desde la terminal de powershell

1- python -m pytest tests/test_validaciones.py -v

En la revisión pasaron las 20 pruebas de validaciones, con objetivo de comprobar que pytest descubre los escenarios móviles sin iniciar una sesión:

2- python -m pytest tests/test_login.py --collect-only -q

Se descubrieron dos pruebas de login. **No se ejecutaron**: el driver contiene una ruta de APK y datos de dispositivo de ejemplo, y no se dispone de una app ni de un servidor Appium para verificar la interfaz. La consigna no exige ejecutar esa parte en un emulador

## Alcance de la entrega

Las pruebas de `test_login.py` ilustran el flujo esperado y los locators indicados por la consigna. Por otro lado, las credenciales son de ejemplo, ya que, no constituyen evidencia de que el login funcione en una aplicación real, asi mismo, el reporte de bug parte de la observación de un usuario; sus pasos son una propuesta de reproducción, no una ejecución confirmada
