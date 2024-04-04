#Alejandra Rodriguez Guevara 21310127 6E1

#Los Modelos de Markov Ocultos (HMM) son un tipo de modelo estadístico que se utiliza para modelar secuencias 
#son "ocultos" y solo pueden ser inferidos indirectamente a través de observaciones observables.

from hmmlearn import hmm #Importamos las librerias necesarias.
import numpy as np

#Definimos el modelo HMM.
model = hmm.GaussianHMM(n_components=2, covariance_type="full")

#Definimos los parámetros del modelo.
model.startprob_ = np.array([0.5, 0.5]) #Probabilidades iniciales de los estados ocultos.
model.transmat_ = np.array([[0.7, 0.3],[0.4, 0.6]]) #Probabilidades de transición entre estados ocultos.
model.means_ = np.array([[0.0, 0.0],[3.0, 3.0]]) #Medias de las distribuciones gaussianas para cada estado oculto.
model.covars_ = np.tile(np.identity(2), (2, 1, 1)) #Covarianzas de las distribuciones gaussianas.

#Generamos una secuencia de observaciones.
X, Z = model.sample(n_samples=100)

#Inferimos la secuencia de estados ocultos más probable.
hidden_states = model.predict(X)

#Imprimimos la secuencia de estados ocultos y las observaciones.
print("Secuencia de estados ocultos:")
print(hidden_states)
print("Secuencia de observaciones:")
print(X)