#Alejandra Rodriguez Guevara 21310127 6E1

#La hipótesis de Markov establece que la evolución futura de un sistema (o proceso) depende únicamente de su estado presente y no de su historia pasada. 
#En otras palabras, dado el estado actual de un sistema, la probabilidad de transición a un estado futuro específico depende únicamente de ese estado actual 
#y no de cómo se llegó a ese estado.

import numpy as np #Importamos la libreria necesaria.

estados = ['Soleado', 'Nublado', 'Lluvioso'] #Definimos los estados posibles y la matriz de transición.
matriz_transicion = np.array([
    [0.6, 0.2, 0.2],  #Probabilidades de transición desde 'Soleado'.
    [0.3, 0.5, 0.2],  #Probabilidades de transición desde 'Nublado'.
    [0.2, 0.3, 0.5]   #Probabilidades de transición desde 'Lluvioso'.
])

def simular_cadena_markov(n, estado_inicial): #Función para simular una cadena de Markov.
    cadena = [estado_inicial]
    estado_actual = estado_inicial

    for _ in range(n-1):
        index_estado_actual = estados.index(estado_actual) #Obtenemos las probabilidades de transición para el estado actual.
        probabilidades = matriz_transicion[index_estado_actual]
        estado_siguiente = np.random.choice(estados, p=probabilidades) #Elegimos el próximo estado según las probabilidades de transición.
        cadena.append(estado_siguiente) #Agregamos el estado siguiente a la cadena.
        estado_actual = estado_siguiente #Actualizamos el estado actual.
    return cadena

cadena_simulada = simular_cadena_markov(10, 'Soleado') #Simulamos una cadena de Markov con un estado inicial 'Soleado' y longitud 10.
print("Cadena de Markov simulada:", cadena_simulada)