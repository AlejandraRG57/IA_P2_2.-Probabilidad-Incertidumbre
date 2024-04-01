#Alejandra Rodriguez Guevara 21310127 6E1

#Una Red Bayesiana es un modelo gráfico probabilístico que representa las relaciones de dependencia condicional entre un conjunto de variables aleatorias.

from pgmpy.models import BayesianNetwork #Importamos las librerias necesarias.
from pgmpy.factors.discrete import TabularCPD
import networkx as nx
import matplotlib.pyplot as plt

model = BayesianNetwork([('Tiempo', 'Llevar_paraguas'), ('Tiempo', 'Estar_mojado')]) #Creamos una instancia del modelo bayesiano.

#Definimos las distribuciones de probabilidad condicional (CPDs).
cpd_tiempo = TabularCPD(variable='Tiempo', variable_card=3, values=[[0.4], [0.3], [0.3]], 
                         state_names={'Tiempo': ['Soleado', 'Nublado', 'Lluvioso']})

cpd_llevar_paraguas = TabularCPD(variable='Llevar_paraguas', variable_card=2,
                                  values=[[0.9, 0.6, 0.1],
                                          [0.1, 0.4, 0.9]],
                                  evidence=['Tiempo'], evidence_card=[3],
                                  state_names={'Llevar_paraguas': ['No', 'Si'],
                                               'Tiempo': ['Soleado', 'Nublado', 'Lluvioso']})

cpd_estar_mojado = TabularCPD(variable='Estar_mojado', variable_card=2,
                               values=[[0.9, 0.2, 0.1],
                                       [0.1, 0.8, 0.9]],
                               evidence=['Tiempo'], evidence_card=[3],
                               state_names={'Estar_mojado': ['No', 'Si'],
                                            'Tiempo': ['Soleado', 'Nublado', 'Lluvioso']})


model.add_cpds(cpd_tiempo, cpd_llevar_paraguas, cpd_estar_mojado) #AñadiMOS las CPDs al modelo.
print("¿El modelo es válido?", model.check_model()) #Verificamos si el modelo es válido.
pos = {'Tiempo': (0, 1), 'Llevar_paraguas': (1, 2), 'Estar_mojado': (2, 1)} #Dibujamos el modelo.
nx.draw(model, pos=pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold")
plt.title("Red Bayesiana") #Le ponemos un titulo al modelo.
plt.show() #Mostramos al usuario el modelo.