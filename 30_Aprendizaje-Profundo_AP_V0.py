#Alejandra Rodriguez Guevara 21310127 6E1

#El aprendizaje profundo, también conocido como deep learning en inglés, es una rama del aprendizaje automático que se basa en redes neuronales 
#artificiales con múltiples capas de procesamiento. A través de estas redes, el aprendizaje profundo busca aprender representaciones de datos de 
#manera jerárquica y automatizada, permitiendo la extracción de características y la realización de tareas complejas de aprendizaje.

import tensorflow as tf #Importamos las librerias necesarias.
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

#Cargamos los datos de entrenamiento y prueba de MNIST.
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#Normalizamos los datos y convertimos las etiquetas a one-hot encoding.
x_train, x_test = x_train / 255.0, x_test / 255.0
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

#Construimos el modelo de red neuronal.
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

#Compilamos el modelo.
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#Entrenamos a el modelo.
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_test, y_test))

#Evaluamos el modelo en datos de prueba.
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Precisión en datos de prueba:', test_acc) #Imprimimos resultados.