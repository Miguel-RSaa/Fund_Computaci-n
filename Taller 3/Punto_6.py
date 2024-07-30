import numpy as np

# Definimos la función f(x) que será evaluada
def f(x):
    # f(x) = sin(x) * ln(x + 1) * sinh(x)
    return np.sin(x) * np.log(x + 1) * np.sinh(x)

# Función para evaluar f(x) en el intervalo [0, 10] con un paso dx
def evaluar_funcion(dx):
    # Abrimos el archivo 'resultados.txt' en modo de escritura
    with open('resultados.txt', 'w') as file:
        # Escribimos el encabezado en el archivo
        file.write('i\tx\tf(x)\n')
        # Inicializamos el contador i en 0
        i = 0
        # Usamos np.arange para crear una secuencia de valores desde 0 hasta 10 con paso dx
        for x in np.arange(0, 10 + dx, dx):
            # Calculamos el valor de f(x) para el valor actual de x
            fx = f(x)
            # Escribimos el índice i, el valor de x y el valor de f(x) en el archivo
            file.write(f'{i}\t{x:.6f}\t{fx:.6f}\n')
            # Incrementamos el contador i
            i += 1

# Solicitamos al usuario que ingrese el valor del paso dx
dx = float(input("Ingrese el valor del paso dx: "))

# Llamamos a la función evaluar_funcion con el valor de dx proporcionado por el usuario
evaluar_funcion(dx)
