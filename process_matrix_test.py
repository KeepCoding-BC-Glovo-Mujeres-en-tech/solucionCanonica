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
    r1 = [[1.5,1.5,2.5,3.5]]
    r2 = [[1,1.5],[1.5, 2]]

    assert process_matrix(m0) == r0
    assert process_matrix(m1) == r1
    assert process_matrix(m2) == r2
    