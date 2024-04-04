#Alejandra Rodriguez Guevara 21310127 6E1

#Las redes neuronales multicapa (MLP, por sus siglas en inglés) son un tipo de red neuronal artificial que consta de al menos tres capas de nodos: 
#una capa de entrada, una o más capas ocultas y una capa de salida. Cada nodo en una capa está conectado a todos los nodos de la capa siguiente, y 
#estas conexiones están asociadas con pesos que se ajustan durante el proceso de entrenamiento.

from tensorflow.keras.models import Sequential #Importamos las librerias necesarias.
from tensorflow.keras.layers import Dense
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

#Generamos datos de ejemplo.
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

#Dividimos los datos en conjuntos de entrenamiento y prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Definimos  el modelo de red neuronal.
model = Sequential([
    Dense(64, activation='relu', input_shape=(20,)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

#Compilamos  el modelo.
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#Entrenamos  el modelo.
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test)) 

#Evaluamos  el modelo en datos de prueba.
loss, accuracy = model.evaluate(X_test, y_test)
print("Precisión del modelo en datos de prueba:", accuracy) #Imprimimos resultados.