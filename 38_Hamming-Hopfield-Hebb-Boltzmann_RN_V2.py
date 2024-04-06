#Alejandra Rodriguez Guevara 21310127 6E1

#-> Regla de Hebb: La regla de Hebb es un principio en neurociencia que afirma que las sinapsis entre neuronas se 
#fortalecen si las neuronas asociadas activadas repetidamente se activan simultáneamente.

import numpy as np #Importamos la libreria necesaria.

class HebbRule:
    def __init__(self, n_inputs):
        self.n_inputs = n_inputs
        self.weights = np.zeros((n_inputs, n_inputs))  #Inicializamos como una matriz de ceros.

    def train(self, inputs): #Método para entrenar la red Hopfield.
        for input_vector in inputs: #Iteramos sobre cada vector de entrada en la lista de patrones.
            self.weights += np.outer(input_vector, input_vector) #Calculamos el producto externo del vector de entrada consigo mismo y lo sumamos a los pesos.

    def predict(self, input_vector): #Método para predecir un patrón dado un vector de entrada.
        return np.sign(np.dot(input_vector, self.weights)) #Multiplicamos el vector de entrada por los pesos y aplicamos la función de activación signo.

if __name__ == "__main__":
    inputs = np.array([[1, 1, -1], #Definimos la entrada y la salida esperada.
                       [-1, -1, -1],
                       [-1, 1, 1]])
    
    hebb_rule = HebbRule(n_inputs=3) #Creamos una instancia de la regla de Hebb.
    hebb_rule.train(inputs) #Entrenamos la regla de Hebb con los datos de entrada.
    test_input = np.array([1, -1, -1]) #Patrón de prueba.
    predicted_output = hebb_rule.predict(test_input) #Predecimos la salida utilizando la regla de Hebb.

    print("Salida predicha:", predicted_output) #Imprimimos resultados.