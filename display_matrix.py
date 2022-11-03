from beautifultable import BeautifulTable

def display_matrix(matrix):
    """
    Imprime una matriz 
    """
    tb = BeautifulTable()
    for column in matrix:
        tb.columns.append(column)
    print(tb)

