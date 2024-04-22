#Alejandra Rodriguez Guevara 21310127 6E1

#La recuperación de datos se refiere al proceso de recuperar información o patrones útiles de un conjunto de datos, 
#generalmente mediante técnicas de aprendizaje automático, minería de datos o procesamiento de lenguaje natural.

import numpy as np
from sklearn.impute import SimpleImputer

#Datos de ejemplo con algunos valores faltantes.
data = np.array([[1, 2, np.nan],
                 [4, np.nan, 6],
                 [np.nan, 8, 9]])

#Creamos el imputador.
imputer = SimpleImputer(strategy='mean')  # Otros strategies: 'median', 'most_frequent', 'constant'.

#Entrenamos el imputador en los datos de ejemplo y luego lo aplicamos para imputar los valores faltantes.
imputed_data = imputer.fit_transform(data)

print("Datos originales:")
print(data)
print("\nDatos imputados:")
print(imputed_data)