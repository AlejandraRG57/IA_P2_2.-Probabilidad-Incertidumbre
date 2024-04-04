#Alejandra Rodriguez Guevara 21310127 6E1

#Los Modelos Ocultos de Markov (HMM, por sus siglas en inglés) son modelos estadísticos utilizados para modelar secuencias de datos con una estructura temporal subyacente.

#Un HMM consta de tres componentes principales:
# -Estados Ocultos: Representan el proceso estocástico subyacente que no es directamente observable.
# -Observaciones: Son los datos que se observan directamente.
# -Modelo de Transición: Especifica las probabilidades de transición entre los estados ocultos. 

from hmmlearn import hmm #Importamos las librerias necesarias.
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42) #Datos simulados.
X = np.concatenate([np.random.normal(0, 1, 100), np.random.normal(3, 1, 100)]).reshape(-1, 1)

model = hmm.GaussianHMM(n_components=2, covariance_type="diag", n_iter=100) #Creamos y ajustamos el modelo HMM.
model.fit(X)

n_samples = 100 #Generamos nuevas observaciones usando el modelo HMM.
samples, _ = model.sample(n_samples)

#Graficamos los datos originales y las nuevas observaciones generadas por el HMM.
plt.figure(figsize=(10, 6))
plt.plot(X, label='Datos Originales', color='blue')
plt.plot(range(len(X), len(X) + n_samples), samples, label='Nuevas Observaciones', color='orange')
plt.title('Datos Originales vs. Nuevas Observaciones Generadas por el HMM') #Agregamos un titulo.
plt.xlabel('Tiempo') #Agregamos etiquetas al eje X y Y.
plt.ylabel('Observaciones')
plt.legend() #Agregamos una leyenda.
plt.grid(True) #Mostramos la cuadricula.
plt.show() #Mostramos el gráfico.