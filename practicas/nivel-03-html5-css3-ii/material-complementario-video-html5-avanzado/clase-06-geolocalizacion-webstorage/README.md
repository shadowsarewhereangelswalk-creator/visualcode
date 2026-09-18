# Clase 06 — Geolocalización y Web Storage

Ejercicios reconstruidos a partir de la clase **HTML5 Nivel 2 — APIs de Geolocalización y Web Storage**.

## Ejemplo 06 — Geolocalización

`ejemplo-06.html`:

- Comprueba si `navigator.geolocation` está disponible.
- Solicita la posición con `getCurrentPosition`.
- Muestra latitud y longitud.
- Mantiene deshabilitado el botón de mapa hasta obtener coordenadas.
- Abre la ubicación en OpenStreetMap.
- Maneja los códigos de error de permiso denegado, posición no disponible y tiempo de espera.
- Cambia el mensaje a verde cuando obtiene la posición y a rojo cuando ocurre un error.

La API de geolocalización suele requerir HTTPS o `localhost`.

## Ejemplo 06-01 y 06-02 — localStorage

`ejemplo-06-01-localstorage.html` guarda `nombreCurso` y `nivelCurso`, muestra los valores y permite eliminarlos con `removeItem`.

`ejemplo-06-02-recuperar-localstorage.html` recupera los mismos valores desde otra página del mismo origen para mostrar la persistencia de `localStorage`.

## Ejemplo 06-03 y 06-04 — sessionStorage

`ejemplo-06-03-sessionstorage.html` guarda y muestra las variables de sesión.

`ejemplo-06-04-recuperar-sessionstorage.html` intenta recuperarlas sin volver a asignarlas. Para comprobar la separación por contexto de navegación, abre esta página manualmente en una pestaña independiente.

## Archivos

- `ejemplo-06.html`
- `ejemplo-06-01-localstorage.html`
- `ejemplo-06-02-recuperar-localstorage.html`
- `ejemplo-06-03-sessionstorage.html`
- `ejemplo-06-04-recuperar-sessionstorage.html`
- `estilos.css`
