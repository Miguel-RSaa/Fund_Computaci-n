# Definimos la función
def palabra_mas_larga(lista_palabras):
    # Se comprueba si la lista está vacía. Si lo está, retorna una tupla con None y 0
    if not lista_palabras:
        return None, 0
    
    # La función max() para encontrar la palabra más larga en la lista.
    # key=len se usa para determinar cual sera el rango maximo de la longitud de la palabra
    palabra_mas_larga = max(lista_palabras, key=len)
    
    # Retorna la palabra más larga y su longitud en una tupla.
    return palabra_mas_larga, len(palabra_mas_larga)

# Ejemplo de uso:
# Creamos una lista y la funcion que va a ser palabra_mas_larga con la lista
lista = ["perro", "gato", "hipopótamo", "elefante"]
resultado = palabra_mas_larga(lista) # Imprimimos el resultado
print(resultado)  # Output: ('hipopótamo', 10)