#Alejandra Rodriguez Guevara 21310127 6E1

#En el contexto de la robótica y la inteligencia artificial, la incertidumbre se refiere a la falta de conocimiento completo o 
#precisión en los datos, modelos o resultados de un sistema.

import numpy as np
import matplotlib.pyplot as plt

#Función de actualización de la posición del robot (modelo de movimiento).
def update_robot_position(x, y, dt, velocity, heading):
    new_x = x + velocity * np.cos(heading) * dt
    new_y = y + velocity * np.sin(heading) * dt
    return new_x, new_y

#Función de medición de la posición del robot (modelo de observación).
def measure_robot_position(x_true, y_true, std_dev):
    x_meas = np.random.normal(x_true, std_dev)
    y_meas = np.random.normal(y_true, std_dev)
    return x_meas, y_meas

#Función para la propagación del filtro de Kalman extendido (EKF).
def ekf_predict(x, P, dt, velocity, heading, Q):
    F = np.array([[1, 0, -velocity * np.sin(heading) * dt],
                  [0, 1, velocity * np.cos(heading) * dt],
                  [0, 0, 1]])
    x_pred = np.dot(F, x)
    P_pred = np.dot(F, np.dot(P, F.T)) + Q
    return x_pred, P_pred

#Función para la actualización del filtro de Kalman extendido (EKF).
def ekf_update(x_pred, P_pred, z, R):
    H = np.array([[1, 0, 0],
                  [0, 1, 0]])
    y = z - np.dot(H, x_pred)
    S = np.dot(H, np.dot(P_pred, H.T)) + R
    K = np.dot(P_pred, np.dot(H.T, np.linalg.inv(S)))
    x_new = x_pred + np.dot(K, y)
    P_new = P_pred - np.dot(K, np.dot(S, K.T))
    return x_new, P_new

#Parámetros del robot y del entorno.
dt = 0.1 #Intervalo de tiempo (s).
velocity = 1.0 #Velocidad del robot (m/s).
heading = np.pi / 4 #Dirección del movimiento del robot (rad).
std_dev_meas = 0.5 #Desviación estándar de la medición de posición.
std_dev_process = 0.1 #Desviación estándar del proceso de movimiento.
Q = np.diag([std_dev_process**2, std_dev_process**2, 0.1**2])  #Matriz de covarianza del proceso.
R = np.diag([std_dev_meas**2, std_dev_meas**2])  #Matriz de covarianza de la medición.

#Condiciones iniciales del robot.
x_true = 0.0  #Posición inicial en x (m).
y_true = 0.0  #Posición inicial en y (m).
x_est = np.array([0.0, 0.0, velocity * np.cos(heading)])  #Estado inicial estimado (posición y velocidad).
P_est = np.diag([1, 1, 0.1])  #Matriz de covarianza inicial estimada.

#Trayectoria del robot.
x_true_history = [x_true]
y_true_history = [y_true]
x_est_history = [x_est[0]]
y_est_history = [x_est[1]]

#Simulamos la navegación del robot.
for t in np.arange(0, 10, dt):
    #Movimiento del robot (modelo de movimiento).
    x_true, y_true = update_robot_position(x_true, y_true, dt, velocity, heading)
    
    #Medimos la posición del robot (modelo de observación).
    x_meas, y_meas = measure_robot_position(x_true, y_true, std_dev_meas)
    
    #Predecimos el filtro de Kalman extendido (EKF).
    x_est, P_est = ekf_predict(x_est, P_est, dt, velocity, heading, Q)
    
    #Actualizamos el filtro de Kalman extendido (EKF) con la medición.
    x_est, P_est = ekf_update(x_est, P_est, np.array([x_meas, y_meas]), R)
    
    #Guardamos la trayectoria del robot.
    x_true_history.append(x_true)
    y_true_history.append(y_true)
    x_est_history.append(x_est[0])
    y_est_history.append(x_est[1])

#Visualizamos la trayectoria del robot.
plt.figure(figsize=(10, 6))
plt.plot(x_true_history, y_true_history, label='Posición Verdadera', color='b', linestyle='--')
plt.plot(x_est_history, y_est_history, label='Posición Estimada (EKF)', color='r')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.title('Navegación del Robot')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()