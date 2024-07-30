import numpy as np
import matplotlib.pyplot as plt

# Constante gravitacional
g = 9.8  # m/s^2

# Definimos la función para calcular la trayectoria
def calcular_trayectoria(x0, y0, v0x, v0y, t_max, dt):
    # Calculamos los tiempos
    t = np.arange(0, t_max, dt)
    
    # Calculamos las posiciones en x e y
    x = x0 + v0x * t
    y = y0 + v0y * t - 0.5 * g * t**2
    
    return t, x, y

# Parámetros de simulación
t_max = 10  # tiempo máximo en segundos
dt = 0.01  # intervalo de tiempo en segundos

# Casos iniciales
casos = [
    {'x0': 0, 'y0': 100, 'v0x': 0, 'v0y': 0},
    {'x0': 0, 'y0': 100, 'v0x': 1, 'v0y': 0},
    {'x0': 0, 'y0': 0, 'v0x': 0, 'v0y': 10},
    {'x0': 0, 'y0': 0, 'v0x': 1, 'v0y': 10}
]

# Creamos una figura para las gráficas
plt.figure(figsize=(10, 6))

# Iteramos sobre los casos y graficamos las trayectorias
for i, caso in enumerate(casos):
    t, x, y = calcular_trayectoria(caso['x0'], caso['y0'], caso['v0x'], caso['v0y'], t_max, dt)
    plt.plot(x, y, label=f'Caso {i + 1}')

# Añadimos etiquetas y título
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Trayectorias bajo la influencia de un campo gravitacional constante')
plt.legend()
plt.grid(True)

# Mostramos la gráfica
plt.show()
