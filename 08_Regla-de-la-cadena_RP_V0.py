#Alejandra Rodriguez Guevara 21310127 6E1

#La regla de la cadena es un principio fundamental en la teoría de la probabilidad que se utiliza para calcular la probabilidad 
#conjunta de un conjunto de variables aleatorias mediante la descomposición en factores de las probabilidades condicionales.

#Probabilidad de obtener cara o cruz  en un lanzamiento de moneda.
p_cara = 0.5
p_cruz = 0.5

#Probabilidad conjunta de los resultados de dos lanzamientos de moneda utilizando la regla de la cadena.
p_conjunta =  p_cara * p_cara #Ambos lanzamientos resultan en cara.
p_conjunta += p_cara * p_cruz #El primer lanzamiento es cara y el segundo es cruz.
p_conjunta += p_cruz * p_cara #El primer lanzamiento es cruz y el segundo es cara.
p_conjunta += p_cruz * p_cruz #Ambos lanzamientos resultan en cruz.

print("La probabilidad conjunta de los resultados de ambos lanzamientos es:", p_conjunta) #Imprimimos resultado.