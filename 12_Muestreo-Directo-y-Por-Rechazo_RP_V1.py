#Alejandra Rodriguez Guevara 21310127 6E1

#-> Muestreo por Rechazo (Rejection Sampling): se generan muestras de una distribución de probabilidad utilizando 
#una distribución de probabilidad auxiliar más simple de la cual se puede muestrear directamente.

import numpy as np #Importamos las librerias necesarias.
import matplotlib.pyplot as plt

def target_distribution(x): #Función de densidad de probabilidad objetivo.
    return np.exp(-x ** 2 / 2) / np.sqrt(2 * np.pi) #Distribución normal estándar.

def auxiliary_distribution(x): #Función de densidad de probabilidad auxiliar.
    return np.exp(-x ** 2 / 4) / np.sqrt(4 * np.pi) #Distribución normal con varianza 4.

def rejection_sampling(num_samples): #Muestreo por rechazo.
    samples = []
    max_auxiliary_distribution = auxiliary_distribution(0) #Máximo de la función auxiliar.
    while len(samples) < num_samples:
        x = np.random.normal(0, 2, 1) #Generamos una muestra de la distribución auxiliar.
        u = np.random.uniform(0, max_auxiliary_distribution) #Generamos una muestra uniforme entre 0 y el máximo de la función auxiliar.
        if u < target_distribution(x): #Aceptamos la muestra según el criterio de rechazo.
            samples.append(x)
    return np.array(samples).flatten()

num_samples = 1000 #Número de muestras a generar.
samples = rejection_sampling(num_samples) #Generamos muestras utilizando muestreo por rechazo.

plt.hist(samples, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black') #Creamos un histograma de las muestras generadas.

x = np.linspace(-4, 4, 1000) #Graficamos la función de densidad de probabilidad objetivo.
plt.plot(x, target_distribution(x), 'r-', label='Distribución Objetivo')
plt.title('Muestreo por Rechazo') #Le ponemos titulo a nuestra grafica.
plt.xlabel('Valor') #Le ponemos etiqueta al eje X y Y.
plt.ylabel('Densidad de Probabilidad')
plt.legend() #Ponemos una leyenda.
plt.grid(True) #Mostramos la cuadricula.
plt.show() #Mostramos nuestro gráfico.