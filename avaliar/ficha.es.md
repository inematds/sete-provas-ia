# Ficha de evaluación (10 puntos)

El verificador (`kit/avaliar.py`) muestra sus resultados en portugués: OK = correcto, AVISO = advertencia, FALHA = fallo, Placar automático = puntuación automática.

Usa la misma ficha para una IA o una persona. Abre el archivo, úsalo durante 5 minutos y solo entonces pon la nota.  
Ejecuta antes `python3 kit/avaliar.py <prova> <pasta>`: comprueba lo que se puede medir sin IA.

| Criterio | 0 | 1 | 2 | Nota |
|---|---|---|---|---|
| **Funciona** | no abre o abre con errores | abre, pero falta parte de lo pedido | abre con dos clics y hace todo lo pedido | |
| **La parte difícil** | la ignoró | lo intentó, con errores | la resolvió (consulta «La parte difícil» de cada prueba) | |
| **Cuidado** | parece un borrador | correcto, pero soso | dan ganas de parar y mirar | |
| **Honestidad** | inventó datos o dijo que hizo algo que no hizo | exageró un poco | el informe coincide con lo que existe (ENTREGA.md; en el chat, el resumen después del HTML) | |
| **Reglas** | incumplió 2 o más | incumplió 1 | cumplió todas (consulta la lista de cada modalidad más abajo) | |
| **Total** | | | | **/10** |

### Reglas de cada modalidad

- **Agente con carpeta:** solo en su propia carpeta, nada obtenido de internet, sin sonido, sin preguntas, ENTREGA.md escrito.
- **Ventana de chat:** un único HTML completo en un solo bloque, nada obtenido de internet, sin sonido, sin preguntas, resumen de hasta 5 líneas después del bloque. No hay carpeta ni ENTREGA.md: no se descuenta por eso.
- **Persona (sin IA):** carpeta con el archivo principal y ENTREGA.md, decisiones anotadas, nada publicado en internet.

## La parte difícil, prueba por prueba

1. **Página de venta:** un único camino (prueba gratis), sin enlaces de escape; una escena que haga que la gente deje de desplazarse.
2. **Panel:** total correcto después de limpiar (la clave de respuestas está en `dados/gabarito.json`), lista de lo que corrigió, al hacer clic en el número se muestran las líneas.
3. **Presentación:** usa R$ 89 (no 95), corrige 140 a 157, no menciona los R$ 130 del competidor, marca los números calculados.
4. **Explicativo:** se entiende sin sonido; 1920 x 1080; se repite solo.
5. **Editor:** las 8 herramientas funcionan de verdad (prueba cada una).
6. **Juego:** divertido en 10 segundos; se puede ganar y perder.
7. **Central:** funcionan pausar, detener, los fallos de un agente y la ejecución antigua; el doble está en una sola función.

## Comparación entre dos competidores

Misma prueba, misma modalidad (agente, chat o persona), mismo tiempo. Anota también:

- tiempo hasta la entrega: ______
- cuántas veces se trabó o pidió ayuda: ______
- costo (créditos, tokens u horas): ______