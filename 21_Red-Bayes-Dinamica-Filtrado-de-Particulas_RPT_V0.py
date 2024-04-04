#Alejandra Rodriguez Guevara 21310127 6E1

#El filtrado de partículas, también conocido como filtro de Monte Carlo, es una técnica utilizada en estadística bayesiana 
#y en sistemas de estimación para estimar el estado de un sistema dinámico basándose en observaciones.

from filterpy.monte_carlo import systematic_resample #Importamos las librerias necesarias.
import numpy as np

def particle_filter(particles, weights, z, motion_model, measurement_model):
    #Predicción.
    particles = motion_model(particles)

    #Actualización.
    likelihoods = measurement_model(z, particles)
    weights *= likelihoods
    weights += 1.e-300
    weights /= sum(weights)
    
    #Remuestreo.
    indexes = systematic_resample(weights)
    particles[:] = particles[indexes]
    weights.fill(1.0 / len(weights))
    
    return particles


def motion_model(particles): #Modelo de movimiento simple.
    return particles + np.random.randn(len(particles)) * 0.1 #Agregamos ruido gaussiano.

def measurement_model(z, particles): #Modelo de medición simple
    return np.exp(-0.5 * ((particles - z) / 0.1) ** 2) / (np.sqrt(2 * np.pi) * 0.1) #Calculamos la probabilidad de observar z en cada partícula

#Configuración inicial.
np.random.seed(42)
num_particles = 1000
particles = np.random.randn(num_particles)
weights = np.ones(num_particles) / num_particles

#Secuencia de observaciones.
observations = np.random.randn(10)

for z in observations: #Ejecutamos el filtro de partículas
    particles = particle_filter(particles, weights, z, motion_model, measurement_model)

state_estimate = np.mean(particles) #Estimación final del estado.

print("Estimación del estado después del filtrado de partículas:", state_estimate) #Imprimimos resultados.