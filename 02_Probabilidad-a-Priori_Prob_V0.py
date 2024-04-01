#Alejandra Rodriguez Guevara 21310127 6E1

#La probabilidad a priori en grafos se refiere a la asignación de probabilidades a los eventos antes de observar cualquier evidencia o datos adicionales.

import numpy as np #Importamos la libreria necesaria.

class GrafoProbab:
    def __init__(self, matriz_probab):
        self.matriz_probab = matriz_probab #Inicializamos la matriz de probabilidades de transición del grafo.

    def transicion_probab(self, estado_actual): #Seleccionamos aleatoriamente el próximo estado basado en la probabilidad de transición desde el estado actual.
        return np.random.choice(len(self.matriz_probab), p=self.matriz_probab[estado_actual]) #Retornamos el próximo estado seleccionado aleatoriamente según la probabilidad de transición desde el estado actual.

matriz_probab = np.array([ #Definimos la matriz de transición con probabilidades a priori.
    [0.7, 0.2, 0.1],  #Probabilidades de transición desde el estado A "0".
    [0.3, 0.4, 0.3],  #Probabilidades de transición desde el estado B "1".
    [0.2, 0.5, 0.3]   #Probabilidades de transición desde el estado C "2".
])

grafo_probab = GrafoProbab(matriz_probab) #Creamos el grafo probabilístico.

estado_actual = 0  #Estado inicial.

for _ in range(10): #Realizamos las transiciones
    print("Estado actual:", estado_actual)
    estado_actual = grafo_probab.transicion_probab(estado_actual)