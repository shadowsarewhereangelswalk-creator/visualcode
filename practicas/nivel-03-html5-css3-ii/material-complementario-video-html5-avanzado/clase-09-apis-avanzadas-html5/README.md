# Clase 09 — APIs avanzadas de HTML5

Video: https://www.youtube.com/watch?v=CdPMeBs0cag

Ejercicio reconstruido a partir de la transcripción de **HTML5 Nivel 2 — APIs avanzadas de HTML5**.

## Qué practica

La práctica principal de la clase es **Drag and Drop**:

- Elemento con `draggable="true"`.
- Eventos `dragstart`, `dragover` y `drop`.
- `event.preventDefault()` para permitir el destino.
- `dataTransfer.setData(...)` y `getData(...)`.
- Traslado del elemento entre dos contenedores.
- Ambos contenedores funcionan como origen y destino.
- Estilos CSS para diferenciar las zonas.

La clase también introduce conceptualmente **WebSocket** y **WebRTC**. Esos dos temas ya cuentan con un ejemplo complementario en:

- `../05-websocket-webrtc.html`
- `../comunicacion.js`

## Archivos

- `ejemplo-09.html`
- `estilos.css`
- `drag-drop.js`
- `imagen-html5.svg`

## Refuerzo

Duplica el elemento arrastrable y modifica el JavaScript para que puedas mover varias tarjetas entre las dos zonas.
