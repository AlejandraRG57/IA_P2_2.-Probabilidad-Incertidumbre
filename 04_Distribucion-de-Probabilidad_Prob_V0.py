#Alejandra Rodriguez Guevara 21310127 6E1

#Una distribución de probabilidad es una función que describe las posibles probabilidades de ocurrencia de diferentes resultados en un experimento o fenómeno aleatorio.

import numpy as np #Importamos las librerias necesarias
import matplotlib.pyplot as plt

#Definimos los posibles resultados de lanzar dos dados y sus probabilidades.
resultados = np.arange(2, 13)  #Resultados posibles: suma de dos dados del 2 al 12.
probabilidades = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) / 36 #Probabilidades de cada resultado
muestras = np.random.choice(resultados, size=1000, p=probabilidades) #Generamos muestras de la distribución de probabilidad.

#Visualizamos la distribución de probabilidad
plt.hist(muestras, bins=np.arange(1.5, 13.5, 1), density=True, alpha=0.75, edgecolor='black') #Creamos un histograma que visualiza la distribución de probabilidad de las muestras generadas.
plt.xticks(resultados) #Mostramos los resultados en el histograma generado.
plt.title('Distribución de Probabilidad de la Suma de Dos Dados') #Le ponemos titulo a nuestro histograma.
plt.xlabel('Suma de los Dados') #Etiquetamos el eje X y Y del histograma.
plt.ylabel('Probabilidad')
plt.grid(True) #Mostramos las lineas de la cuadricula
plt.show() #Mostramos nuesto histograma al usuario.