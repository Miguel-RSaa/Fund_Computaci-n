def calcular_precio(inmueble):
    """
    Calcula el precio de un inmueble basado en su antigüedad, metros cuadrados, 
    número de habitaciones, presencia de garaje y zona.

    Parámetros:
    inmueble (dict): Diccionario que contiene información sobre el inmueble.

    Retorna:
    float: El precio calculado del inmueble.
    """
    # Extraemos el año de construcción, metros cuadrados, número de habitaciones y si tiene garaje
    año = inmueble['año']
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    garaje = 1 if inmueble['garaje'] else 0  # Convertimos el valor booleano a 1 o 0
    zona = inmueble['zona']
    
    # Calculamos la antigüedad del inmueble en años
    antigüedad = 2024 - año
    
    # Calculamos el precio basado en la zona del inmueble
    if zona == 'A':
        # Fórmula para la zona A
        precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antigüedad / 100)
    elif zona == 'B':
        # Fórmula para la zona B
        precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antigüedad / 100) * 1.5
    else:
        # Manejo de zona inválida
        raise ValueError("Zona no válida")
    
    return precio

def buscar_inmuebles(inmuebles, presupuesto):
    """
    Busca inmuebles que estén dentro del presupuesto dado y añade el precio calculado a cada uno.

    Parámetros:
    inmuebles (list of dict): Lista de diccionarios, cada uno representando un inmueble.
    presupuesto (float): El presupuesto máximo para filtrar los inmuebles.

    Retorna:
    list of dict: Lista de inmuebles cuyo precio es menor o igual al presupuesto.
    """
    # Lista para almacenar los inmuebles que cumplen con el presupuesto
    inmuebles_filtrados = []
    
    # Iteramos sobre cada inmueble en la lista
    for inmueble in inmuebles:
        # Calculamos el precio del inmueble usando la función calcular_precio
        precio = calcular_precio(inmueble)
        # Añadimos el precio al diccionario del inmueble
        inmueble['precio'] = precio
        
        # Verificamos si el precio es menor o igual al presupuesto
        if precio <= presupuesto:
            # Si está dentro del presupuesto, lo añadimos a la lista de inmuebles filtrados
            inmuebles_filtrados.append(inmueble)
    
    return inmuebles_filtrados

# Ejemplo de uso:
# Lista de inmuebles, cada uno representado por un diccionario con sus características
inmuebles = [
    {'a~no': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'a~no': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'a~no': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'a~no': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'a~no': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

# Definimos un presupuesto para la búsqueda
presupuesto = 50000

# Llamamos a la función para obtener inmuebles dentro del presupuesto
resultados = buscar_inmuebles(inmuebles, presupuesto)

# Imprimimos los resultados
for inmueble in resultados:
    print(inmueble)
