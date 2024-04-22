#Alejandra Rodriguez Guevara 21310127 6E1

#La dinámica y el control son dos aspectos fundamentales en la robótica que se ocupan del movimiento y el comportamiento de los robots.

import numpy as np
import matplotlib.pyplot as plt

#Parámetros del sistema.
M = 1.0  #Masa del carro (kg).
m = 0.1  #Masa del péndulo (kg).
L = 1.0  #Longitud del péndulo (m).
g = 9.8  # aceleración debida a la gravedad (m/s^2).

#Función de dinámica del sistema.
def pendulum_dynamics(state, u):
    x, theta, dx, dtheta = state
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    ddx = (u + m * L * dtheta**2 * sin_theta) / (M + m - m * cos_theta**2)
    ddtheta = (-u * cos_theta - m * L * dtheta**2 * cos_theta * sin_theta - (M + m) * g * sin_theta) / (L * (M + m - m * cos_theta**2))
    return np.array([dx, dtheta, ddx, ddtheta])

#Controlador PID.
def pid_controller(state, target_theta, Kp, Ki, Kd, prev_error, integral):
    theta = state[1]
    error = target_theta - theta
    integral += error
    derivative = error - prev_error
    prev_error = error
    u = Kp * error + Ki * integral + Kd * derivative
    return u, prev_error, integral

#Simulación del sistema con control PID.
def simulate_pid_control(target_theta, Kp, Ki, Kd, dt, duration):
    state = np.array([0, np.pi, 0, 0])  #Estado inicial [x, theta, dx, dtheta].
    prev_error = 0
    integral = 0
    time = np.arange(0, duration, dt)
    states = np.zeros((len(time), len(state)))
    controls = np.zeros(len(time))
    for i, t in enumerate(time):
        u, prev_error, integral = pid_controller(state, target_theta, Kp, Ki, Kd, prev_error, integral)
        states[i] = state
        controls[i] = u
        state += pendulum_dynamics(state, u) * dt
    return time, states, controls

#Parámetros del controlador PID.
Kp = 100  #Ganancia proporcional.
Ki = 10   #Ganancia integral.
Kd = 5    #Ganancia derivativa.

#Parámetros de simulación.
dt = 0.01  #Intervalo de tiempo (s).
duration = 5  #Duración de la simulación (s).

#Simulamos el sistema con control PID.
target_theta = 0  #Angulo deseado del péndulo (rad).
time, states, controls = simulate_pid_control(target_theta, Kp, Ki, Kd, dt, duration)

#Visualizamos los resultados.
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, states[:, 1], label='Ángulo del péndulo')
plt.plot(time, np.ones_like(time) * target_theta, '--', label='Ángulo deseado')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ángulo (rad)')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time, controls, label='Control de entrada')
plt.xlabel('Tiempo (s)')
plt.ylabel('Fuerza de control (N)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()