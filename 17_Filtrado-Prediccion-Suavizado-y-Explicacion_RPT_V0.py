#Alejandra Rodriguez Guevara 21310127 6E1

#-> Filtrado (Filtering): El filtrado en el contexto de series temporales se refiere al proceso de estimar el estado 
#o el valor actual de un proceso estocástico utilizando toda la información disponible hasta el momento actual.

#-> Predicción (Prediction): La predicción implica estimar el estado o el valor futuro de un proceso estocástico 
#utilizando información disponible hasta el momento presente.

import numpy as np #Importamos las librerias necesarias.
import matplotlib.pyplot as plt

#Parámetros del proceso
delta_t = 0.1 #Intervalo de tiempo entre observaciones.
F = np.array([[1, delta_t], [0, 1]]) #Matriz de transición de estado.
H = np.array([[1, 0]]) #Matriz de observación.

#Varianza del proceso y de la medición.
Q = np.array([[0.1, 0], [0, 0.01]]) #Covarianza del proceso.
R = np.array([[0.5]]) #Covarianza de la medición.

#Condición inicial del estado.
x0 = np.array([[0], [0]]) #Estado inicial.
P0 = np.eye(2) #Covarianza inicial.

#Simulación del proceso verdadero.
T = 100 #Número de pasos de tiempo.
true_states = np.zeros((2, T))
true_states[:, 0] = x0.flatten()

for t in range(1, T):
    true_states[:, t] = np.dot(F, true_states[:, t-1]) + np.random.multivariate_normal([0, 0], Q)

observations = np.dot(H, true_states) + np.random.normal(0, R[0, 0], (1, T)) #Simulación de las observaciones.

x_pred = x0 #Filtro de Kalman.
P_pred = P0
filtered_states = np.zeros((2, T))

for t in range(T):
    x_pred = np.dot(F, x_pred) #Predicción.
    P_pred = np.dot(np.dot(F, P_pred), F.T) + Q
    
    y = observations[:, t] #Actualización.
    K = np.dot(np.dot(P_pred, H.T), np.linalg.inv(np.dot(np.dot(H, P_pred), H.T) + R))
    x_pred = x_pred + np.dot(K, y - np.dot(H, x_pred))
    P_pred = np.dot((np.eye(2) - np.dot(K, H)), P_pred)
    
    filtered_states[:, t] = x_pred.flatten()

plt.figure(figsize=(10, 6)) #Graficamos los resultados.
plt.plot(true_states[0], label='Estado Verdadero', color='blue')
plt.plot(observations.flatten(), label='Observaciones', color='green', marker='o', linestyle='None', markersize=5)
plt.plot(filtered_states[0], label='Estado Filtrado', color='red')
plt.title('Filtrado y Predicción con Filtro de Kalman') #Agregamos un titulo.
plt.xlabel('Tiempo') #Agregamos etiquetas al eje X y Y.
plt.ylabel('Estado')
plt.legend() #Agregamos una leyenda.
plt.grid(True) #Mostramos la cuadricula.
plt.show() #Mostramos el gráfico.