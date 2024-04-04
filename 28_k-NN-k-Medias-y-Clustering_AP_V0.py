#Alejandra Rodriguez Guevara 21310127 6E1

#-> k-NN (k-Nearest Neighbors): Este algoritmo se utiliza para problemas de clasificación y regresión.
#Es un método basado en instancias, lo que significa que no intenta aprender un modelo explícito, sino que memoriza los datos de entrenamiento.

from sklearn.datasets import load_iris #Importamos las librerias necesarias.
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#Cargamos el conjunto de datos Iris.
iris = load_iris()
X = iris.data
y = iris.target

#Dividimos el conjunto de datos en entrenamiento y prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#Creamos un clasificador k-NN con k=3.
knn = KNeighborsClassifier(n_neighbors=3)

#Entrenamos al clasificador k-NN con los datos de entrenamiento.
knn.fit(X_train, y_train)

#Realizamos predicciones en el conjunto de prueba.
y_pred = knn.predict(X_test)

#Calculamos la precisión del clasificador.
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del clasificador k-NN:", accuracy) #Imprimimos resultado.