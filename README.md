# Solución Canónica de Procesamiento de una Matriz

Tenemos que crear la función `process_matrix` que recibe una matriz de números y procesa cada uno de ellas de la siguiente manera:
  
  El nuevo valor de cada uno de ellos es el promedio del valor antiguo y los valores de sus vecinos.

La función devolverá una nueva matriz con los valores cambiados siguiendo el algoritmo descrito.

## Plan de Acción (Divide y Vencerás)

Consideramos una matriz como una lista de columnas. Vamos a recorrer cada uno de los elementos y llevar a cabo las siguientes tareas:

* Por cada uno de los elementos
* Obtenemos una lista de las coordenadas de sus vecinos
* Transformamos esa lista de coordenadas en una lista de valores
* Calculamos el promedio y actualizamos el valor original

## Principales Escollos

### Diferentes números de vecinos según el punto

El principal problema, tal y como se describe en el enunciado, es que los puntos de la matriz tendrán diferentes vecinos, según sean puntos internos, en los bordes de la matriz o en las esquinas.

Para evitar complicaciones, tres casos de punto que tenemos que comprobar, aplicaremos  **Transforma y Vencerás & Cerveza para todos**:

* Consideramos que todos los puntos son _internos_, con lo cual todos tendrán 4 vecinos.
* Esto nos generará una lista de coordenadas, que en la mayoría de los casos será correcta, pero en algunos (esquinas y bordes) contendrá coordenadas inválidas. Estas últimos serán filtradas antes de obtener los valores. Lo hacemos así, porque eliminar coordenadas incorrectas es más sencilla que generar de entrada la lista de las correctas.

Además, también consideraremos que todo punto *también es su propio vecino*. Con esto nos facilitamos la tarea de obtener el promedio.

### Representación de unas coordenadas

Cada punto está definido por sus coordenadas (i & j). Tenemos que representar dos números juntos. Para ello hay varias opciones:

* una lista de dos números
* una tupla de dos números
* una clase

Lo más lógico en este caso es la tercera opción. Puede parecer una tontería, pero una de las clases más útiles que existen es la que se usa para representar una pareja: dos objetos distintos que se tratan como uno solo.

Nosotros declararemos una clase Coord que tiene dos componentes, x e y.

## Deberes

Todo el contenido del fichero neighbours.py, en el fondo debería de ser un método de
la clase `Coord`. Al fin y al cabo, lo que me gustaría es poder pedirle a un `Coord`
cuales son sus vecinos y que me dé una lista con ellos. 
Implementa el método `getNeighbours(self)` en `Coord`.