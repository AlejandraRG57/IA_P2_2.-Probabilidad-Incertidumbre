#Alejandra Rodriguez Guevara 21310127 6E1

#La detección de aristas se refiere a identificar los límites entre regiones en una imagen, mientras que la segmentación implica dividir 
#una imagen en partes significativas basadas en ciertas características como color, textura o forma.

import cv2
import numpy as np 

#Cargamos la imagen original.
imagen = cv2.imread("46_Preprocesado-Filtros-Imagen-Original_Percep_V0.jpg") 

#Convertimos la imagen a espacio de color HSV.
imagen2 = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
#Definimos el rango de colores para el fondo.
fondo_bajo = np.array([100, 100, 100], np.uint8)
fondo_alto = np.array([140, 255, 255], np.uint8)

#Creamos una máscara para el fondo.
mascara_fondo = cv2.inRange(imagen2, fondo_bajo, fondo_alto)
mascara_todos= cv2.bitwise_not(mascara_fondo)
mascara = cv2.bitwise_and(imagen2,imagen2,mask=mascara_todos)

#Definimos el rango de colores para el amarillo.
amar_low = np.array([10,50,50], np.uint8)
amar_high = np.array([65,255,255], np.uint8)

#Creamos una máscara para el color amarillo.
mascara_amar = cv2.inRange(imagen2,amar_low,amar_high)

#Definimos el rango de colores para el rosa.
rosa_low = np.array([107,46,65], np.uint8)
rosa_high = np.array([255,230,255], np.uint8)

#Creamos una máscara para el color rosa.
mascara_rosa = cv2.inRange(imagen2,rosa_low,rosa_high)

#Encontramos los contornos de las regiones amarillas y rosas.
contornos_amarillo, _ = cv2.findContours(mascara_amar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornos_rosa, _ = cv2.findContours(mascara_rosa, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Dibujamos rectángulos alrededor de los contornos encontrados.
for contorno in contornos_amarillo:
    x, y, w, h = cv2.boundingRect(contorno)
    cv2.rectangle(mascara, (x, y), (x+w, y+h), (0, 255, 255), 2)
    
for contorno in contornos_rosa:
    x, y, w, h = cv2.boundingRect(contorno)
    cv2.rectangle(mascara, (x, y), (x+w, y+h), (255, 50, 255), 2)
    
#Mostramos las imágenes.
cv2.imshow('Imagen Original', imagen)
cv2.imshow ('Ventanas',mascara)

cv2.waitKey(0) 
cv2.destroyAllWindows()