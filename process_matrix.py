from list_utils import all_true, average
from neighbours import get_neighbours
from coord import Coord

# Esta es la única función "publica" y l aúnica que habría que importar
# al usar este módulo. Todas las demás son caosas internas
# que no le importan al usario de nuestro módulo
def process_matrix(matrix):
    """
    Recebe un matriz de números y devuelve una nueva en la cual, cada 
    valor es el promedio del anterior y de sus vecinos.

    Requisitos:

    1. La matriz es un alista de listas
    1. Las listas son todas del mismo tamaño
    1. Los elementos son siempre números
    1. La matriz NO tiene por qué ser cuadrada
    """
    if _is_valid_numerical_matrix(matrix):
        # la procesamos
        return _process_matrix(matrix)
    else:
        raise ValueError('The input is not a valid numerical matrix')

def _is_valid_numerical_matrix(matrix):
    """"
    Comprueba que todas las listas de la listade listas tengan 
    la misma longitud y que todos los elementos sena numéricos
    """
    if matrix == []:    # caso trivial
        return True
    else:
        # divide y vencerás
        return _is_list_of_lists(matrix) and _all_lists_same_size(matrix) and _all_elements_numerical(matrix)

def _is_list_of_lists(matrix):
    return all_true(matrix, lambda l : type(l) == list)

def _all_lists_same_size(matrix):
    first_len = len(matrix[0])
    return all_true(matrix, lambda l : len(l) == first_len)

def _all_elements_numerical(matrix):
    result = True
    for sub_list in matrix:
        result = all_true(sub_list, lambda x: type(x) == int or type(x) == float)
        if result == False:
            break
    return result


def _process_matrix(matrix):

    processed = []
    for i, column in enumerate(matrix):
        processed_column = []
        for j, element  in enumerate(column):
            # Por cada elemento,
            element_coord = Coord(i,j)
            # obtengo la lista de vecinos
            neighbours = get_neighbours(element_coord, matrix)
            # lo transformo en una lista de valores
            values = _get_values(neighbours, matrix)
            # calculo el promedio y actualizo
            processed_column.append(average(values))
        # añado la columna procesada
        processed.append(processed_column)


    
    
    
    return processed

def _get_values(coords, matrix):
    """
    Recibe un set de coordenadas y una matriz y devuelve una **lista**
    de valores.
    
    Se devuelve una lista de valores y no un set, porque podría darse la 
    casualidad de que dos (o más) coordenadas tuviesen el mismo valor y eso 
    se perdería con u set (no puede haber cosas repetidas)
    """
    values = []
    for coord in coords:
        values.append(matrix[coord.x][coord.y])
    return values
