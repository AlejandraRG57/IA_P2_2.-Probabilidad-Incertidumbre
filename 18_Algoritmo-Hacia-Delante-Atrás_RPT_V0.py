#Alejandra Rodriguez Guevara 21310127 6E1

#El algoritmo hacia adelante-atrás, también conocido como algoritmo de Baum-Welch se utiliza para 
#estimar los parámetros desconocidos de un HMM a partir de una secuencia de observaciones.

#El HMM es un modelo estadístico en el que se asume que las observaciones son generadas por un proceso estocástico no observable,
# y el objetivo es estimar los parámetros del modelo que maximizan la probabilidad de las observaciones dadas.

from hmmlearn import hmm #Importamos las librerias necesarias.
import numpy as np

np.random.seed(42) #Generamos datos simulados.
model = hmm.GaussianHMM(n_components=2, covariance_type="diag")
model.startprob_ = np.array([0.5, 0.5])
model.transmat_ = np.array([[0.7, 0.3],
                             [0.4, 0.6]])
model.means_ = np.array([[0.0], [3.0]])
model.covars_ = np.array([[1.0], [1.0]])

X, Z = model.sample(100)

hmm_model = hmm.GaussianHMM(n_components=2, covariance_type="diag", n_iter=100) #Inicializamos el modelo HMM.

hmm_model.fit(X) #Ajustamos el modelo usando el algoritmo hacia adelante-atrás.

#Mostramos los parámetros aprendidos.
print("Probabilidades iniciales:") 
print(hmm_model.startprob_)
print("Probabilidades de transición:")
print(hmm_model.transmat_)
print("Medias de los estados:")
print(hmm_model.means_)
print("Covarianzas de los estados:")
print(hmm_model.covars_)