#Alejandra Rodriguez Guevara 21310127 6E1

#El movimiento en el contexto del procesamiento de imágenes se refiere a la detección, seguimiento y análisis de los 
#cambios en la posición de objetos en secuencias de imágenes o vídeos a lo largo del tiempo.

import cv2

#Abrimos el archivo de video.
video = cv2.VideoCapture('51_Etiquetados-de-Lineas-Video_Percep_V0.mkv')

i = 0
while True:
    #Leemos el siguiente fotograma del video.
    ret, frame = video.read()
    
    #Si no hay fotogramas restantes, salimos del bucle.
    if ret == False:
        break
    
    #Convertimos la imagen a escala de grises.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Almacenamos el fotograma 20 como fondo de referencia.
    if i == 20:
        bgGray = gray
    
    #Calculamos la diferencia entre el fotograma actual y el fondo de referencia.
    if i > 20:
        dif = cv2.absdiff(gray, bgGray)
        
        #Aplicamos umbralización para resaltar las diferencias.
        _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
        
        #Encontramos contornos en las diferencias.
        cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        #Dibujamos rectángulos alrededor de los contornos detectados.
        for c in cnts:
            area = cv2.contourArea(c)
            if area > 9000:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    #Mostramos el fotograma actual con los contornos detectados.
    cv2.imshow('Frame', frame)

    #Incrementamos el contador de fotogramas.
    i = i + 1
    
    #Esperamos 30 milisegundos para la próxima tecla.
    if cv2.waitKey(30) & 0xFF == ord ('q'):
        break

#Liberamos el objeto de video.
video.release()

#Cerramos todas las ventanas.
cv2.destroyAllWindows()