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

    def __eq__(self, other):
        """
        Dos coordenadas serán iguales si sus x e y son iguales
        """
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        else:
            # no son de la misma clase, así que no hay nada que pensar
            return False

    def __hash__(self) :
        """
        Para calcular el hash de dos números, lo más sencillo es 
        calcular el hash de un tupla de esos dos números. Con eso no 
        me tengo que preoucpar por calcular los hash de cad auno de ellos
        y representar un total que tenga en cuenta el orden.
        
        Hemos aplicado **transforma y vencerás**, transformando dos números
        en otra cosa para la cual ya tenemos el calculo del hecho, testado
        y comprobado.

        El crear a un 'pringao' temporal al cual le endosamos un trabajo sucio
        (creamos una tupla y le dejamos que calcule ella el hash) es una aplicación
        muy común del **transforma y vencerás**. Al pringao en cuestión, se le
        llama `Proxy` y es un patrón de diseño muy común.

        Se podría haber hecho lo mismo en el caso de `__eq__`. 
        """
        return hash((self.x, self.y))