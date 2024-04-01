#Alejandra Rodriguez Guevara 21310127 6E1

#-> Probabilidad condicionada: La probabilidad condicionada se refiere a la probabilidad de que ocurra un evento A dado que otro evento B ya ha ocurrido.
#-> Normalización: La normalización se refiere al proceso de ajustar valores para que estén dentro de un rango específico o cumplan ciertas propiedades deseables.

def probabilidad_condicionada(prob_A_interseccion_B, prob_B): #Función para calcular la probabilidad condicionada P(A|B).
    return prob_A_interseccion_B / prob_B

def normalizar_probabilidad(distribucion_probabilidad): #Función para normalizar una distribución de probabilidad.
    suma_total = sum(distribucion_probabilidad) #Calculamos la suma total de probabilidades.
    return [prob / suma_total for prob in distribucion_probabilidad] #Normalizamos cada probabilidad dividiéndola por la suma total.

distribucion_probabilidad = [0.2, 0.2, 0.2, 0.2] #Proponemos un ejemplo de distribución de probabilidad.

#Normalizamos la distribución de probabilidad solo si no está normalizada.
if sum(distribucion_probabilidad) != 1:
    distribucion_normalizada = normalizar_probabilidad(distribucion_probabilidad)
else:
    distribucion_normalizada = distribucion_probabilidad

print("Distribución de probabilidad original:", distribucion_probabilidad) #Imprimimos resultados.
print("Distribución de probabilidad normalizada:", distribucion_normalizada)

prob_A_interseccion_B = 0.2  #Probabilidad de la intersección de los eventos A y B.
prob_B = 0.5  #Probabilidad del evento condicionante B.

prob_condicionada = probabilidad_condicionada(prob_A_interseccion_B, prob_B) #Calculamos la probabilidad condicionada P(A|B).
print("La probabilidad condicionada P(A|B) es:", prob_condicionada) #Imprimimos el resultado.