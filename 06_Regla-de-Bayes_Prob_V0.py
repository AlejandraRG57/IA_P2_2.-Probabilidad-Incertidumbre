#Alejandra Rodriguez Guevara 21310127 6E1

#La regla de Bayes es un principio fundamental en la teoría de la probabilidad y la estadística que se utiliza para actualizar 
#las creencias sobre un evento en función de la evidencia observada. 

#Definimos las probabilidades.
p_enfermedad = 0.01  #Probabilidad a priori de tener la enfermedad.
p_positivo_dado_enfermedad = 0.9  #Sensibilidad de la prueba.
p_positivo_dado_no_enfermedad = 0.05  #Probabilidad de un resultado positivo dado que no tiene la enfermedad (falsos positivos).

#Aplicamos la regla de Bayes
p_enfermedad_dado_positivo = (p_positivo_dado_enfermedad * p_enfermedad) / ((p_positivo_dado_enfermedad * p_enfermedad) + (p_positivo_dado_no_enfermedad * (1 - p_enfermedad)))

#Imprimimos el resultado
print("La probabilidad de tener la enfermedad dado un resultado positivo en la prueba es:", p_enfermedad_dado_positivo)

#Con el codigo calculamos la probabilidad de que un paciente tenga la enfermedad dado un resultado positivo en la prueba, utilizando la regla de Bayes.