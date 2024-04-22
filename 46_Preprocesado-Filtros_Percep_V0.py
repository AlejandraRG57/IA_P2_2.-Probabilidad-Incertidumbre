#Alejandra Rodriguez Guevara 21310127 6E1

#Los filtros utilizados en procesamiento de imágenes para la percepción suelen enfocarse en realzar ciertas características de la imagen o 
#reducir el ruido sin afectar demasiado los detalles importantes.

import cv2 #Importamos las librerias necesarias.
import numpy as np

imagenor=cv2.imread("46_Preprocesado-Filtros-Imagen-Original_Percep_V0.jpg") #Esta es nuestra imagen original.
imagen = cv2.imread("46_Preprocesado-Filtros-Imagen-Color_Percep_V1.jpg") #Esta es la imagen que editamos color morado.

#Convertir la imagen a escala de grises.
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

#Encontramos el píxel más brillante en la imagen (píxel blanco).
max_value = np.amax(gris)
max_index = np.where(gris == max_value)

#Calculamos el valor promedio de los canales de color en ese píxel (white patch).
white_patch = imagen[max_index[0][0], max_index[1][0]]

#Calculamos el coeficiente de escala para cada canal.
scale_factors = np.divide(255.0, white_patch)

#Aplicamos el ajuste de balance de blancos multiplicando cada canal por el coeficiente de escala.
imagen_corregida = np.clip(imagen * scale_factors, 0, 255).astype(np.uint8)

#Aplicamos corrección de gamma para hacer la imagen aún más neutra.
gamma = 1
imagen_corregida_gamma = np.clip(np.power(imagen_corregida / 255.0, gamma) * 255.0, 0, 255).astype(np.uint8)

#Convertimos a binario.
imagen_bi=cv2.cvtColor(imagen_corregida_gamma, cv2.COLOR_BGR2HSV)
ros_low = np.array([100,45,100], np.uint8)
ros_high = np.array([255,230,255], np.uint8)
mascararosa=cv2.inRange(imagen_bi,ros_low,ros_high)

imagen_bi2=cv2.cvtColor(imagen_corregida_gamma, cv2.COLOR_BGR2HSV)
amar_low = np.array([10,50,50], np.uint8)
amar_high = np.array([65,255,255], np.uint8)
mascara_amar = cv2.inRange(imagen_bi2,amar_low,amar_high)

#Mostramos la imagen corregida y la comparativa de a que se deberia de asemejar y como se veia originalmente.
cv2.imshow("Imagen Original", imagenor)
cv2.imshow("Imagen Color Morado", imagen)
cv2.imshow("Imagen Corregida Morado", imagen_corregida_gamma) #Esta es nuestra imagen corregida.

cv2.waitKey(0)
cv2.destroyAllWindows()