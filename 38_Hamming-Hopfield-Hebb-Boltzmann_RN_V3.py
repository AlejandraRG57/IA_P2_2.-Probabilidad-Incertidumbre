#Alejandra Rodriguez Guevara 21310127 6E1

#-> Máquina de Boltzmann: La máquina de Boltzmann es una red neuronal de tipo energético, que tiene unidades (neuronas) binarias o continuas y conexiones ponderadas. 
#Estas redes se utilizan para modelar distribuciones de probabilidad sobre conjuntos de variables. El aprendizaje en una máquina de Boltzmann se realiza mediante 
#métodos de aprendizaje no supervisado basados en el muestreo estocástico.

import numpy as np #Importamos la libreria necesaria.

class BoltzmannMachine:
    def __init__(self, n_visible, n_hidden):
        #Inicializamos la máquina de Boltzmann con el número de neuronas visibles y ocultas.
        self.n_visible = n_visible
        self.n_hidden = n_hidden
        #Inicializamos aleatoriamente los pesos y sesgos.
        self.weights = np.random.randn(n_visible, n_hidden)
        self.bias_visible = np.random.randn(n_visible)
        self.bias_hidden = np.random.randn(n_hidden)
        
    def sigmoid(self, x): #Función de activación sigmoide.
        return 1 / (1 + np.exp(-x))
    
    def gibbs_sampling(self, visible_input): #Muestreo de Gibbs para obtener una muestra de la red.
        hidden_prob = self.sigmoid(np.dot(visible_input, self.weights) + self.bias_hidden)
        hidden_sample = np.random.binomial(1, hidden_prob)
        visible_prob = self.sigmoid(np.dot(hidden_sample, self.weights.T) + self.bias_visible)
        visible_sample = np.random.binomial(1, visible_prob)
        return visible_sample, hidden_sample
    
    def train(self, data, learning_rate=0.1, epochs=100): #Entrenamos la máquina de Boltzmann utilizando el algoritmo de muestreo de Gibbs.
        for epoch in range(epochs):
            for sample in data:
                v0 = sample
                v1, h1 = self.gibbs_sampling(v0)
                #Actualizamos los pesos y sesgos de acuerdo con el algoritmo de aprendizaje de Boltzmann.
                self.weights += learning_rate * (np.outer(v0, h1) - np.outer(v1, h1))
                self.bias_visible += learning_rate * (v0 - v1)
                self.bias_hidden += learning_rate * (np.mean(v0) - np.mean(v1))

data = np.array([[0, 1, 1, 0],
                 [1, 1, 0, 0],
                 [0, 0, 0, 1],
                 [1, 0, 0, 1]])

bm = BoltzmannMachine(n_visible=4, n_hidden=2)
bm.train(data)

#Generamos las muestras.
for _ in range(5):
    visible_sample, _ = bm.gibbs_sampling(np.array([0, 0, 0, 0]))
    print("Muestra generada:", visible_sample)