def producto_impares(arreglo):
    # Inicializamos el producto en 1, que es el neutro multiplicativo.
    producto = 1
    # Una bandera para verificar si hay números impares en el arreglo.
    tiene_impares = False

    # Iteramos sobre cada número en el arreglo.
    for num in arreglo:
        # Verificamos si el número es impar. 
        # Un número es impar si al dividirlo por 2 el residuo no es 0.
        if num % 2 != 0:
            # Si es impar, lo multiplicamos con el producto actual.
            producto *= num
            # Marcamos que hemos encontrado al menos un número impar.
            tiene_impares = True

    # Si hemos encontrado al menos un número impar, retornamos el producto.
    # Si no encontramos números impares, retornamos 0.
    return producto if tiene_impares else 0

# Ejemplo de uso:
arreglo = [2, 3, 4, 5, 6]
print(producto_impares(arreglo))  # Salida: 15 (porque 3 * 5 = 15)
