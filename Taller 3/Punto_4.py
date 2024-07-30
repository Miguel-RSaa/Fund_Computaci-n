import numpy as np  # Importa la biblioteca NumPy para cálculos numéricos
import matplotlib.pyplot as plt  # Importa la biblioteca Matplotlib para crear gráficos

# Definición de parámetros
A = 0.3  # Amplitud en metros
k = 4  # Constante del resorte en kg/s^2
gamma = 0.15  # Coeficiente de amortiguamiento en s^-1
m = 9  # Masa en kg

# Definir el intervalo de tiempo
t = np.linspace(0, 25, 500)  # Genera 500 puntos de tiempo entre 0 y 25 segundos

# Calcular y(t) usando la fórmula dada
# y(t) = A * exp(-gamma * t) * cos(sqrt(k/m) * t)
y = A * np.exp(-gamma * t) * np.cos(np.sqrt(k / m) * t)

# Crear la figura y el gráfico
plt.figure(figsize=(10, 6))  # Configura el tamaño de la figura
plt.plot(t, y, label='y(t)')  # Dibuja la curva de y(t) contra el tiempo t
plt.title('Movimiento oscilatorio amortiguado')  # Añade un título al gráfico
plt.xlabel('Tiempo (s)')  # Etiqueta el eje x
plt.ylabel('Posición y(t) (m)')  # Etiqueta el eje y
plt.grid(True)  # Añade una cuadrícula al gráfico para mejor lectura
plt.legend()  # Añade una leyenda para identificar la curva
plt.show()  # Muestra el gráfico