#Alejandra Rodriguez Guevara 21310127 6E1

#El método de Monte Carlo para cadenas de Markov (MCMC, por sus siglas en inglés) es una técnica de simulación estadística 
#que se utiliza para generar muestras de una distribución de probabilidad dada. 

import numpy as np #Importamos la libreria necesaria.

def target_distribution(x): #Función que define la distribución de probabilidad objetivo.
    probabilities = [0.2, 0.4, 0.3, 0.1] #Probabilidades de cada posible valor.
    return probabilities[x]

def metropolis_hastings(num_samples): #Algoritmo de Metropolis-Hastings para generar muestras de la distribución objetivo.
    current_state = np.random.randint(0, 4) #Empezamos desde un punto arbitrario.
    samples = [current_state]

    for _ in range(num_samples):
        proposed_state = np.random.randint(0, 4) #Generamos una nueva propuesta de estado aleatorio.
        acceptance_ratio = min(1, target_distribution(proposed_state) / target_distribution(current_state)) #Calculamos la razón de aceptación.
        
        if np.random.uniform(0, 1) < acceptance_ratio: #Aceptamos el nuevo estado con una probabilidad igual a la razón de aceptación.
            current_state = proposed_state
        samples.append(current_state)

    return samples

num_samples = 10000 #Generamos muestras utilizando el algoritmo de Metropolis-Hastings.
samples = metropolis_hastings(num_samples)

unique, counts = np.unique(samples, return_counts=True) #Imprimimos algunas estadísticas sobre las muestras generadas.
for value, count in zip(unique, counts):
    print(f"Valor: {value}, Frecuencia: {count/num_samples}")