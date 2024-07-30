import numpy as np

def encontrar_valores_atipicos(muestra):
    """
    Encuentra los valores atípicos en una muestra de números. Un valor se considera atípico si su puntuación
    típica es mayor que 3 o menor que -3.

    Parámetros:
    muestra (array-like): Un arreglo o lista de números en los que se buscan valores atípicos.

    Retorna:
    numpy.array: Un arreglo con los valores atípicos.
    """
    # Convertimos la muestra en un array de NumPy para facilitar los cálculos
    muestra = np.array(muestra)
    
    # Calculamos la media de la muestra
    media = np.mean(muestra)
    
    # Calculamos la desviación estándar de la muestra
    desviacion_estandar = np.std(muestra)
    
    # Calculamos la puntuación típica para cada valor en la muestra
    puntuaciones_tipicas = (muestra - media) / desviacion_estandar
    
    # Identificamos los valores que tienen una puntuación típica mayor que 3 o menor que -3
    valores_atipicos = muestra[(puntuaciones_tipicas > 3) | (puntuaciones_tipicas < -3)]
    
    return valores_atipicos

# Ejemplo de uso:
# Definimos una muestra de números
muestra = [10, 12, 12, 13, 13, 14, 15, 16, 17, 100]

# Encontramos los valores atípicos en la muestra
atipicos = encontrar_valores_atipicos(muestra)

# Imprimimos los valores atípicos encontrados
print("Valores atípicos:", atipicos)
