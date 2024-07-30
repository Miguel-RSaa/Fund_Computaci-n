def matriz_borde_unos(n):
    # Creamos una matriz `n x n` inicializada con ceros
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    
    # Llenamos los bordes con unos
    for i in range(n):
        matriz[0][i] = 1  # Borde superior
        matriz[n-1][i] = 1  # Borde inferior
        matriz[i][0] = 1  # Borde izquierdo
        matriz[i][n-1] = 1  # Borde derecho

    return matriz

# Ejemplo de uso:
n = 5
for fila in matriz_borde_unos(n):
    print(fila)
