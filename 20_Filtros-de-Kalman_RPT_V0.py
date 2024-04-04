#Alejandra Rodriguez Guevara 21310127 6E1

#Los Filtros de Kalman son algoritmos de estimación óptima utilizados para estimar el estado de un sistema dinámico a partir de una serie de mediciones ruidosas.
#El filtro de Kalman se basa en un modelo dinámico del sistema que describe cómo evoluciona el estado del sistema a lo largo del tiempo.

from filterpy.kalman import KalmanFilter #Importamos las librerias necesarias.
import numpy as np

kf = KalmanFilter(dim_x=2, dim_z=1) #Creamos un filtro de Kalman.

#Definimos la matriz de transición de estado (F).
dt = 0.1 #Intervalo de tiempo entre las mediciones.
kf.F = np.array([[1, dt],[0, 1]])

#Definimos la matriz de observación (H).
kf.H = np.array([[1, 0]])

#Definimos las covarianzas del proceso (Q) y de las mediciones (R).
kf.Q = np.diag([0.01, 0.01]) #Covarianza del proceso.
kf.R = np.diag([0.1]) #Covarianza de las mediciones.

#Definimos la covarianza inicial del estado y el estado inicial.
kf.P = np.eye(2) * 1000 #Covarianza inicial del estado.
kf.x = np.array([0, 0]) #Estado inicial.

#Realizamos la predicción y la actualización.
measurement = 1.2 #Nueva medición.
kf.predict()
kf.update(measurement)

state_estimate = kf.x #Obtenemos la estimación del estado.

print("Estimación del estado después de la actualización:", state_estimate) #Imprimimos los resultados.