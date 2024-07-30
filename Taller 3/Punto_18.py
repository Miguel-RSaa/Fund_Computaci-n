import numpy as np
import matplotlib.pyplot as plt

def camino_borracho(n):
    """
    Simula el camino de un borracho que da 'n' pasos aleatorios en una cuadrícula.

    Parámetros:
    n (int): Número de pasos que da el borracho.

    Retorna:
    tuple: Dos listas con las coordenadas x e y del camino del borracho.
    """
    # Inicializamos las coordenadas x e y del borracho en el origen (0, 0)
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    
    # Iteramos sobre cada paso que da el borracho
    for i in range(n):
        # Elegimos una dirección aleatoria entre las cuatro posibles: izquierda, derecha, arriba, abajo
        direccion = np.random.choice(['izquierda', 'derecha', 'arriba', 'abajo'])
        
        if direccion == 'izquierda':
            # Moverse a la izquierda disminuye la coordenada x
            x[i + 1] = x[i] - 1
            y[i + 1] = y[i]
        elif direccion == 'derecha':
            # Moverse a la derecha aumenta la coordenada x
            x[i + 1] = x[i] + 1
            y[i + 1] = y[i]
        elif direccion == 'arriba':
            # Moverse hacia arriba aumenta la coordenada y
            x[i + 1] = x[i]
            y[i + 1] = y[i] + 1
        elif direccion == 'abajo':
            # Moverse hacia abajo disminuye la coordenada y
            x[i + 1] = x[i]
            y[i + 1] = y[i] - 1
    
    return x, y

def calcular_distancia(x, y):
    """
    Calcula la distancia euclidiana desde el origen (0, 0) a la posición final.

    Parámetros:
    x (array): Coordenadas x del camino.
    y (array): Coordenadas y del camino.

    Retorna:
    float: La distancia euclidiana desde el origen.
    """
    # La distancia euclidiana se calcula usando la fórmula sqrt(x^2 + y^2)
    return np.sqrt(x[-1]**2 + y[-1]**2)

def visualizar_camino(x, y):
    """
    Visualiza el camino del borracho en un gráfico 2D.

    Parámetros:
    x (array): Coordenadas x del camino.
    y (array): Coordenadas y del camino.
    """
    plt.figure(figsize=(8, 8))
    # Graficamos el camino con marcadores y líneas conectando los puntos
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title('Camino del Borracho')
    plt.xlabel('Coordenada x')
    plt.ylabel('Coordenada y')
    plt.grid(True)
    plt.show()

# Parámetros de la simulación
n = 1000  # Número de pasos

# Simulación del camino del borracho
x, y = camino_borracho(n)

# Cálculo de la distancia final desde el origen
distancia_final = calcular_distancia(x, y)
print(f'Distancia final: {distancia_final:.2f}')

# Cálculo de la raíz cuadrada de n, que es el valor teórico esperado para la distancia
valor_teorico = np.sqrt(n)
print(f'Valor teórico (raíz cuadrada de n): {valor_teorico:.2f}')

# Visualización del camino en un gráfico
visualizar_camino(x, y)
