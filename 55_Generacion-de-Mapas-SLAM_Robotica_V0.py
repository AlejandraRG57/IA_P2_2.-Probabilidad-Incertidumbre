#Alejandra Rodriguez Guevara 21310127 6E1

#La Generación de Mapas y Localización Simultánea (SLAM, por sus siglas en inglés) es un problema fundamental en robótica que implica que 
#un robot construya un mapa de su entorno mientras determina simultáneamente su propia ubicación dentro de ese mapa. 

import numpy as np
import matplotlib.pyplot as plt

#Definimos las funciones de movimiento del robot y las observaciones del sensor.
def move(x, u):
    return x + u

def observe_landmark(x, landmark_pos):
    return np.linalg.norm(x - landmark_pos)

#Parámetros del entorno y del robot.
landmark_pos = np.array([10, 0]) #Posición conocida de la marca en el entorno.
true_position = np.array([0, 0]) #Posición inicial del robot.
u = np.array([1, 0]) # Movimiento del robot.

#Listas para almacenar las posiciones estimadas y observaciones del robot.
estimated_positions = [true_position]
observations = [observe_landmark(true_position, landmark_pos)]

#Realizamos iteraciones para actualizar la posición del robot y estimar el mapa.
for i in range(10):
    #Movimiento del robot.
    true_position = move(true_position, u)
    
    #Observación del sensor.
    observation = observe_landmark(true_position, landmark_pos)
    
    #Almacenar las observaciones y posiciones estimadas.
    observations.append(observation)
    estimated_positions.append(true_position)

#Graficamos el mapa y la trayectoria estimada del robot.
plt.plot(landmark_pos[0], landmark_pos[1], 'ro', label='Landmark')
plt.plot([pos[0] for pos in estimated_positions], [pos[1] for pos in estimated_positions], 'b-', label='Estimated Path')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('SLAM: Estimated Path and Landmark')
plt.legend()
plt.grid(True)
plt.show()