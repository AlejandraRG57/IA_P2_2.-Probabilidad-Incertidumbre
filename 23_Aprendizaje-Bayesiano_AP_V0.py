#Alejandra Rodriguez Guevara 21310127 6E1

#El Aprendizaje Bayesiano es un enfoque para el aprendizaje automático que utiliza la teoría de la probabilidad bayesiana para inferir 
#la distribución de probabilidad de los parámetros de un modelo dado, dadas las observaciones de los datos.

import numpy as np #Importamos las librerias necesarias.
import scipy.optimize as optimize
import matplotlib.pyplot as plt

#Generamos datos sintéticos.
np.random.seed(0)
x = np.random.uniform(0, 10, size=100)
true_slope = 2
true_intercept = 5
y = true_slope * x + true_intercept + np.random.normal(0, 1, size=100)

def linear_regression(params, x, y): #Definimos la función de regresión lineal.
    slope, intercept = params
    y_pred = slope * x + intercept
    return np.sum((y_pred - y) ** 2)

#Estimamos los parámetros del modelo utilizando máxima verosimilitud.
initial_guess = [0, 0] #Estimación inicial de los parámetros.
result = optimize.minimize(linear_regression, initial_guess, args=(x, y))
slope, intercept = result.x

#Visualizamos los datos y la línea de regresión.
plt.scatter(x, y, label='Datos')
plt.plot(x, slope * x + intercept, color='red', label='Regresión lineal')
plt.title('Regresión lineal simple (Aproximación de máxima verosimilitud)') #Agregamos un titulo.
plt.xlabel('x')#Agregamos etiquetas al eje X y Y.
plt.ylabel('y')
plt.legend() #Agregamos una leyenda.
plt.grid(True) #Mostramos la cuadricula.
plt.show() #Mostramos el gráfico.

#Imprimimos los parámetros del modelo.
print('Pendiente estimada (máxima verosimilitud):', slope)
print('Intersección estimada (máxima verosimilitud):', intercept)