#Alejandra Rodriguez Guevara 21310127 6E1

#-> k-Means: Es un algoritmo de agrupamiento que se utiliza para particionar un conjunto de datos en k grupos distintos. El algoritmo comienza con k centroides aleatorios, 
#luego asigna cada punto de datos al centroide más cercano y recalcula los centroides como el centroide del grupo. 

#-> Clustering: Clustering es el proceso de agrupar un conjunto de objetos en grupos o "clústeres" similares entre sí, con el objetivo de maximizar la similitud intra-cluster 
#y minimizar la similitud inter-cluster.

import matplotlib.pyplot as plt #Importamos las librerias necesarias.
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

#Generamos datos sintéticos.
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=42)

#Creamos el modelo k-Means con k=4.
kmeans = KMeans(n_clusters=4)

#Ajustamos el modelo a los datos.
kmeans.fit(X)

#Obtenemos las etiquetas de los clústeres y los centroides.
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

#Visualizamos los clústeres y los centroides.
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='o', s=200, color='red')
plt.title('Clústeres y Centroides') #Agregamos un titulo al grafico.
plt.xlabel('Característica 1') #Agregamos etiqueta al eje X y Y.
plt.ylabel('Característica 2')
plt.show() #Mostramos el grafico.