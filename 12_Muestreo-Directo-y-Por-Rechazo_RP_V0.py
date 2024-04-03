#Alejandra Rodriguez Guevara 21310127 6E1

#-> Muestreo Directo (Direct Sampling): se generan muestras directamente de la distribución de probabilidad deseada.

import numpy as np #Importamos las librerias necesarias.
import matplotlib.pyplot as plt

def target_distribution(x): #Función de densidad de probabilidad.
    return np.exp(-x ** 2 / 2) / np.sqrt(2 * np.pi) #Distribución normal estándar.

def direct_sampling(num_samples): #Muestreo directo.
    samples = np.random.normal(0, 1, num_samples) #Generamos muestras utilizando una distribución normal estándar.
    return samples

num_samples = 1000 #Número de muestras a generar.
samples = direct_sampling(num_samples) #Generamos muestras utilizando muestreo directo.

plt.hist(samples, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black') #Creamos un histograma de las muestras generadas.

x = np.linspace(-4, 4, 1000) #Graficamos la función de densidad de probabilidad objetivo.
plt.plot(x, target_distribution(x), 'r-', label='Distribución Objetivo')
plt.title('Muestreo Directo') #Le ponemos titulo a nuestra grafica.
plt.xlabel('Valor') #Le ponemos etiqueta al eje X y Y.
plt.ylabel('Densidad de Probabilidad')
plt.legend() #Ponemos una leyenda.
plt.grid(True) #Mostramos la cuadricula.
plt.show() #Mostramos nuestro gráfico.