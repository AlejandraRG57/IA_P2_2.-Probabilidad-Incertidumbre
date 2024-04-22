#Alejandra Rodriguez Guevara 21310127 6E1

#El reconocimiento de objetos es una tarea fundamental en el campo de la visión por computadora que implica identificar y clasificar objetos dentro de imágenes o videos. 
#Esto puede incluir la detección de la presencia de objetos, la localización de su posición y la asignación de una etiqueta o categoría a cada objeto reconocido.

import cv2
import numpy as np

#Cargamos la imagen original.
imagenor = cv2.imread("46_Preprocesado-Filtros-Imagen-Original_Percep_V0.jpg") #Esta es nuestra imagen original.

#Función para encontrar y dibujar coincidencias entre una imagen y varias plantillas.
def match_and_draw(image, template_paths, threshold=0.8):
    #Cargamos la imagen sobre la cual buscar coincidencias.
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_rgb_copy = img_rgb.copy()

    #Iteramos sobre cada plantilla y buscamos coincidencias.
    for template_path in template_paths:
        template = cv2.imread(template_path, 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        
        #Dibujamos rectángulos alrededor de las coincidencias encontradas.
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb_copy, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    return img_rgb_copy

#Rutas de las plantillas a buscar en la imagen.
template_paths = ['49_Reconocimiento-de-Objetos-Template_Percep_V0.jpg', '49_Reconocimiento-de-Objetos-Template_Percep_V1.jpg', '49_Reconocimiento-de-Objetos-Template_Percep_V2.jpg', '49_Reconocimiento-de-Objetos-Template_Percep_V3.jpg'] # Añadimos las rutas de nuestras plantillas 

#Llamamos a la función y mostramos el resultado.
result_image = match_and_draw("46_Preprocesado-Filtros-Imagen-Original_Percep_V0.jpg", template_paths) # Esta es nuestra imagen original

cv2.imshow('Resultado Detectando Patitas', result_image)
cv2.imshow('Imagen original', imagenor)

cv2.waitKey(0)
cv2.destroyAllWindows()