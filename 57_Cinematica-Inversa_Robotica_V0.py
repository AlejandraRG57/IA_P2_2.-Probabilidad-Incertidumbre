#Alejandra Rodriguez Guevara 21310127 6E1

#La cinemática inversa es un problema clave en robótica que implica determinar las configuraciones de las articulaciones de un robot necesarias 
#para lograr una posición y orientación específicas del extremo del efector final (end-effector), como una pinza o una herramienta.

import numpy as np

#Función para calcular la cinemática inversa de un robot 2-DOF.
def inverse_kinematics(x, y, l1, l2):
    #Calculamos la distancia al extremo del efector desde el origen.
    d = np.sqrt(x**2 + y**2)
    
    #Calculamos el ángulo de la articulación del primer eslabón.
    alpha = np.arctan2(y, x)
    
    #Calculamos el ángulo de la articulación del segundo eslabón usando la ley de cosenos.
    beta = np.arccos((l1**2 + d**2 - l2**2) / (2 * l1 * d))
    
    #Calculamos los ángulos de las articulaciones.
    theta1 = alpha + beta
    theta2 = np.arccos((l1**2 + l2**2 - d**2) / (2 * l1 * l2))
    
    return np.degrees(theta1), np.degrees(theta2)

#Coordenadas deseadas del extremo del efector.
x_deseado = 5
y_deseado = 5

#Longitudes de los eslabones del robot.
longitud_eslabon1 = 4
longitud_eslabon2 = 4

#Calculamos la cinemática inversa.
theta1, theta2 = inverse_kinematics(x_deseado, y_deseado, longitud_eslabon1, longitud_eslabon2)

print("Ángulo de la articulación 1:", theta1)
print("Ángulo de la articulación 2:", theta2)