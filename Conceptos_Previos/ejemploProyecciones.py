import numpy as np

# Generar datos aleatorios para 100 puntos en el tiempo
tiempo = np.arange(100)
ventas_aleatorias = np.random.rand(10)*1000

# Proyectar las ventas con una tendencia linea
pendiente = 50
interseccion = 1000
ventas_proyectadas = pendiente * tiempo + interseccion + ventas_aleatorias

# Visualizar los resultados 

import matplotlib as plt

plt.plot(tiempo, ventas_proyectadas, label = "Ventas proyectadas")
plt.xlabel("Tiempo")
plt.ylabel("Ventas proyectadas")
plt.legend()
plt.show()