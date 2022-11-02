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
    pass

def _process_matrix(matrix):

    # Por cada elemento,
    # obtengo la lista de vecinos
    # lo transformo en una lista de valores
    # calculo el promedio y actualizo
    pass
