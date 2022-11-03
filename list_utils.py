# Algunas funciones varias, que en su mayoría hemos visto a lo largo del módulo
from functools import reduce

def all_true(elements, predicate):
    """
    Recibe una lista y un predicado. Devueltrue True si TODOS los
    elementos de la lista pasan el test del rpedicado. Pariente de `filter`
    """
    result = True
    for element in elements:
        if predicate(element) != True:
            result = False
            break
    return result


def average(values):
    """
    Recibe una lista de números y devuelve su promedio
    """
    return reduce(lambda x, y: x + y, values) / len(values)