#Alejandra Rodriguez Guevara 21310127 6E1

#El etiquetado de líneas se refiere a la identificación y clasificación de líneas dentro de una imagen o un conjunto de datos. Esto puede ser parte de un proceso 
#más amplio de análisis de imágenes, donde las líneas pueden representar bordes de objetos, límites de regiones, contornos, o características específicas de interés.

import cv2

#Función utilizada para el trackbar.
def nada(x):
    pass

#Leemos la imagen.
img = cv2.imread("46_Preprocesado-Filtros-Imagen-Original_Percep_V0.jpg")

#Redimensionamos la imagen.
filas, columnas, _ = img.shape
img = cv2.resize(img, (columnas // 1, filas // 1))

#Aplicamos un filtro de desenfoque.
img = cv2.blur(img, (5, 5))

#Creamos la ventana y barras deslizantes.
cv2.namedWindow("Canny con barras")
cv2.createTrackbar("Umbral1", "Canny con barras", 0, 400, nada)
cv2.createTrackbar("Umbral2", "Canny con barras", 0, 400, nada)

while True:
    img2 = img.copy()
    
    #Obtenemos los valores actuales de los trackbars.
    a = cv2.getTrackbarPos("Umbral1", "Canny con barras")
    b = cv2.getTrackbarPos("Umbral2", "Canny con barras")
    
    #Aplicamos el algoritmo de Canny.
    imgCanny = cv2.Canny(img, a, b)
    
    #Encontramos y dibujar contornos.
    contornos, _ = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img2, contornos, -1, (0, 255, 0), 3)

    #Mostramos la imagen resultante y la de los contornos.
    cv2.imshow("Canny con barras", imgCanny)
    cv2.imshow("Contornos", img2)
    
    #Salimos del bucle al presionar 's'.
    if cv2.waitKey(1) == ord("s"):
        break

#Cerramos todas las ventanas.
cv2.destroyAllWindows()