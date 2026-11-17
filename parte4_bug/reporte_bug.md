# Reporte de bug: cantidad de camisas en el carrito tras rotar el teléfono

## Título

La cantidad de camisas del carrito vuelve de 3 a 1 al girar el teléfono en Android 13

## Entorno

- Dispositivo: Samsung
- Modelo: No fue indicado por el usuario
- SO: Android 13
- Versión de ShopGo: No fue indicada
- Orientación inicial: Por confirmar

## Precondiciones

- Mantener ShopGo abierta y una camisa disponible para agregar al carrito
- Encontrarse en el carrito con la cantidad de esa camisa en 3 antes de girar el teléfono

## Pasos para reproducir

1. Abrir ShopGo en un Samsung con Android 13
2. Agregar una camisa al carrito y poner la cantidad a 3
3. Confirmar que la fila de la camisa muestra 3 unidades
4. Sin salir del carrito, girar el celular a la orientación contraria
5. Verificar nuevamente la cantidad mostrada para esa misma camisa

Importante: Los pasos anteriores son una propuesta para llegar a reproducir el reporte del usuario, así mismo, todavía no se han ejecutado en un dispositivo

## Resultado esperado

1. La camisa debe mantener sus 3 unidades después de la rotación
2. Girar la pantalla no tendria que modificar el carrito

## Resultado actual

Según el usuario, la cantidad mostrada vuelve a 1 tras girar el teléfono, así mismo,no se ha llegado a saber si el cambio afecta solo a la pantalla o también al carrito guardado

## Severidad y prioridad

1- Severidad: Media, ya que el usuario puede terminar comprando una cantidad distinta de la elegida, aunque no se ha confirmado pérdida de datos al finalizar la compra

2- Prioridad: Alta, ya que la rotación puede ocasionarse en el transcurso normal de la compra y el cambio de cantidades pasa inadvertido si el usuario no vuelve a revisar el carrito

## Evidencia que solicitaría

- Video en donde se demuestre la cantidad en 3, la rotación y el cambio a 1, con el modelo del dispositivo y la versión del app
- Pantallazos del carrito antes y después de girar, mostrando la misma camisa y su cantidad.
- Logs del app alrededor de la rotación y, si existe, el estado del carrito enviado o recibido por la API.

 Solicitar esta evidencia; no está adjunta al reporte original.

## Preguntas abiertas

- ¿Cuál es el modelo del Samsung?
- ¿Cuál es la versión de ShopGo?
- ¿La rotación fue de vertical a horizontal o al revés? 
- ¿Sucede constantemente o solo algunas veces?
- Al volver a la orientación inicial o reabrir el carrito, ¿la cantidad sigue en 1? Esto ayudaría a distinguir un problema visual de un cambio en los datos del carrito
- ¿En qué pantalla estaba el usuario cuando giró el teléfono: dentro del carrito o en otra pantalla?