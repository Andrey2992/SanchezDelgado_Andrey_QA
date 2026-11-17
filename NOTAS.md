# Notas de entrega

## Decisiones y suposiciones

- `validar_password` devuelve `False` para `None`, texto vacío, longitudes fuera de 8 a 20 caracteres, ausencia de mayúscula o número y presencia de un espacio. La función devuelve un booleano, como piden las instrucciones

- Por otro lado, en la parte móvil se usaron los identificadores de accesibilidad indicados en el enunciado, las credenciales, el nombre del dispositivo y la ruta del APK en el código son ejemplos; no representan una app instalada ni una cuenta real

- El reporte de bug se basa en el relato de un usuario con un Samsung y Android 13, ya que, no se llega a conocer el modelo ni la versión de ShopGo, asi mismo, los pasos del reporte son una propuesta para reproducirlo y todavía no se han confirmado en un dispositivo

## Verificación realizada

- `python -m pytest tests/test_validaciones.py -q`: **20 pruebas pasaron**
- `python -m pytest tests/test_login.py --collect-only -q`: pytest descubrió **2 pruebas de login**. No se ejecutaron porque requieren la app y un servidor Appium
- El resultado de la parte móvil describe el código entregado; no demuestra que el flujo funcione en una aplicación real

## Uso de AI

Utilicé ChatGPT/Codex como tutor ya que me gusta entender el ¿porque? y ¿como?, asi mismo, tambien me ayudo a organizar el trabajo, revision de partes de los casos de prueba, y recibir revisiónes en general, asi mismo, tambien para estructurar el README.md

## Revisión personal antes de enviar

- Casos de prueba: Listo 
- Tiempo invertido: 40 mins
