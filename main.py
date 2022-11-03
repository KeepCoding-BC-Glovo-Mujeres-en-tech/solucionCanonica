from display_matrix import display_matrix
from process_matrix import process_matrix

if __name__ == '__main__':
    m = [[0,1,2,1],[2,2,3,1],[0,2,3,9],[72,3,6,9]]

    print("\n\nMatriz original")
    print('===================')
    display_matrix(m)

    print('\n\nMatriz procesada')
    print('===================')
    p = process_matrix(m)
    display_matrix(p)

    print('\n\nProcesada 100 veces')
    print('========================')
    for i in range(99):
        p = process_matrix(p)
    display_matrix(p)