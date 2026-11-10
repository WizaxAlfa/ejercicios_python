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
        return True



def esAntisimetrica(matriz):
    diagonal = 0
    for fila in matriz:
        for columna in fila:
            if (fila[diagonal] and columna) != 0:
                return False
        diagonal += 1
    return True

if __name__ == '__main__':
    # Test Cases:
    assert esAntisimetrica([[0, 1, 2],
                            [-1, 0, 3],
                            [-2, -3, 0]]) is True

    assert esAntisimetrica([[0, 1, 2, 7],
                            [-1, 0, 3, 5],
                            [-2, -3, 0, 8],
                            [2, 4, 5, 0]]) is True

    assert esAntisimetrica([[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]) is True

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

    print("All tests passed")