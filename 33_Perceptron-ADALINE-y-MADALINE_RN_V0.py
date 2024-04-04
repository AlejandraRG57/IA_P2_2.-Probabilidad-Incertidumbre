#Alejandra Rodriguez Guevara 21310127 6E1

#-> Perceptrón: El perceptrón es un modelo de clasificación binaria que puede aprender a separar linealmente dos clases.
#-> ADALINE (Adaptive Linear Neuron): ADALINE es un modelo similar al perceptrón, pero con una salida lineal en lugar de una salida binaria. 
#-> MADALINE (Multiple ADALINE): MADALINE es una extensión de ADALINE que utiliza múltiples neuronas lineales para formar un modelo más complejo.

import numpy as np #Importamos las librerias necesarias.
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.metrics import accuracy_score
from sklearn.linear_model import Perceptron, SGDRegressor
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


#Cargamos el conjunto de datos Iris.
iris_data = load_iris()
X, y = iris_data.data, iris_data.target

#Dividimos los datos en conjuntos de entrenamiento y prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Creamos y entrenamos un perceptrón.
perceptron = Perceptron()
perceptron.fit(X_train, y_train)

#Evaluamos el perceptrón.
perceptron_score = accuracy_score(y_test, perceptron.predict(X_test))
print("Precisión del perceptrón:", perceptron_score)

#Creamos y entrenamos un ADALINE.
adaline = SGDRegressor(max_iter=1000, tol=1e-3)
adaline.fit(X_train, y_train)

#Evaluamos el ADALINE.
adaline_score = adaline.score(X_test, y_test)
print("Precisión de ADALINE:", adaline_score) #Imprimimos resultado de ADALINE.

class MADALINE(BaseEstimator, ClassifierMixin):
    def __init__(self, n_neurons=3, max_iter=1000, tol=1e-3):
        self.n_neurons = n_neurons #Número de neuronas ADALINE en la red MADALINE.
        self.max_iter = max_iter #Número máximo de iteraciones permitidas durante el entrenamiento de cada ADALINE.
        self.tol = tol #Tolerancia para la convergencia durante el entrenamiento de cada ADALINE.
        self.adalines = [] #Inicializamos y añadimos ADALINEs a la lista adalines
        for _ in range(n_neurons):
            self.adalines.append(SGDRegressor(max_iter=self.max_iter, tol=self.tol))

    def fit(self, X, y):
        for i, adaline in enumerate(self.adalines):
            binary_y = np.where(y == i, 1, -1) #Convertimos etiquetas a -1 y 1.
            adaline.fit(X, binary_y) #Entrenamos el modelo ADALINE correspondiente a la clase i

    def predict(self, X):
        predictions = np.zeros((X.shape[0], len(self.adalines))) #Inicializamos la matriz para almacenar predicciones de cada ADALINE.
        for i, adaline in enumerate(self.adalines):
            predictions[:, i] = adaline.predict(X) #Realizamos predicciones con el modelo ADALINE correspondiente a la clase i.
        return np.argmax(predictions, axis=1) #Seleccionamos la clase con la predicción más alta para cada muestra.

#Usamos MADALINE en el conjunto de datos Iris
madaline = MADALINE(n_neurons=3)
madaline.fit(X_train, y_train)

#Evaluamos MADALINE
madaline_score = accuracy_score(y_test, madaline.predict(X_test))
print("Precisión de MADALINE:", madaline_score) #Imprimimos resultado de MADALINE.
