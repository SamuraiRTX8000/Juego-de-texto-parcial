import pygame 
import constantes
from clases_jugador import Prueba
 
jugador = Prueba(50,50)
#Inicialisacion
pygame.init()
#creacion de la pantalla e importacion de constantes
screen = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                  constantes.ALTO_VENTANA))

pygame.display.set_caption("EEB")
run = True
#ciclo para el juego
while run == True:
    #importacion de funcion dibujar
    jugador.dibujar(screen)
    #lee los eventos(interacciones)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #actualiza la pantalla para mostrar eventos anteriores/ se actuliza por que la peimera pantalla es negra
    pygame.display.update()
 #lee el evento de cerrar el programa
pygame.quit()