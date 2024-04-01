#Alejandra Rodriguez Guevara 21310127 6E1

#El "Manto de Markov" es una forma informal de referirse a un modelo en cadena de Markov oculto (HMM, por sus siglas en inglés), 
#el cual es un modelo estadístico que describe una secuencia de eventos donde el estado actual depende solo del estado anterior 
#y no de todos los estados anteriores. Es "oculto" porque los estados no se observan directamente, sino que solo se observan las 
#variables observables que están condicionadas por los estados ocultos.

import numpy as np #Importamos la libreria necesaria.

class HiddenMarkovModel:
    def __init__(self, states, symbols, start_prob, transition_prob, emission_prob): #Inicializamos el modelo HMM con los parámetros necesarios.
        self.states = states #Lista de estados posibles.
        self.symbols = symbols #Lista de símbolos observables.
        self.start_prob = start_prob #Probabilidad inicial de los estados ocultos.
        self.transition_prob = transition_prob #Matriz de probabilidades de transición entre estados ocultos.
        self.emission_prob = emission_prob #Matriz de probabilidades de emisión de los símbolos observables.

    def forward(self, observations): #Algoritmo de adelante para calcular la probabilidad de observar una secuencia de símbolos.
        T = len(observations) #Longitud de la secuencia de observaciones.
        alpha = np.zeros((T, len(self.states))) #Inicializamos la matriz de variables alpha.

        for i, obs in enumerate(observations):
            if i == 0: 
                alpha[i, :] = self.start_prob * self.emission_prob[:, obs] #Inicializamos en el primer paso de tiempo.
            else:
                alpha[i, :] = np.sum(alpha[i-1, :] * self.transition_prob.T * self.emission_prob[:, obs], axis=1) # Cálculo recursivo de las variables alpha en los pasos de tiempo siguientes.
        return alpha

    def viterbi(self, observations): #Algoritmo de Viterbi para encontrar la secuencia de estados más probable dada una secuencia de observaciones.
        T = len(observations) #Longitud de la secuencia de observaciones.
        delta = np.zeros((T, len(self.states))) #Inicializamos la matriz de variables delta.
        psi = np.zeros((T, len(self.states)), dtype=int) #Inicializamos la matriz de índices psi.
        delta[0, :] = self.start_prob * self.emission_prob[:, observations[0]]

        for t in range(1, T):
            for j in range(len(self.states)): #Calculamos de las variables delta y psi en los pasos de tiempo siguientes.
                delta[t, j] = np.max(delta[t-1, :] * self.transition_prob[:, j]) * self.emission_prob[j, observations[t]]
                psi[t, j] = np.argmax(delta[t-1, :] * self.transition_prob[:, j])

        states = np.zeros(T, dtype=int)
        states[T-1] = np.argmax(delta[T-1, :])

        for t in range(T-2, -1, -1):
            #Recuperamos la secuencia de estados a partir de los índices psi.
            states[t] = psi[t+1, states[t+1]]
        return states

states = ['Sunny', 'Rainy'] #Estados posibles del clima.
symbols = ['Dry', 'Dryish', 'Soggy'] #Símbolos observables.
start_prob = np.array([0.5, 0.5]) #Probabilidad inicial de los estados ocultos.
transition_prob = np.array([[0.8, 0.2], [0.4, 0.6]]) #Probabilidad de transición entre estados ocultos.
emission_prob = np.array([[0.6, 0.2, 0.2], [0.1, 0.4, 0.5]]) #Probabilidad de emisión de los símbolos observables en cada estado oculto.

model = HiddenMarkovModel(states, symbols, start_prob, transition_prob, emission_prob) #Creamos el modelo HMM.
observations = [0, 1, 2] #Secuencia de observaciones.

alpha = model.forward(observations) #Calculamos la probabilidad de observar la secuencia de observaciones dado el modelo.
print("Probabilidad de observar la secuencia de observaciones:", alpha[-1].sum()) #Imprimimos resultado.

states_sequence = model.viterbi(observations) #Encontramos la secuencia de estados más probable dada la secuencia de observaciones.
print("Secuencia de estados más probable:", [model.states[state] for state in states_sequence]) #Imprimimos resultado.