def valores_comunes(a, b):
    # Convertimos las listas en conjuntos para facilitar la intersección
    conjunto_a = set(a)
    conjunto_b = set(b)
    
    # Encontramos la intersección de los dos conjuntos
    comunes = conjunto_a & conjunto_b
    
    # Convertimos el resultado de nuevo a una lista y lo retornamos
    return list(comunes)

# Ejemplo de uso:
a = [0, 10, 20, 40, 60]
b = [10, 30, 40]
print(valores_comunes(a, b))  # Salida: [10, 40]
