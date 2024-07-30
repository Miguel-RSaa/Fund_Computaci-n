import numpy as np

def diferencia_arreglos(a, b):
    # Usamos np.setdiff1d para encontrar los elementos en 'a' que no están en 'b'
    resultado = np.setdiff1d(a, b)
    return resultado

# Ejemplo de uso:
a = np.array([0, 10, 20, 40, 60, 80])
b = [10, 30, 40, 50, 70]
print(diferencia_arreglos(a, b))  # Salida: [ 0 20 60 80]
