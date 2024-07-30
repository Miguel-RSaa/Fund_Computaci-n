def suma_pares(arreglo):
    """
    Esta función toma un arreglo de enteros y retorna la suma de los números pares.
    
    Parámetros:
    arreglo (list): Lista de enteros.
    
    Retorna:
    int: Suma de los números pares en el arreglo.
    """
    # Inicializar la suma de los números pares
    suma = 0
    
    # Recorrer cada número en el arreglo
    for numero in arreglo:
        # Verificar si el número es par
        if numero % 2 == 0:
            # Añadir el número a la suma
            suma += numero
    
    # Retornar la suma de los números pares
    return suma

# Ejemplo de uso de la función
arreglo_ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = suma_pares(arreglo_ejemplo)
print(f"La suma de los números pares en el arreglo es: {resultado}")
