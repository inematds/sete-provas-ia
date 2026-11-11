# Prueba 7: Central de agentes

Crea un centro de control para un pequeño equipo de agentes de IA: un planificador, un investigador, un redactor y un revisor.

Escribo un objetivo y veo al equipo planificar, trabajar y revisar en vivo. Puedo pausar o detener una ejecución. Al final recibo un informe claro y puedo abrir ejecuciones anteriores. Si un agente falla, veo el motivo y la ejecución continúa.

En esta versión, cada agente es un simulador: espera unos segundos y devuelve un texto de ejemplo. Coloca ese simulador detrás de una única función, para poder reemplazarlo por un modelo real más adelante. No uses una clave de API.

Archivo principal: `central.html`, que se abre con dos clics. Todo funciona en el navegador; las ejecuciones anteriores quedan guardadas en el propio navegador.

## Esmero
- Haz que se vea realmente bien: quien pase la vista tiene que detenerse y dejar de desplazarse.
- Usa las herramientas y habilidades que tengas (diseño, animación, generador de imágenes). Tú eliges.

## Imágenes (opcional)
- Si esta interfaz genera imágenes, genera como máximo 4 e indica el nombre de archivo de cada una (img1.jpg, img2.jpg...), para que las guarde junto al HTML. En el HTML, usa <img src="img1.jpg"> y muestra un dibujo en SVG o CSS en su lugar si el archivo no existe, para que la página nunca abra con una imagen rota.
- Si no genera, dibuja todo en SVG o CSS dentro del HTML. La prueba vale lo mismo.
- Modo rayos X: la tecla X y un botón pequeño activan los contornos, con un color para cada imagen y otro para cada animación hecha con código, con una etiqueta pequeña en cada uno.

## Cómo entregar (estás en una ventana de chat, sin carpeta)
- Responde con UN archivo HTML completo en un único bloque de código, desde <!doctype html> hasta </html>, con el CSS y JavaScript dentro.
- El archivo tiene que estar completo. Nada de "el resto sigue igual".
- No uses archivos de Internet. Nunca reproduzcas sonido.
- No hagas preguntas. Termina de una vez.
- Después del bloque, en hasta 5 líneas: qué hiciste y cómo abrirlo.
