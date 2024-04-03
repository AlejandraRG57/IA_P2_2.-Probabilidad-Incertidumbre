#Alejandra Rodriguez Guevara 21310127 6E1

#La eliminación de variables es un método de inferencia utilizado en redes bayesianas para calcular la distribución de probabilidad de un conjunto de variables 
#eliminando variables ocultas. Este método es útil cuando se desea calcular la probabilidad de un conjunto de variables observadas dado un conjunto de evidencia.

class BayesianNetwork:
    def __init__(self): #Definimos las probabilidades condicionales.
        self.probabilities = {
            ('Soleado', 'Llevar Paraguas'): {'Sí': 0.0, 'No': 0.9},
            ('Nublado', 'Llevar Paraguas'): {'Sí': 0.5, 'No': 0.5},
            ('Lluvioso', 'Llevar Paraguas'): {'Sí': 0.9, 'No': 0.1},
            'Clima': {'Soleado': 0.6, 'Nublado': 0.3, 'Lluvioso': 0.2}
        }
    
    def joint_probability(self, evidence):
        #Calculamos la probabilidad conjunta dada la evidencia.
        probability = 1.0
        for variable, value in evidence.items():
            if variable in self.probabilities:
                if isinstance(value, str):
                    probability *= self.probabilities[variable][value]
                else:
                    probability *= self.probabilities[variable]
        return probability
    
    def get_hidden_variables(self):
        return ['Clima'] #Obtenemos las variables ocultas de la red bayesiana.

    def eliminate_variables(self, variables_to_eliminate):
        reduced_network = BayesianNetwork() #Reducimos la red bayesiana eliminando variables ocultas.
        return reduced_network

def variable_elimination(network, query_variables, evidence):
    joint_distribution = {} #Inicializamos la distribución de probabilidad conjunta.
    
    for query_variable in query_variables: #Iteramos sobre las variables a consultar.
        variables_to_eliminate = set(network.get_hidden_variables()) - set([query_variable]) #Eliminamos las variables ocultas.
        reduced_network = network.eliminate_variables(variables_to_eliminate)
        marginal_probability = reduced_network.joint_probability(evidence) #Calculamos la probabilidad marginal de la variable consultada dada la evidencia.
        joint_distribution[query_variable] = marginal_probability
    return joint_distribution

network = BayesianNetwork() #Creamos una instancia de la red bayesiana.
evidence = {'Llevar Paraguas': 'Sí'} #Definimos la evidencia.
query_variables = ['Clima'] #Definimos las variables a consultar.
joint_distribution = variable_elimination(network, query_variables, evidence) #Realizamos eliminación de variables para calcular la distribución de probabilidad marginal.

for variable, probability in joint_distribution.items(): #Imprimimos la distribución de probabilidad marginal calculada.
    print(f"Probabilidad para {variable}: {probability}")