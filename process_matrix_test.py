from process_matrix import process_matrix, _is_valid_numerical_matrix


def test_empty_list():
    """
    La matriz vacía es una matriz válida
    """
    assert process_matrix([]) == []
    assert _is_valid_numerical_matrix([]) == True

def test_wrong_matrices():
    assert _is_valid_numerical_matrix([[1,2,3], [0], [9]]) == False # longitudes diferentes
    assert _is_valid_numerical_matrix([[4,5,6],[9, 7, '42']]) == False # valor no numérico
    assert _is_valid_numerical_matrix([1,2,3,4,5]) == False     # no es lista de listas


def test_valid_matrices():
    m0 = [[0,0], [0,0]]
    m1 = [[1,2,3,4]]
    m2 = [[0,1],[1, 2]]

    r0 = [[0,0], [0,0]]
    r1 = [[1.5,2.0,3,3.5]]
    r2 = [[2/3,1],[1, 4/3]]

    p0 = process_matrix(m0)
    assert p0 == r0

    p1 = process_matrix(m1)
    assert p1 == r1

    p2 = process_matrix(m2)
    assert p2 == r2
