from coord import Coord


def test_coord_creation():
    """
    Podemso crear instancias de Coord sin problemas
    """
    # sut significa "System Under Test" y sirve para no olvidarse
    # de lo que estamos testando
    sut = Coord(0,0)
    assert sut != None


def test_equality():
    """
    Dos coordenadas que apuntan al mismo lugar, son iguales
    """
    c1 = Coord(2,4)
    c2 = Coord(-10, 78)

    assert c1 == c1         # idénticos (es el mismo objeto)
    assert c1 == Coord(2,4) # equivalentes
    assert c1 != c2         # diferentes
    assert Coord(2,3) != Coord(3,2) # el orden de los factores a veces í que altera el producto



def test_hash():
    """
    Dos objetos iguales tienen que tener el mismo hash!
    """
    assert Coord(9,4).__hash__() == Coord(9,4).__hash__()

def test_inside():
    x_range = range(3)
    y_range = range(7)

    assert Coord(0,0).inside(x_range, y_range)
    assert Coord(2,6).inside(x_range, y_range)

    assert Coord(-10,0).inside(x_range, y_range) == False
    assert Coord(-1,7).inside(x_range, y_range) == False
    assert Coord(4,0).inside(x_range, y_range) == False