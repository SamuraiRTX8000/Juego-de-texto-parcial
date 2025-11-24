import pygame

class Prueba:
    def __init__(self,x,y):
        self.forma = pygame.Rect(0,0,50,50)
        self.forma.center = (x,y)
        self.color=(255,255,0) 
    def dibujar(self, screen):
        pygame.draw.rect(screen,self.color,self.forma)
        
        
