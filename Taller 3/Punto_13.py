def elementos_multiplos_tres(arreglo):
    # Creamos una nueva lista para almacenar los elementos múltiplos de tres
    resultado = [num for num in arreglo if num % 3 == 0]
    return resultado

# Ejemplo de uso:
arreglo = [1, 3, 4, 6, 9, 10]
print(elementos_multiplos_tres(arreglo))  # Salida: [3, 6, 9]
