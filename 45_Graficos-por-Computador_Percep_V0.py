#Alejandra Rodriguez Guevara 21310127 6E1

#La percepción en gráficos por computadora se refiere al proceso mediante el cual una computadora interpreta y 
#representa datos visuales para crear imágenes comprensibles por el usuario.

#Importamos los paquetes.
import pygame
import sys

#Inicializamos Pygame.
pygame.init()

#Creamos la pantalla.
PANTALLA = pygame.display.set_mode((500, 400))

# Especificamos el título.
pygame.display.set_caption("FONDO")

#Creamos una paleta de colores.
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
HC74225 = (199, 66, 37)
H61CD35 = (97, 205, 53)
ROSA = (255, 192, 203)

PANTALLA.fill(NEGRO) #Hacemos el fondo de color negro.
pygame.draw.rect(PANTALLA, ROJO, (100,100,70,50)) #Dibujamos un rectangulo -> (En la pantalla, De color rojo, (Posicion X y Y, Dimensiones en pixeles).
pygame.draw.line(PANTALLA, VERDE, (70,200),(199,200), 1) #Dibujamos una linea -> (En la pantalla, De color Verde, (Coordenadas de los extremos de la línea), Grosor).
pygame.draw.circle(PANTALLA, AZUL, (122, 250), 20, 0) #Dibujamos un circulo -> (En la pantalla, De color Azul, (Centro del circulo), Radio en pixeles, grosor del borde del circulo si es 0 se rellena completamente).
pygame.draw.ellipse(PANTALLA, BLANCO, (275, 200, 40, 80), 10) #Dibujamos una elipse -> (En la pantalla, De color Blanco, (Posicion X y Y, Anchura y altura en pixeles), Grosor, si es 0 se rellena completamente).
puntos = [(100,300), (100,100), (170,100)] #Forma libre, declaramos 3 puntos que seran los vertices de nuestro poligono.
pygame.draw.polygon(PANTALLA, ROSA, puntos, 8) #Dibujamos el poligono -> (En la pantalla, Su color, vertices, grosor si es 0 se rellena).

#Bucle de ejecución.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit()		
    pygame.display.update()