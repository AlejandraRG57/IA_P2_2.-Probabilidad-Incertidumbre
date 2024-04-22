#Alejandra Rodriguez Guevara 21310127 6E1

#El software robótico abarca una amplia gama de herramientas, bibliotecas y marcos de trabajo diseñados para programar, controlar y gestionar robots y sistemas robóticos.

import pygame
import time

#Configuramos el robot.
robot_x = 100
robot_y = 100

#Configuramos la ventana.
window_width = 800
window_height = 600

#Configuramos los colores.
white = (255, 255, 255)
black = (0, 0, 0)

#Función principal.
def main():
    #Inicializamos Pygame.
    pygame.init()
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Simulación de Robot")

    #Bucle principal.
    running = True
    while running:
        #Manejo de eventos.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Lógica del robot (aquí iría el código de control).
        move_robot()

        #Dibujamos el robot y la ventana.
        window.fill(white)
        pygame.draw.circle(window, black, (robot_x, robot_y), 20)
        pygame.display.update()

        #Pequeño retraso para controlar la velocidad de la simulación.
        time.sleep(0.05)

    #Salimos de Pygame al finalizar.
    pygame.quit()

#Función para controlar el movimiento del robot.
def move_robot():
    global robot_x, robot_y
    #Por simplicidad, simplemente hacemos que el robot se mueva hacia la derecha.
    robot_x += 1
    #robot_y += 1 para moverlo hacia abajo o si pongo ambos en diagonal.

#Llamamos a la función principal al ejecutar el script.
if __name__ == "__main__":
    main()