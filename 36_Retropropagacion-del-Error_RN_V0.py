#Alejandra Rodriguez Guevara 21310127 6E1

#La retropropagación del error (backpropagation en inglés) es un algoritmo utilizado en el entrenamiento de redes neuronales artificiales para ajustar 
#los pesos de las conexiones entre neuronas, con el objetivo de minimizar el error entre las salidas predichas y las salidas reales.

from tensorflow.keras.models import Sequential #Importamos las librerias necesarias.
from tensorflow.keras.layers import Dense
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

#Generamos datos de ejemplo.
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

#Dividimos los datos en conjuntos de entrenamiento y prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Definimos el modelo de red neuronal.
model = Sequential([
    Dense(64, activation='relu', input_shape=(20,)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

#Compilamos el modelo.
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#Entrenamos el modelo con retropropagación del error.
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))