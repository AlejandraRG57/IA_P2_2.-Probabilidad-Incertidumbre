#Alejandra Rodriguez Guevara 21310127 6E1

#El reconocimiento de escritura es una tarea en la que se busca convertir la escritura a mano en texto digitalmente legible. 
#Este proceso implica la detección y análisis de los patrones de escritura manual para identificar letras, palabras y frases.

import cv2
import easyocr

#Inicializamos el lector de OCR para el idioma español.
reader = easyocr.Reader(["es"], gpu=False)

#Cargamos la imagen.
image = cv2.imread("50_Reconocimiento-de-Escritura-Imagen-Texto_Percep_V0.jpg")

#Realizamos el reconocimiento de texto en la imagen.
result = reader.readtext(image, paragraph=False)

#Iteramos sobre los resultados obtenidos.
for res in result:
    #Imprimimos cada resultado.
    print("res:", res)
    
    #Obtenemos las coordenadas de los puntos del cuadro del texto.
    pt0 = res[0][0]
    pt1 = res[0][1]
    pt2 = res[0][2]
    pt3 = res[0][3]
    
    #Dibujamos un rectángulo de fondo para el texto.
    cv2.rectangle(image, pt0, (pt1[0], pt1[1] - 23), (166, 56, 242), -1)
    
    #Escribimos el texto sobre la imagen.
    cv2.putText(image, res[1], (pt0[0], pt0[1] - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 1)
    
    #Dibujamos el contorno del texto.
    cv2.rectangle(image, pt0, pt2, (166, 56, 242), 2)
    
    #Dibujamos círculos en los puntos de referencia del texto.
    cv2.circle(image, pt0, 2, (255, 0, 0), 2)
    cv2.circle(image, pt1, 2, (0, 255, 0), 2)
    cv2.circle(image, pt2, 2, (0, 0, 255), 2)
    cv2.circle(image, pt3, 2, (0, 255, 255), 2)
    
    #Mostramos la imagen con los resultados.
    cv2.imshow("Image", image)
    cv2.waitKey(0)

#Cerramos todas las ventanas al finalizar.
cv2.destroyAllWindows()