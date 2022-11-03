
from coord import Coord


def get_neighbours(coord, matrix):
    """
    Recibe las coordenadas de un elemento de una matriz y devuelve las coordenadas
    de sus vecinos, como una lista de objetos Coord, siendo que el propio punto es 
    cosniderado un vecino de si mismo.
    """
    # obtengo la lista de vecinos de forma simplona, considerando que se trata de un punto
    # interno.
    neighbours = _naive_get_neighbours(coord)
    # Elimino aquellos vecinos que tienen coordenadas fuera del rango de
    # la matriz (range(0, len(matrix)))
    xrange = range(len(matrix))
    yrange = range(len(matrix[0]))
    neighbours = _remove_out_of_range(neighbours, xrange, yrange)
    # me añado a mi mismo y devuevlo
    neighbours.add(coord)
    return neighbours


def _naive_get_neighbours(coord):
    """
    Recibo un objeto Coord y devuelvo un  Set con sus 4 vecinos,
    tanto si existen como si no.

    Uso un Set en vez de una lista, porque quiero asegurarme de que 
    nunca hay un elemento repetido y además el orden no importa.

    Los sets se pueden iterar con un for in, al igual que una lista
    """
    x = coord.x
    y = coord.y
    return set([Coord(x+1, y), Coord(x, y+1), Coord(x, y-1), Coord(x-1, y)])

def _remove_out_of_range(coords, x_range, y_range):
    """
    Función que recibe una lista de coords y elimina los que tienen
    valores de x e y fuera de un rango. Para eso también recibe dos
    objtos de tipo range que representan el rango válida para cada una
    de las dimensiones
    """
    def _ok(coord):
        if coord.x in x_range and coord.y in y_range:
            return True
        else:
            return False
    new_set = set(filter(_ok, coords))
    return new_set
    