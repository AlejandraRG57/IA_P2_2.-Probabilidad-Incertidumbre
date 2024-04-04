#Alejandra Rodriguez Guevara 21310127 6E1

#El algoritmo de Expectation-Maximization (EM) es un método iterativo utilizado para encontrar estimaciones de los parámetros 
#de un modelo estadístico cuando los datos observados están incompletos o contienen variables latentes no observadas. 

from sklearn.mixture import GaussianMixture #Importamos las librerias necesarias.
import numpy as np

#Generamos datos sintéticos.
np.random.seed(0)
X = np.concatenate([np.random.normal(0, 1, 1000), np.random.normal(4, 1, 1000)]).reshape(-1, 1)

#Ajustamos un modelo de mezcla gaussiana utilizando EM.
gmm = GaussianMixture(n_components=2)
gmm.fit(X)

#Obtenemos las medias y varianzas de los componentes.
means = gmm.means_
covariances = gmm.covariances_

#Imprimimos los resultados recabados.
print("Medias de las componentes:", means)
print("Varianzas de las componentes:", covariances)