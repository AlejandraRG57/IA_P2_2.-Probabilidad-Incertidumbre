#Alejandra Rodriguez Guevara 21310127 6E1

#El clasificador Naive Bayes es un modelo de clasificación probabilístico que se basa en el Teorema de Bayes 
#y asume independencia condicional entre las características (variables predictoras) dadas las clases.

from sklearn.datasets import load_iris #Importamos las librerias necesarias.
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

#Cargamos el conjunto de datos Iris.
iris = load_iris()
X = iris.data
y = iris.target

#Dividimos el conjunto de datos en datos de entrenamiento y datos de prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Creamos el clasificador Naive Bayes.
clf = GaussianNB()

#Entrenamos el clasificador Naive Bayes con los datos de entrenamiento.
clf.fit(X_train, y_train)

#Realizamos predicciones sobre los datos de prueba.
y_pred = clf.predict(X_test)

#Calculamos la precisión del clasificador.
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del clasificador Naive Bayes:", accuracy)

#Mostramos un informe de clasificación.
print("\nInforme de clasificación:")
print(classification_report(y_test, y_pred))