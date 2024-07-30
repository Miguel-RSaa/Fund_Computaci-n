import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
lado_caja = 10  # Tamaño de la caja (10 x 10)
dt = 0.01  # Intervalo de tiempo en segundos
t_max = 20  # Tiempo máximo de simulación en segundos

# Posición inicial de la pelota
x = 5.0  # Posición inicial en x
y = 5.0  # Posición inicial en y

# Velocidad inicial de la pelota
vx = 2.0  # Velocidad inicial en x (m/s)
vy = 3.0  # Velocidad inicial en y (m/s)

# Listas para almacenar la trayectoria
trayectoria_x = [x]
trayectoria_y = [y]

# Bucle de simulación
t = 0
while t < t_max:
    # Actualizar posición
    x += vx * dt
    y += vy * dt
    
    # Verificar colisiones con las paredes y cambiar dirección de velocidad si es necesario
    if x <= 0 or x >= lado_caja:
        vx = -vx
    if y <= 0 or y >= lado_caja:
        vy = -vy
    
    # Almacenar la nueva posición
    trayectoria_x.append(x)
    trayectoria_y.append(y)
    
    # Incrementar tiempo
    t += dt

# Graficar la trayectoria de la pelota
plt.figure(figsize=(8, 8))
plt.plot(trayectoria_x, trayectoria_y, label='Trayectoria de la pelota')
plt.xlim(0, lado_caja)
plt.ylim(0, lado_caja)
plt.axhline(0, color='black')
plt.axhline(lado_caja, color='black')
plt.axvline(0, color='black')
plt.axvline(lado_caja, color='black')
plt.xlabel('Posición en x (m)')
plt.ylabel('Posición en y (m)')
plt.title('Trayectoria de una pelota en una caja de 10x10')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
