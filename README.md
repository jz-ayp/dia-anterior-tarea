# Funciones

## Ejercicio: Día anterior

## Instrucciones
- Elabora el análisis y el algoritmo ***antes de escribir el código***. Utiliza un diagrama de flujo para representar tu algoritmo e ilustrar su lógica.

- **Diseña un programa para calcular el día anterior a una fecha dada**.
  - El programa recibirá tres números enteros que representarán, respectivamente, el día, el mes y el año correpondientes a una fecha dada. 
  - El programa calculará, a continuación, la fecha correspondiente al día anterior a la fecha introducida.
  - Considerar que se recibirán como entrada valores correspondientes a una fecha válida, es decir, no es necesario validar las entradas.

- Codifica tu solución en el archivo [`dia_anterior.py`](dia_anterior.py).

- Para tu referencia, el archivo [`dia_siguiente.py`](dia_siguiente.py) contiene el código trabajado en clase. También se te proporciona el [diagrama de flujo correspondiente al día siguiente](assets/dia_siguiente.drawio.svg).
   
- Utiliza los siguientes ejemplos para dar formato a tus entradas y salidas:
  ```
  Fecha inicial:
      Día: 25
      Mes: 3
      Año: 2021
  Un día antes:
      Día: 24
      Mes: 3
      Año: 2021
  
  Fecha inicial:
      Día: 1
      Mes: 3
      Año: 2021
  Un día antes:
      Día: 28
      Mes: 2
      Año: 2021
  ```
  
- Prueba tu programa corriéndolo varias veces con diferentes entradas. Verifica que tu algoritmo produzca las salidas correctas. Identifica y pon atención especial a los casos que pudieran ser problemáticos de manejar (casos límite).

- Añade la correspondiente cadena de documentación (*docstring*) al inicio de tu programa.
  
## Entrega
Completa este ejercicio y compila el enunciado, análisis, diagrama de flujo, código y pruebas de ejecución en un informe, tal como se describe en los requisitos para entrega de tareas en Canvas. No olvides incluir portada y conclusiones.

## Casos de prueba de ejemplo
| Entradas | Salidas |
|:---------|:--------|
| `25`<br>`3`<br>`2021` | `24`<br>`3`<br>`2021` |
| `1`<br>`3`<br>`2021` | `28`<br>`2`<br>`2021` |
| `1`<br>`1`<br>`2021` | `31`<br>`12`<br>`2020` |
| `1`<br>`3`<br>`2020` | `29`<br>`2`<br>`2020` |

## Rúbrica
Verifica tu entrega contra la rúbrica disponible en Canvas para maximizar tu calificación.
