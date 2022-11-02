class Coord(object):
    """
    Clase que representa las coordenadas de un punto. 
    La usaremos para generar la lista de vecinos, 
    y luego dicha lista de coordenadas la transformaremos 
    en una lista de valores que reduciremos a un promedio.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<{self.__class__.__name__}: ({self.x}{self.y})>'

    