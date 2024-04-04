#Alejandra Rodriguez Guevara 21310127 6E1

#La computación neuronal, también conocida como neurocomputación, se refiere al estudio y la aplicación de modelos y algoritmos 
#computacionales inspirados en el funcionamiento del cerebro humano y el sistema nervioso.

from tensorflow.keras import layers, models #Importamos las librerias necesarias.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

#Cargamos el conjunto de datos Iris.
iris_data = load_iris()
X, y = iris_data.data, iris_data.target

#Dividimos los datos en conjuntos de entrenamiento y prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Construimos el modelo de red neuronal.
model = models.Sequential([
    layers.Dense(10, activation='relu', input_shape=(4,)),
    layers.Dense(3, activation='softmax')
])

#Compilamos el modelo.
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#Entrenamos el modelo.
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

#Evaluamos el modelo en datos de prueba.
test_loss, test_acc = model.evaluate(X_test, y_test)
print('Precisión en datos de prueba:', test_acc) #Imprimimos resultados.