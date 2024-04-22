#Alejandra Rodriguez Guevara 21310127 6E1

#El filtro de partículas de Monte Carlo es altamente robusto y puede manejar de manera efectiva la incertidumbre en la localización del robot, 
#así como los problemas de no linealidad en los modelos de movimiento y sensores.

import numpy as np

def localizacion_mcl(iteraciones, num_particulas):
    #Inicializamos las partículas y sus pesos.
    particulas = np.random.rand(num_particulas, 2) * 100  #Coordenadas aleatorias en un espacio de 100x100.
    pesos = np.ones(num_particulas) / num_particulas  #Inicialmente, todas las partículas tienen el mismo peso.

    #Simulación de la localización.
    for i in range(iteraciones):
        #Predecimos el movimiento de las partículas.
        movimiento_x = np.random.normal(0, 1, num_particulas)  #Movimiento aleatorio en el eje x.
        movimiento_y = np.random.normal(0, 1, num_particulas)  #Movimiento aleatorio en el eje y.
        particulas[:, 0] += movimiento_x
        particulas[:, 1] += movimiento_y

        #Actualización de los pesos basada en la observación (simulamos la observación de un sensor).
        pesos = np.ones(num_particulas) / num_particulas

        #Re-muestreo de las partículas.
        particulas_indices = np.arange(num_particulas)
        particulas_indices = np.random.choice(particulas_indices, size=num_particulas, replace=True, p=pesos)
        particulas = particulas[particulas_indices]

    return particulas

#Parámetros de la simulación.
iteraciones = 100
num_particulas = 100

#Simulamos de la localización.
particulas_finales = localizacion_mcl(iteraciones, num_particulas)

#Visualizamos de las partículas finales.
print("Partículas finales:")
print(particulas_finales)