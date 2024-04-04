#Alejandra Rodriguez Guevara 21310127 6E1

#Los Mapas Autoorganizados de Kohonen (SOM) son una técnica de aprendizaje no supervisado que permite visualizar y 
#organizar datos de alta dimensión en un espacio de baja dimensión, generalmente bidimensional.

import numpy as np #Importamos las librerias necesarias.
import matplotlib.pyplot as plt
from minisom import MiniSom

#Generamos datos de ejemplo.
np.random.seed(0)
data = np.random.rand(100, 2) #100 muestras de 2 dimensiones.

#Definimos el tamaño del SOM.
grid_size = 10
som = MiniSom(grid_size, grid_size, 2, sigma=0.5, learning_rate=0.5)

#Inicializamos el SOM con los datos de entrada.
som.random_weights_init(data)
print("Entrenando el SOM...")
som.train_random(data, 100) #Entrenamos el SOM con 100 iteraciones.

#Obtenemos las posiciones de los nodos en el SOM y visualizamos los datos.
plt.figure(figsize=(8, 8))
plt.pcolor(som.distance_map().T, cmap='bone_r') #Visualizamos el mapa de distancias.
plt.colorbar()

#Colocamos los marcadores de los datos en el mapa.
for i, x in enumerate(data):
    w = som.winner(x)
    plt.plot(w[0] + 0.5, w[1] + 0.5, 'o', markerfacecolor='None', markeredgecolor='r', markersize=10, markeredgewidth=2)

plt.title('Mapa Autoorganizado de Kohonen') #Agregamos un titulo al grafisco.
plt.show() #Mostramos el grafico.