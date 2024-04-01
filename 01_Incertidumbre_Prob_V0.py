#Alejandra Rodriguez Guevara 21310127 6E1

#La incertidumbre en el contexto de la probabilidad se refiere a la falta de certeza o la imposibilidad de predecir con precisión el resultado de un evento futuro.

import random  #Importamos el módulo random para generar números aleatorios.

def lanzamiento_dado():  #Definimos una función para simular el lanzamiento de un dado.
    return random.randint(1, 6)  #Devolvemos un número aleatorio entre 1 y 6, simulando el resultado del lanzamiento del dado.

def calcular_probabilidad_numero_par(intentos):  #Definimos una función para calcular la probabilidad de obtener un número par en un dado número de intentos.
    conteo_pares = 0  #Inicializamos el contador para los números pares.
    for _ in range(intentos):  #Repetimos el proceso de lanzamiento del dado el número de veces especificado en 'intentos'.
        resultado = lanzamiento_dado()  #Realizamos un lanzamiento del dado.
        if resultado % 2 == 0:  #Verificamos si el resultado es un número par.
            conteo_pares += 1  #Si el resultado es par, incrementamos el contador de números pares.
    probabilidad = conteo_pares / intentos  #Calculamos la probabilidad dividiendo el número de pares entre el total de intentos.
    return probabilidad  #Devolvemos la probabilidad calculada.

intentos = 10000  #Especificamos la cantidad de lanzamientos.
probabilidad_par = calcular_probabilidad_numero_par(intentos)  #Calculamos la probabilidad de obtener un número par en los intentos especificados.
print("La probabilidad de que salga un número par en el lanzamiento de un dado es aproximadamente:", probabilidad_par)  #Imprimimos la probabilidad calculada.