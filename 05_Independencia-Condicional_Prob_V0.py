#Alejandra Rodriguez Guevara 21310127 6E1

#Dos variables aleatorias A y B se consideran condicionalmente independientes dada una tercera variable C si la ocurrencia o no ocurrencia de 
#A es independiente de la ocurrencia o no ocurrencia de B, dados los valores de C.
#Formalmente, A y B son condicionalmente independientes dados C si la siguiente igualdad se cumple:  P(A∩B∣C)=P(A∣C)⋅P(B∣C)

import numpy as np #Importamos la biblioteca necesaria.

def lanzamiento_moneda(): #Función para simular lanzamientos de moneda.
    return np.random.choice(['Cara', 'Cruz'])

def experimento(n): #Función para simular el experimento.
    resultados_A = [] #Almacenamos los resultados de la variable aleatoria A.
    resultados_B = [] #Almacenamos los resultados de la variable aleatoria B.
    
    for _ in range(n): #Realizamos el experimento.
        resultado_A = lanzamiento_moneda() #Lanzamos una moneda para la variable aleatoria A.
        resultado_B = lanzamiento_moneda() #Lanzamos una moneda para la variable aleatoria B.
        resultados_A.append(resultado_A) #Almacenamos los resultados.
        resultados_B.append(resultado_B)  
    return resultados_A, resultados_B

def verificar_independencia(resultados_A, resultados_B): #Función para verificar la independencia condicional.
    ocurrencias_A = {resultado: resultados_A.count(resultado) for resultado in set(resultados_A)} #Contamos las ocurrencias de los resultados.
    ocurrencias_B = {resultado: resultados_B.count(resultado) for resultado in set(resultados_B)}
    ocurrencias_conjuntas = {(resultado_A, resultado_B): 0 for resultado_A in ocurrencias_A.keys() for resultado_B in ocurrencias_B.keys()} #Contamos las ocurrencias conjuntas.

    for i in range(len(resultados_A)):
        ocurrencias_conjuntas[(resultados_A[i], resultados_B[i])] += 1
    
    prob_cond_A_dado_B = {conjunto: ocurrencias_conjuntas[conjunto] / ocurrencias_B[conjunto[1]] for conjunto in ocurrencias_conjuntas.keys()} #Calculamos las probabilidades condicionales.
    prob_cond_B_dado_A = {conjunto: ocurrencias_conjuntas[conjunto] / ocurrencias_A[conjunto[0]] for conjunto in ocurrencias_conjuntas.keys()}
    #Verificamos la independencia condicional.
    independencia = all(np.isclose(prob_cond_A_dado_B[conjunto], ocurrencias_A[conjunto[0]] / len(resultados_A)) for conjunto in ocurrencias_conjuntas.keys()) and all(np.isclose(prob_cond_B_dado_A[conjunto], ocurrencias_B[conjunto[1]] / len(resultados_B)) for conjunto in ocurrencias_conjuntas.keys())
    return independencia


n = 1000 #Número de experimentos.
resultados_A, resultados_B = experimento(n) #Realizamos el experimento.

independencia = verificar_independencia(resultados_A, resultados_B) #Verificamos la independencia condicional.
print("¿Las variables aleatorias A y B son condicionalmente independientes?", independencia) #imprimimos resultado.