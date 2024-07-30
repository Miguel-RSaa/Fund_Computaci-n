import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
A = 1.0      # Amplitud de la oscilación en metros (m)
omega = 2.0  # Frecuencia angular en radianes por segundo (rad/s)
m = 1.0      # Masa en kilogramos (kg)
k = m * omega**2  # Constante del resorte en Newtons por metro (N/m)

# Definir el intervalo de tiempo
t_max = 10   # Tiempo máximo en segundos
dt = 0.01    # Intervalo de tiempo en segundos
t = np.arange(0, t_max, dt)  # Arreglo de tiempos

# Funciones de posición, velocidad y aceleración
x = A * np.cos(omega * t)  # Posición (m)
v = -A * omega * np.sin(omega * t)  # Velocidad (m/s)
a = -A * omega**2 * np.cos(omega * t)  # Aceleración (m/s^2)

# Funciones de energía potencial y cinética
E_p = 0.5 * k * x**2  # Energía potencial (J)
E_k = 0.5 * m * v**2  # Energía cinética (J)
E_total = E_p + E_k  # Energía total (J)

# Graficar posición, velocidad y aceleración
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, x, label='Posición (x)')
plt.ylabel('Posición (m)')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, v, label='Velocidad (v)', color='orange')
plt.ylabel('Velocidad (m/s)')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, a, label='Aceleración (a)', color='green')
plt.xlabel('Tiempo (s)')
plt.ylabel('Aceleración (m/s²)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Graficar energía potencial y cinética
plt.figure(figsize=(10, 6))
plt.plot(t, E_p, label='Energía Potencial (E_p)')
plt.plot(t, E_k, label='Energía Cinética (E_k)', color='orange')
plt.plot(t, E_total, label='Energía Total (E_total)', color='green')
plt.xlabel('Tiempo (s)')
plt.ylabel('Energía (J)')
plt.legend()
plt.grid(True)
plt.title('Energías del Sistema')
plt.show()
