from operator import ne
from neighbours import get_neighbours, _naive_get_neighbours, _remove_out_of_range
from coord import Coord

def test_out_of_range():
    # Suponinedo una matriz de 2x3
    # y por lo tanto los rangos validos son:
    # x 0, 1
    # y 0, 2 
    x_valid_range = range(2)
    y_valid_range = range(3)

    in0 = Coord(0,0)
    in1 = Coord(1,2)
    in2 = Coord(1,1)

    out0 = Coord(-1, 0)
    out1 = Coord(1, -10)
    out2 = Coord(-1, 20)

    assert in0.inside(x_valid_range, y_valid_range)
    assert in1.inside(x_valid_range, y_valid_range)
    assert in2.inside(x_valid_range, y_valid_range)
    
    assert out0.inside(x_valid_range, y_valid_range) == False
    assert out1.inside(x_valid_range, y_valid_range) == False
    assert out2.inside(x_valid_range, y_valid_range) == False

def test_naive_get_neighbours():
    c0 = Coord(0,0)
    c1 = Coord(2, 3)

    assert _naive_get_neighbours(c0) == set([Coord(0,1), Coord(1,0), Coord(-1,0), Coord(0,-1)])
    assert _naive_get_neighbours(c1) == set([Coord(2,4), Coord(3,3), Coord(1,3), Coord(2,2)])

def test_remove_out_of_range():
    # suponinedo matrix de 4x4
    xr = range(4)
    yr = range(4)

    # rincón superior izquierdo
    corner0 = _naive_get_neighbours(Coord(0,0))
    neighbours = _remove_out_of_range(corner0, xr,yr)
    assert len(neighbours) == 2
    assert neighbours == set([Coord(0,1), Coord(1,0)])


    ## rincón inferiro derecho
    corner1 = _naive_get_neighbours(Coord(3,3))
    neighbours = _remove_out_of_range(corner1, xr,yr)
    assert len(neighbours) == 2
    assert neighbours == set([Coord(2,3), Coord(3,2)])


    corner2 = _naive_get_neighbours(Coord(0,3))
    neighbours = _remove_out_of_range(corner2, xr,yr)
    assert len(neighbours) == 2

    corner3 = _naive_get_neighbours(Coord(3,0))
    neighbours = _remove_out_of_range(corner3, xr,yr)
    assert len(neighbours) == 2

    border0 = _naive_get_neighbours(Coord(0, 2))
    neighbours = _remove_out_of_range(border0, xr,yr)
    assert len(neighbours) == 3


    border1 = _naive_get_neighbours(Coord(3, 1))
    neighbours = _remove_out_of_range(border1, xr,yr)
    assert len(neighbours) == 3

    interior0 = _naive_get_neighbours(Coord(1,1))
    neighbours = _remove_out_of_range(interior0, xr,yr)
    assert len(neighbours) == 4
    assert neighbours == interior0


    interior1 = _naive_get_neighbours(Coord(2,1))
    neighbours = _remove_out_of_range(interior1, xr,yr)
    assert len(neighbours) == 4
    assert neighbours == interior1


    

    
