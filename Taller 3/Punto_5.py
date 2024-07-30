# Importamos numpy para manejar los arreglos y realizar cálculos matemáticos, y matplotlib.pyplot para graficar.
import numpy as np
import matplotlib.pyplot as plt

# Definimos los valores de theta, que va de 0 a 2*pi en 1000 pasos
theta = np.linspace(0, 2 * np.pi, 1000)

# Definimos la función r(theta) que calcula la distancia en función de theta y la excentricidad e
def r(theta, e):
    return 1 / (1 + e * np.cos(theta))

# Definimos las excentricidades que queremos graficar
e_values = [0, 0.5, 0.8]

# Creamos una figura para la primera gráfica
plt.figure(figsize=(10, 6))

# Iteramos sobre los valores de excentricidad
for e in e_values:
    # Calculamos r(theta) para la excentricidad actual
    r_values = r(theta, e)
    # Graficamos r(theta) vs theta
    plt.plot(theta, r_values, label=f'e = {e}')

# Etiquetas y título para la gráfica
plt.xlabel('θ (radianes)')
plt.ylabel('r (UA)')
plt.title('Distancia del planeta a la estrella en función de la posición angular')
# Mostramos la leyenda
plt.legend()
# Mostramos la cuadrícula
plt.grid(True)
# Mostramos la gráfica
plt.show()

# Creamos una figura para la segunda gráfica
plt.figure(figsize=(10, 6))

# Iteramos sobre los valores de excentricidad
for e in e_values:
    # Calculamos r(theta) para la excentricidad actual
    r_values = r(theta, e)
    # Calculamos las coordenadas x e y
    x = r_values * np.cos(theta)
    y = r_values * np.sin(theta)
    # Graficamos y vs x
    plt.plot(x, y, label=f'e = {e}')

# Etiquetas y título para la gráfica
plt.xlabel('x (UA)')
plt.ylabel('y (UA)')
plt.title('Órbitas reales del planeta')
# Mostramos la leyenda
plt.legend()
# Mostramos la cuadrícula
plt.grid(True)
# Aseguramos que los ejes tengan la misma escala
plt.gca().set_aspect('equal')
# Mostramos la gráfica
plt.show()
