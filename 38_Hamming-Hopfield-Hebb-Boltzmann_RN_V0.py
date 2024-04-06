#Alejandra Rodriguez Guevara 21310127 6E1

#-> Distancia de Hamming: es una medida de la diferencia entre dos secuencias de símbolos del mismo tamaño. 
#Se define como el número de posiciones en las que los símbolos correspondientes son diferentes. 

def hamming_distance(str1, str2):
    #Nos aseguramos de que las cadenas tengan la misma longitud.
    if len(str1) != len(str2):
        raise ValueError("Las cadenas deben tener la misma longitud")

    hamming_dist = 0 #Inicializamos la distancia de Hamming.

    #Calculamos la distancia de Hamming.
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            hamming_dist += 1

    return hamming_dist

str1 = "1010101"
str2 = "1001001"
distance = hamming_distance(str1, str2)
print("Distancia de Hamming entre", str1, "y", str2, ":", distance) #Imprimimmos el resultado