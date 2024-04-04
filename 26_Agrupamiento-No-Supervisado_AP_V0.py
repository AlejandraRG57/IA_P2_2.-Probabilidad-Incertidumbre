#Alejandra Rodriguez Guevara 21310127 6E1

#El agrupamiento no supervisado es una técnica de aprendizaje automático utilizada para identificar patrones o estructuras ocultas en un conjunto de datos sin etiquetas. 
#Algunos de los algoritmos de agrupamiento no supervisado más comunes incluyen: K-Means, Agrupamiento jerárquico, Modelos de mezcla gaussiana, DBSCAN y Agrupamiento espectral.

#En este ejemplo utilizamos el agrupamiento jerárquico.

import matplotlib.pyplot as plt #Importamos las librerias necesarias.
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

#Generamos datos sintéticos.
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

#Calculamos la matriz de enlace utilizando el método de enlace completo.
linkage_matrix = linkage(X, method='complete')

#Mostramos el dendrograma.
plt.figure(figsize=(12, 6))
dendrogram(linkage_matrix)
plt.title('Dendrograma') #Agregamos un titulo.
plt.xlabel('Índices de datos') #Agregamos etiquetas al eje X y Y.
plt.ylabel('Distancia')
plt.grid(False) #Ocultamos la cuadricula.
plt.show() #Mostramos el gráfico.

#Ajustamos el modelo de agrupamiento jerárquico.
agg_cluster = AgglomerativeClustering(n_clusters=4, linkage='complete')
agg_cluster.fit(X)

#Visualizamos los clústeres.
plt.scatter(X[:, 0], X[:, 1], c=agg_cluster.labels_, cmap='viridis', alpha=0.5)
plt.title('Agrupamiento Jerárquico') #Agregamos un titulo.
plt.xlabel('Feature 1') #Agregamos etiquetas al eje X y Y.
plt.ylabel('Feature 2')
plt.grid(True) #Mostramos la cuadricula.
plt.show() #Mostramos el gráfico.