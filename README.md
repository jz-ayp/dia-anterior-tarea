# Funciones

## Ejercicio: Día anterior

## Instrucciones
- Elabora el análisis y el algoritmo ***antes de escribir el código***. Utiliza un diagrama de flujo para representar tu algoritmo e ilustrar su lógica.
    - [diagrams.net](https://app.diagrams.net/) es una herramienta gratuita y fácil de usar con la que puedes crear diagramas de flujo y se puede usar directamente en VS Code mediante la extensión `Draw.io Integration`.

- **Diseña un programa para calcular el día anterior a una fecha dada**.
  - El programa recibirá tres números enteros que representarán, respectivamente, el día, el mes y el año correpondientes a una fecha dada. 
  - El programa calculará, a continuación, la fecha correspondiente al día anterior a la fecha introducida.
  - Considerar que se recibirán como entrada valores correspondientes a una fecha válida, es decir, no es necesario validar las entradas.

- Codifica tu solución en el archivo [`dia_anterior.py`](dia_anterior.py).

- Para tu referencia, el archivo [`dia_siguiente.py`](dia_siguiente.py) contiene el código trabajado en clase. También se te proporciona el [diagrama de flujo correspondiente al día siguiente](assets/dia_siguiente.drawio).
   
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

- Añade una cadena de documentación (*docstring*) como la siguiente al inicio de tu programa:
  ```
  '''
  Tarea: <Nombre de la tarea y del ejercicio>
  Autor: <Tu nombre>
  Fecha de entrega: DD/MMM/YYYY
  Grupo: <Tu grupo ESI-XXXX-XX>
  Profesor: <Nombre del profesor>

  Descripción:
  <Una breve descripción del programa>
  '''
  ```
  
## Entrega
1. Completa este ejercicio y compila el enunciado, análisis, diagrama de flujo, código y pruebas de ejecución en un informe, tal como se describe en los [requisitos para entrega de tareas](assets/report_example.pdf). No olvides incluir portada y conclusiones.

2. Sube el informe (.pdf) y los archivos con el código fuente (.py) a Canvas.

## Casos de prueba de ejemplo
| Entradas | Salidas |
|:---------|:--------|
| `25`<br>`3`<br>`2021` | `24`<br>`3`<br>`2021` |
| `1`<br>`3`<br>`2021` | `28`<br>`2`<br>`2021` |
| `1`<br>`1`<br>`2021` | `31`<br>`12`<br>`2020` |
| `1`<br>`3`<br>`2020` | `29`<br>`2`<br>`2020` |

## Rúbrica
Verifica tu entrega contra esta rúbrica para maximizar tu calificación. Los puntos se indican en porcentaje.

| Criterio | Puntos |
|----------|--------|
| Entrega:<br>Todos los archivos fueron entregados tal como se indicó.<br>El informe:<br>- tiene portada con todos los datos requeridos,<br>- en formato PDF,<br>- las conclusiones incluyen los elementos indicados en el documento de requerimientos. | 5 |
| Código:<br>- incluido como texto en el informe, no como captura de pantalla,<br>- con tipo de letra de ancho fijo,<br>- espaciado sencillo,<br>- sin líneas que alcancen el margen. | 5 |
| Análisis:<br>- identifica todas las entradas y salidas necesarias,<br>- no clasifica como entrada una salida o viceversa,<br>- no nombra entradas o salidas innecesarias.<br>- El proceso es claro,<br>- no es una simple repetición del enunciado,<br>- sino un acercamiento a la solución, y<br>- no incluye seudocódigo. | 15 |
| *Docstring*:<br>- presente en la parte superior del programa, <br>- tiene el formato exacto indicado en las instrucciones, y<br>- su contenido fue editado por el estudiante.<br>Comentarios:<br>- hay comentarios en el programa,<br>- describen claramente el propósito del código, y<br>- siguen los lineamientos del PEP8<br>[PEP8 Comments](https://www.python.org/dev/peps/pep-0008/#comments) | 5 |
| Identificadores:<br>- usan [snake case](https://en.wikipedia.org/wiki/Snake_case), y<br>- son descriptivos del dato que representan.<br>[PEP8 Naming Conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions) | 5 |
| Formato de salidas:<br>- conforme al ejemplo en las instrucciones. | 5 |
| Diagrama de flujo:<br>- es claro y legible,<br>- corresponde con la lógica del programa,<br>- usa las formas geométricas correctas, y<br>- está en formato png<br>[Cómo subir diagramas de flujo a GitHub](https://youtu.be/oy5nhA7QpNI) | 15 |
| Pruebas de ejecución:<br>- son suficientes para comprobar la funcionalidad del programa,<br>- al menos una de las capturas de pantalla muestra el escritorio completo, y<br>- son legibles. | 15 |
| Funcionalidad:<br>- pasa los casos de prueba de ejemplo, y<br>- pasa los casos de prueba reservados por el profesor. | 30 |

Estos puntajes son equivalentes, aproximadamente, a la siguiente ponderación:
- Presentación: 20%
- Funcionalidad: 60%
- Pruebas: 20%
