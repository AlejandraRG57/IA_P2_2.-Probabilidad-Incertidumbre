#Alejandra Rodriguez Guevara 21310127 6E1

#-> Suavizado (Smoothing): El suavizado en series temporales se refiere al proceso de estimar el estado o el valor 
#pasado de un proceso estocástico utilizando toda la información disponible hasta el momento presente. 

#-> Explicación (Interpretation): La explicación en el contexto de modelos de series temporales implica el análisis e interpretación 
#de los resultados obtenidos a partir de los modelos y métodos utilizados para el filtrado, la predicción y el suavizado. 

import numpy as np #Importamos las librerias necesarias.
import matplotlib.pyplot as plt

#Parámetros del proceso.
delta_t = 0.1 #Intervalo de tiempo entre observaciones.
F = np.array([[1, delta_t], [0, 1]]) #Matriz de transición de estado.
H = np.array([[1, 0]]) #Matriz de observación.

#Varianza del proceso y de la medición.
Q = np.array([[0.1, 0], [0, 0.01]]) #Covarianza del proceso.
R = np.array([[0.5]]) #Covarianza de la medición.

#Condición inicial del estado.
x0 = np.array([[0], [0]]) #Estado inicial.
P0 = np.eye(2) #Covarianza inicial.

#Simulamos el proceso verdadero.
T = 100 #Número de pasos de tiempo.
true_states = np.zeros((2, T))
true_states[:, 0] = x0.flatten()

for t in range(1, T):
    true_states[:, t] = np.dot(F, true_states[:, t-1]) + np.random.multivariate_normal([0, 0], Q)

observations = np.dot(H, true_states) + np.random.normal(0, R[0, 0], (1, T)) #Simulamos las observaciones.

smoothed_states = np.zeros((2, T)) #Suavizado de Kalman.
x_smooth = x0
P_smooth = P0

for t in reversed(range(T)):
    x_smooth = np.dot(F, x_smooth) #Retroceso.
    P_smooth = np.dot(np.dot(F, P_smooth), F.T) + Q
    
    K = np.dot(np.dot(P_smooth, H.T), np.linalg.inv(np.dot(np.dot(H, P_smooth), H.T) + R)) #Ganancia de Kalman.
    
    y = observations[:, t] #Actualizamos.
    x_smooth = x_smooth + np.dot(K, y - np.dot(H, x_smooth))
    P_smooth = P_smooth - np.dot(np.dot(K, H), P_smooth)
    
    smoothed_states[:, t] = x_smooth.flatten()

plt.figure(figsize=(10, 6)) #Graficamos los resultados.
plt.plot(true_states[0], label='Estado Verdadero', color='blue')
plt.plot(observations.flatten(), label='Observaciones', color='green', marker='o', linestyle='None', markersize=5)
plt.plot(smoothed_states[0], label='Estado Suavizado', color='orange')
plt.title('Suavizado con Filtro de Kalman') #Agregamos un titulo.
plt.xlabel('Tiempo') #Agregamos etiquetas al eje X y Y.
plt.ylabel('Estado')
plt.legend() #Agregamos una leyenda.
plt.grid(True) #Mostramos la cuadricula.
plt.show() #Mostramos el gráfico.

#Explicaciones.
print("Explicación:")
print("El suavizado de Kalman se utiliza para estimar el estado pasado del proceso utilizando todas las observaciones disponibles.")
print("Se basa en el principio del filtro de Kalman, pero se ejecuta en orden inverso (retroceso), utilizando tanto información pasada como futura.")
print("El suavizado de Kalman es útil para obtener una estimación más precisa del estado pasado del proceso,")
print("ya que incorpora información futura para mejorar la estimación.")