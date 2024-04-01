#Alejandra Rodriguez Guevara 21310127 6E1

#La incertidumbre en los grafos puede manifestarse de varias maneras, y las técnicas para manejarla varían dependiendo del contexto y del tipo de incertidumbre presente.

import random #Importamos la libreria necesaria.

def grafo_incertidumbre(graph): #Definimos una función para generar un grafo con incertidumbre a partir de un grafo dado.
    grafo_incertidumbre = {} #Inicializamos un diccionario vacío para el nuevo grafo con incertidumbre.
    
    for nodo, conexiones in graph.items(): #Iteramos sobre cada nodo y sus conexiones en el grafo original.
        grafo_incertidumbre[nodo] = {} #Inicializamos un diccionario vacío para las conexiones del nodo en el nuevo grafo.
        
        for vecino, longitud in conexiones.items(): #Iteramos sobre cada vecino y longitud en las conexiones del nodo original.
            incertidumbre = random.uniform(-0.5, 0.5) #Generamos un valor de incertidumbre aleatorio en el rango de -0.5 a 0.5.
            longitud_intervalo = (longitud - incertidumbre, longitud + incertidumbre) #Calculamos un intervalo de longitud para la arista.
            grafo_incertidumbre[nodo][vecino] = longitud_intervalo #Asignamos este intervalo de longitud al vecino en el nuevo grafo.
    return grafo_incertidumbre #Devolvemos el nuevo grafo con incertidumbre.

graph = {             #Declaramos nuestro grafo en base a la imagen "00.4_Mapa-de-Busqueda_Imagen-Referencia.png" y les asignamos costos por su longitud de separacion.
    'A': {'B':3, 'E':3},
    'B': {'A':3, 'C':2},
    'C': {'B':2, 'D':5, 'F':3},
    'D': {'C':5, 'I':3},
    'E': {'A':3, 'F':3, 'G':4, 'H':4},
    'F': {'C':3, 'E':3},
    'G': {'E':4, 'J':2},
    'H': {'E':4, 'I':2, 'J':4},
    'I': {'D':3, 'H':2, 'L':3},
    'J': {'G':2, 'H':4, 'K':3, 'M':3},
    'K': {'J':3, 'L':4},
    'L': {'I':3, 'K':4, 'N':7},
    'M': {'J':3, 'N':3},
    'N': {'L':7, 'M':3}
}

graph_uncertainty = grafo_incertidumbre(graph) #Generamos un nuevo grafo con incertidumbre a partir del grafo original.

for nodo, conexiones in graph_uncertainty.items(): #Mostramos las aristas y sus intervalos de longitud en el grafo con incertidumbre.
    for vecino, intervalo in conexiones.items():
        print("Arista:", nodo, "-", vecino, "Longitud:", intervalo)

#En este código, la incertidumbre se abordó generando variaciones aleatorias en las longitudes de las aristas y creando intervalos de longitud que reflejan esta incertidumbre.