#Alejandra Rodriguez Guevara 21310127 6E1

#La inferencia por enumeración es un método utilizado en redes Bayesianas para calcular la distribución de probabilidad conjunta de un conjunto de variables ocultas y observadas. 
#Consiste en enumerar todas las posibles combinaciones de valores de las variables ocultas y calcular la probabilidad conjunta de las variables observadas dados estos valores de 
#las variables ocultas. 

import itertools #Importamos la libreria necesaria.

class BayesianNetwork:
    def __init__(self): #Definimos las probabilidades condicionales.
        self.probabilities = {
            ('Soleado', 'Llevar Paraguas'): {'Sí': 0.1, 'No': 0.9},
            ('Nublado', 'Llevar Paraguas'): {'Sí': 0.3, 'No': 0.7},
            ('Lluvioso', 'Llevar Paraguas'): {'Sí': 0.8, 'No': 0.2},
            'Clima': {'Soleado': 0.6, 'Nublado': 0.2, 'Lluvioso': 0.2}
        }
    
    def joint_probability(self, evidence): #Calculamos la probabilidad conjunta dada la evidencia.
        probability = 1.0
        for variable, value in evidence.items():
            if variable in self.probabilities:
                if isinstance(value, str):
                    probability *= self.probabilities[variable][value]
                else:
                    probability *= self.probabilities[variable]
        return probability

def enumeration_inference(network, evidence): 
    joint_distribution = {} #Inicializamos la distribución de probabilidad conjunta.
    hidden_variables = ['Clima'] #Enumeramos todas las posibles combinaciones de valores de las variables ocultas.
    hidden_values = ['Soleado', 'Nublado', 'Lluvioso']
    hidden_combinations = itertools.product(*[hidden_values])
    
    for hidden_combination in hidden_combinations: #Calculamos la probabilidad conjunta para cada combinación de valores de las variables ocultas.
        updated_evidence = evidence.copy() #Actualizamos la evidencia con la combinación de valores de las variables ocultas.
        updated_evidence['Clima'] = hidden_combination[0]
        joint_prob = network.joint_probability(updated_evidence) #Calculamos la probabilidad conjunta dadas las variables ocultas.
        joint_distribution[hidden_combination] = joint_prob
    return joint_distribution

network = BayesianNetwork() #Creamos una instancia de la red bayesiana.
evidence = {'Llevar Paraguas': 'Sí'} #Definimos la evidencia.
joint_distribution = enumeration_inference(network, evidence) #Realizamos inferencia por enumeración para calcular la distribución de probabilidad conjunta.

for combination, probability in joint_distribution.items(): #Imprimimos la distribución de probabilidad conjunta calculada.
    print(f"Probabilidad para {combination}: {probability}")