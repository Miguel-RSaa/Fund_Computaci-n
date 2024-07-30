import numpy as np

def elementos_en_arreglo(a, b):
    # Usamos np.isin para comprobar si cada elemento de 'a' está en 'b'
    # np.isin(a, b) retorna un arreglo booleano con True en las posiciones donde
    # el elemento de 'a' está presente en 'b' y False donde no está.
    resultado = np.isin(a, b)
    
    # Retornamos el arreglo booleano resultante
    return resultado

# Ejemplo de uso:
a = np.array([0, 10, 20, 40, 60])  # Arreglo 'a'
b = np.array([0, 40])              # Arreglo 'b'
print(elementos_en_arreglo(a, b))  # Salida: [ True False False  True False]
