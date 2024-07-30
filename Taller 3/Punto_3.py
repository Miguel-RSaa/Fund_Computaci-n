#Definimos la funcion
def es_contrasena_buena(contrasena):
    # Aquí comprobamos si la longitud de la contraseña es menor a 8 caracteres. 
    # Si es así, la función retorna False inmediatamente, ya que no cumple con el requisito mínimo de longitud.
    if len(contrasena) < 8:
        return False

    # Las variables para verificar la presencia de los requisitos
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    # Recorremos cada carácter de la contraseña. Utilizamos métodos de cadena para verificar si el carácter es una letra mayúscula (isupper), 
    # una letra minúscula (islower) o un número (isdigit). Si encontramos un carácter que cumpla con alguno de estos requisitos, 
    # actualizamos la variable correspondiente a True.
    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True

    # Después de recorrer todos los caracteres, verificamos si se cumplen todos los requisitos 
    # Si se cumplen, la función retorna True; de lo contrario, retorna False.
    if tiene_mayuscula and tiene_minuscula and tiene_numero:
        return True
    else:
        return False

# Ejemplos de uso
print(es_contrasena_buena("Contraseña123"))  # True
print(es_contrasena_buena("contraseña"))     # False
print(es_contrasena_buena("CONTRASEÑA123"))  # False
print(es_contrasena_buena("Con123"))         # False
print(es_contrasena_buena("Contrasena123"))  # True