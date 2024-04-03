#Alejandra Rodriguez Guevara 21310127 6E1

#La ponderación de verosimilitud (likelihood weighting) es un método utilizado en inferencia probabilística 
#para estimar la probabilidad de un evento dado un conjunto de evidencia observada.

import numpy as np #Importamos la libreria necesaria.

def weighted_likelihood(estimations, variances):
    weights = 1 / np.array(variances) #Calculamos los pesos basados en las varianzas inversas.
    total_weight = np.sum(weights) #Calculamos la suma de los pesos.
    weighted_estimator = np.sum(weights * np.array(estimations)) / total_weight #Calculamos el estimador ponderado como la suma ponderada de las estimaciones.
    return weighted_estimator

estimations = [10, 12, 15] #Estimaciones de un parámetro.
variances = [1, 2, 3] #Varianzas asociadas a las estimaciones.

weighted_estimator = weighted_likelihood(estimations, variances) #Calculamos el estimador ponderado.
print("Estimador ponderado:", weighted_estimator) #Imprimimos resultado: