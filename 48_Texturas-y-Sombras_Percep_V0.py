#Alejandra Rodriguez Guevara 21310127 6E1 

#Las texturas se refieren a los patrones repetitivos en una imagen, como los granos de madera o las hojas de un árbol. En el procesamiento de imágenes, 
#la detección y análisis de texturas son importantes para tareas como clasificación de objetos o reconocimiento de superficies.

import cv2
import numpy as np

#Cargamos la imagen original.
imagen=cv2.imread("46_Preprocesado-Filtros-Imagen-Original_Percep_V0.jpg") #Esta es nuestra imagen original.
m,c,n=imagen.shape

cv2.imshow("Ajolote original", imagen)

#Convertimos la imagen a escala cromática.
imagenc=imagen.copy()
imagenc=imagenc.astype(np.float32)
imagen=imagen.astype(np.float32)

for x in range(m):
    for y in range(c):
        imagenc[x,y,0]=imagen[x,y,0]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])
        imagenc[x,y,1]=imagen[x,y,1]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])    
        imagenc[x,y,2]=imagen[x,y,2]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])

imagenc=imagenc*255
imagenc=imagenc.astype(np.uint8)    
cv2.imshow("imagen cromatica 1 ", imagenc)

#Convertimos la imagen cromática a espacio HSV y aplicamos un umbral para identificar el color rosa.
imagen_bi=cv2.cvtColor(imagenc, cv2.COLOR_BGR2HSV)
ros_low = np.array([107,46,65], np.uint8)
ros_high = np.array([255,230,255], np.uint8)
mascararosa=cv2.inRange(imagen_bi,ros_low,ros_high)

cv2.imshow("Imagen Binarizada 1", mascararosa)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------------------------

#Reducimos la intensidad de la imagen original y repetimos el proceso anterior.
imagenobs1=imagen*0.5
imagenobs1=imagenobs1.astype(np.uint8)
cv2.imshow("ajoloteobsc 1", imagenobs1)

imagenc1=imagenobs1.copy()
imagenc1=imagenc1.astype(np.float32)
imagenobs1=imagenobs1.astype(np.float32)

for x in range(m):
    for y in range(c):
        imagenc1[x,y,0]=imagenobs1[x,y,0]/(imagenobs1[x,y,0]+imagenobs1[x,y,1]+imagenobs1[x,y,2])
        imagenc1[x,y,1]=imagenobs1[x,y,1]/(imagenobs1[x,y,0]+imagenobs1[x,y,1]+imagenobs1[x,y,2])
        imagenc1[x,y,2]=imagenobs1[x,y,2]/(imagenobs1[x,y,0]+imagenobs1[x,y,1]+imagenobs1[x,y,2])

imagenc1=imagenc1*255
imagenc1=imagenc1.astype(np.uint8)
cv2.imshow("imagen cromatica 2",imagenc1)

imagen_bi2=cv2.cvtColor(imagenc1, cv2.COLOR_BGR2HSV)
ros_low = np.array([107,46,65], np.uint8)
ros_high = np.array([255,230,255], np.uint8)
mascararosa2=cv2.inRange(imagen_bi2,ros_low,ros_high)

cv2.imshow("Imagen Binarizada 2", mascararosa2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------------------------

#Reducimos aún más la intensidad de la imagen original y repetimos el proceso anterior.
imagenobs2=imagen*0.2
imagenobs2=imagenobs2.astype(np.uint8)
cv2.imshow("ajoloteobsc 2", imagenobs2)

imagenc2=imagenobs2.copy()
imagenc2=imagenc2.astype(np.float32)
imagenobs2=imagenobs2.astype(np.float32)

for x in range(m):
    for y in range(c):
        imagenc2[x,y,0]=imagenobs2[x,y,0]/(imagenobs2[x,y,0]+imagenobs2[x,y,1]+imagenobs2[x,y,2])
        imagenc2[x,y,1]=imagenobs2[x,y,1]/(imagenobs2[x,y,0]+imagenobs2[x,y,1]+imagenobs2[x,y,2])
        imagenc2[x,y,2]=imagenobs2[x,y,2]/(imagenobs2[x,y,0]+imagenobs2[x,y,1]+imagenobs2[x,y,2])

imagenc2=imagenc2*255
imagenc2=imagenc2.astype(np.uint8)
cv2.imshow("imagen cromatica 3",imagenc2)

imagen_bi3=cv2.cvtColor(imagenc2, cv2.COLOR_BGR2HSV)
ros_low = np.array([107,46,65], np.uint8)
ros_high = np.array([255,230,255], np.uint8)
mascararosa3=cv2.inRange(imagen_bi3,ros_low,ros_high)

cv2.imshow("Imagen Binarizada 3", mascararosa3)
cv2.waitKey(0)
cv2.destroyAllWindows()
