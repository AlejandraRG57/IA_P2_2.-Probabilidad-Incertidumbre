#Alejandra Rodriguez Guevara 21310127 6E1

#El espacio de configuración es un concepto fundamental en el análisis de movimiento de robots. Se refiere al conjunto de todas las 
#posibles configuraciones que puede adoptar un robot dentro de su entorno. 

import numpy as np
import matplotlib.pyplot as plt

#Definimos el tamaño del entorno.
width = 10
height = 10

#Creamos una cuadrícula para representar el espacio de configuración.
x = np.linspace(0, width, 100)
y = np.linspace(0, height, 100)
X, Y = np.meshgrid(x, y)

#Visualizamos el espacio de configuración.
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, np.zeros_like(X), cmap='gray', alpha=0.1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Espacio de Configuración')
plt.grid(True)
plt.show()