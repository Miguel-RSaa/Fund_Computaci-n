
#//Función para generar el diccionario de frecuencias//

#Definimos la funcion
def contar_frecuencias(lista_palabras):
    # Se crea un diccionario vacío para almacenar las frecuencias
    frecuencias = {}
    
    # Recorre cada palabra en la lista
    for palabra in lista_palabras:
        # Si la palabra ya está en el diccionario, incrementar su frecuencia
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        # Si la palabra no está en el diccionario, añadirla con una frecuencia de 1
        else:
            frecuencias[palabra] = 1
    
    # Retornar el diccionario de frecuencias
    return frecuencias

# Ejemplo de uso de la primera función
lista = ["perro", "gato", "perro", "elefante", "gato", "perro"] #Creamos una lista de palabras
frecuencias = contar_frecuencias(lista)#Definimos la funcion
print(frecuencias)  # Output: {'perro': 3, 'gato': 2, 'elefante': 1}

#//Función para encontrar la palabra más repetida

def palabra_mas_frecuente(diccionario_frecuencias):  #Esta función recibe una lista de palabras
    # Se usa la función max() para encontrar la palabra con mayor frecuencia
    # La variable palabra contendrá la palabra más frecuente y frecuencia su frecuencia.
    palabra = max(diccionario_frecuencias, key=diccionario_frecuencias.get)
    frecuencia = diccionario_frecuencias[palabra]
    
    # Retornar una tupla con la palabra más repetida y su frecuencia
    return palabra, frecuencia

# Ejemplo de uso de la segunda función
# Usamos el diccionario 'frecuencias' generado anteriormente
resultado = palabra_mas_frecuente(frecuencias)
print(resultado)  # Output: ('perro', 3)