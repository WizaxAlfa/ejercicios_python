# Define una rutina que devuelve True si una matriz es
# atisimetrica y False en otro caso. 
# Una matriz n*n es antisimetrica si se verifica que 
# sus elementos mantienen la relación:
# matriz[i][j] = - matriz[j][i] 
# para cada i=0,1,...,n-1 y para cada j=0,1,...,n-1.


def esMatrizCuadrada(matriz):
    numeroFilas = len(matriz)
    for fila in matriz:
        if len(fila) != numeroFilas:
            return False

def esAntisimetrica(matriz):
    
    for fila in matriz:
        return matriz[0] == matriz[1] == matriz[2]   

if __name__ == '__main__':
    # Test Cases:
    '''assert esAntisimetrica([ [0, 1, 2],
[-1, 0, 3],
[-2, -3, 0]]) is True'''

    assert esAntisimetrica([[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]) is True

'''
    assert esAntisimetrica([ [0, 1, 2],
                            [-1, 0, -2],
                            [2, 2, 3]]) is False

    assert esAntisimetrica([ [1, 2, 5],
                            [0, 1, -9],
                            [0, 0, 1]]) is False
    
    assert esAntisimetrica([ [1, 2,  5],
                            [-2, 1, -9],
                            [-5, 0, 1]]) is False


    # casos test que no satisfacen la precondicion de que la matriz sea cuadrada:
    matriz5 = [[1, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 1]]

    assert esAntisimetrica(matriz5) is False

    matriz6 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

    assert esAntisimetrica(matriz6) is False

    matriz7 = [[1, 0, 0, 0],
                [0, 1, 0],
                [0, 0, 0, 1]]

    assert esAntisimetrica(matriz7) is False


    # casos test matriz cuadrada:
    assert esMatrizCuadrada([[1, 0, 0, 0],
                            [0, 1, 1, 0],
                            [0, 0, 0, 1]]) is False

    assert esMatrizCuadrada([[1, 0, 0, 0, 0, 0, 0, 0, 0]]) is False

    assert esMatrizCuadrada([[1, 2, 3, 4],
                            [-2, 1, 5],
                            [-3, -5, 1, 1]]) is False

    assert esMatrizCuadrada([[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]) is True

    print("All tests passed")'''