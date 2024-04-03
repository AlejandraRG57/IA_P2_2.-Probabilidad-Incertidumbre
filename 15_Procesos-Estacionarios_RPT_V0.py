#Alejandra Rodriguez Guevara 21310127 6E1

#Un proceso estacionario es un tipo de proceso aleatorio en el cual las propiedades estadísticas del proceso no cambian con el tiempo. 

import numpy as np #Importamos las librerias necesarias.
import matplotlib.pyplot as plt

def simular_AR1_estacionario(n, phi, sigma): #Función para simular un proceso AR(1) estacionario.
    x = [0] #Inicializamos el proceso con una condición inicial arbitraria.
    
    for _ in range(n): #Generamos muestras del proceso.
        nuevo_valor = phi * x[-1] + np.random.normal(0, sigma)
        x.append(nuevo_valor)
    
    return x[1:] #Excluimos el primer valor, que es la condición inicial.

n = 1000 #Número de muestras.
phi = 0.9 #Parámetro de autoregresión.
sigma = 1 #Desviación estándar del ruido.

datos = simular_AR1_estacionario(n, phi, sigma) #Simulamos el proceso AR(1) estacionario.

plt.plot(datos) #Graficamos los datos generados.
plt.title('Proceso AR(1) Estacionario') #Le ponemos un titulo al grafico.
plt.xlabel('Tiempo') #Etiquetamos el eje X y Y.
plt.ylabel('Valor')
plt.grid(True) #Le ponemos cuadricula al grafico.
plt.show() #Mostramos el grafico.