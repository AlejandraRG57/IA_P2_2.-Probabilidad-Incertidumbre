#Alejandra Rodriguez Guevara 21310127 6E1

#Las Máquinas de Vectores de Soporte (SVM) son un algoritmo de aprendizaje supervisado utilizado para clasificación y regresión. En su forma básica, 
#SVM encuentra el hiperplano óptimo que separa los puntos de datos de diferentes clases en un espacio dimensional más alto.

from sklearn.datasets import make_classification #Importamos las librerias necesarias.
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#Generamos datos sintéticos para clasificación.
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

#Dividimos los datos en conjunto de entrenamiento y prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Creamos un clasificador SVM con un núcleo radial.
svm = SVC(kernel='rbf')

#Entrenamos al clasificador SVM.
svm.fit(X_train, y_train)

#Realizamos predicciones en el conjunto de prueba.
y_pred = svm.predict(X_test)

#Calculamos la precisión del clasificador.
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del clasificador SVM:", accuracy) #Imprimimos resultados.