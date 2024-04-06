#Alejandra Rodriguez Guevara 21310127 6E1

#-> Red de Hopfield: Las redes de Hopfield son redes neuronales artificiales con unidades binarias (neuronas) y conexiones ponderadas que forman una red completamente conectada. 
#Estas redes se utilizan para almacenar y recuperar patrones de entrada, y pueden converger hacia estados estables que representan los patrones almacenados.

import numpy as np #Importamos la libreria necesaria.

class HopfieldNetwork:
    def __init__(self, num_neurons):
        self.num_neurons = num_neurons #Inicializamos la red de Hopfield con el número de neuronas especificado.
        self.weights = np.zeros((num_neurons, num_neurons)) #Creamos una matriz de pesos inicialmente llena de ceros.

    def train(self, patterns): #Entrenamos la red de Hopfield con una lista de patrones de entrada.
        num_patterns = len(patterns)
        pattern_length = len(patterns[0])
        for pattern in patterns:
            if len(pattern) != pattern_length:
                raise ValueError("Todos los patrones deben tener la misma longitud")
        for pattern in patterns:
            pattern_row = np.array(pattern).reshape(-1, 1) #Convertimos el patrón en una matriz unidimensional.
            self.weights += np.dot(pattern_row, pattern_row.T) #Actualizamos los pesos de la red sumando el producto externo del patrón con su transpuesta.
        np.fill_diagonal(self.weights, 0) #Aseguramos que los pesos diagonales sean cero.

    def recall(self, pattern, max_iterations=100):
        pattern = np.array(pattern).reshape(-1, 1) #Convertimos el patrón en un vector columna.
        for _ in range(max_iterations):
            new_pattern = np.sign(np.dot(self.weights, pattern)) #Calculamos el nuevo patrón utilizando la fórmula de actualización de Hopfield.
            if np.array_equal(new_pattern, pattern):
                return new_pattern.flatten() #Devolvemos el nuevo patrón como un vector plano.
            pattern = new_pattern #Si no se ha convergido, se actualiza el patrón para la próxima iteración.
        return pattern.flatten() #Si no se logra la convergencia dentro del número máximo de iteraciones, se devuelve el patrón actual.

patterns = [
    [1, 1, -1, -1],
    [-1, -1, 1, 1],
    [1, -1, 1, -1]
]

hopfield_net = HopfieldNetwork(len(patterns[0])) #Creamos una instancia de la red de Hopfield.
hopfield_net.train(patterns) #Entrenamos la red con los patrones de entrada.

test_pattern = [1, -1, 1, -1] #Patrón de prueba.
recovered_pattern = hopfield_net.recall(test_pattern)
print("Patrón original:", test_pattern) #Imprimimos los resultados.
print("Patrón recuperado:", recovered_pattern)
