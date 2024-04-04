#Alejandra Rodriguez Guevara 21310127 6E1

#La separabilidad lineal se refiere a la capacidad de un conjunto de datos de ser separado en clases distintas mediante una frontera de decisión lineal.

import numpy as np #Importamos las librerias necesarias.
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Generamos datos linealmente separables.
X, y = make_classification(n_samples=100, n_features=2, n_classes=2, n_clusters_per_class=1, n_informative=2, n_redundant=0, n_repeated=0, random_state=42)

#Dividimos los datos en conjuntos de entrenamiento y prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Creamos y entrenamos un clasificador Perceptrón.
perceptron = Perceptron()
perceptron.fit(X_train, y_train)

#Realizamos predicciones en el conjunto de prueba.
y_pred = perceptron.predict(X_test)

#Calculamos la precisión del clasificador.
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del Perceptrón:", accuracy) #Imprimimos la precisión.

#Visualizamos los datos y la frontera de decisión.
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, marker='o', edgecolors='k')
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

#Creamos una cuadrícula para evaluar el modelo.
xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 50), np.linspace(ylim[0], ylim[1], 50))
Z = perceptron.predict(np.c_[xx.ravel(), yy.ravel()])

#Coloreamos la región de decisión.
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Paired)

plt.title('Separabilidad Lineal y Clasificador Perceptrón') #Agregamos un titulo.
plt.xlabel('Feature 1') #Agregamos etiquetas al eje X y Y.
plt.ylabel('Feature 2')
plt.show()#Mostramos el grafico.