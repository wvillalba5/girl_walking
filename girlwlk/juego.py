
import os
import pygame
from  Chica import Girl 

class Game:
    pantalla = (800,400)
    color_fondo = (8,30,24)
    x_inicial = 50
    y_inicial = 225
    
    tiempo = pygame.time.Clock()
   
    framexseg = 30
    

    def __init__(self):
        pygame.init()
        self.fondo = pygame.display.set_mode(Game.pantalla)
    
        pygame.display.set_caption('Girl Walking')
        self.__Girl = Girl((Game.x_inicial, Game.y_inicial))
        
      


    def run(self):
        self.__running = True
        while self.__running: 
            self.__process_events()
            self.__Girl.movimiento_por_teclado(self.__event)
            self.__render()
            Game.tiempo.tick(Game.framexseg)

        self.__quit()   

    def __process_events(self):
       
        for self.__event in pygame.event.get():
            if self.__event.type == pygame.QUIT:
                self.__running = False

    def __render(self):
        self.fondo.fill( Game.color_fondo)
        self.fondo.blit(self.__Girl.image, self.__Girl.rect)
        pygame.display.flip()


    
    def __quit(self):
        pygame.quit ()
