import os
import pygame


class Girl(pygame.sprite.Sprite):
    __imagen_girl_path = ['assets','imagenes','gcam.png']
    __frame = 0


    def __init__(self, hubicacion_inicial):
        self.__tapiz_completo = pygame.image.load(os.path.join(*Girl.__imagen_girl_path ))
        self.__tapiz_completo.set_clip(pygame.Rect(0, 0, 64, 130))
        self.image = self.__tapiz_completo.subsurface(self.__tapiz_completo.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = hubicacion_inicial
        
        
        self.__girl_move_right = { 0: (64, 0, 64, 130), 1: (128, 0, 64, 130), 2: (192, 0, 64, 130),
                            3: (256, 0, 64, 130), 4: (320, 0, 64, 130), 5: (384, 0, 64, 130),
                            6: (448, 0, 64, 130), 7: (512, 0, 64, 130), 8: (576, 0, 64, 130) }

        self.__girl_move_left = { 0: (64, 130, 64, 130), 1: (128, 130, 64, 130), 2: (192, 130, 64, 130),
                            3: (256, 130, 64, 130), 4: (320, 130, 64, 130), 5: (384, 130, 64, 130),
                            6: (448, 130, 64, 130), 7: (512, 130, 64, 130), 8: (576, 130, 64, 130) }
        
        self.__girl_stop = {0:(0,0,64,130) , 1:(0,130,64,130)}


    
    def __Recuadro(self, frame_set):
        
        Girl.__frame += 1
        if Girl.__frame > (len(frame_set) - 1):
            Girl.__frame = 0
           
        return frame_set[Girl.__frame]

    def __Area_Recorte_Actual(self, girl_frame):
     
        if type(girl_frame) is dict:
            self.__tapiz_completo.set_clip(pygame.Rect(self.__Recuadro(girl_frame)))
        else:
            self.__tapiz_completo.set_clip(pygame.Rect(girl_frame))
        return girl_frame

    def __Actualizar(self, direccion_movimiento,):
        
        if  direccion_movimiento is 'mov_izquierda' and self.rect.x >= 10:
            self.__Area_Recorte_Actual(self.__girl_move_left)
            self.rect.x -= 10
            
        if direccion_movimiento is 'mov_derecha' and self.rect.x <= 550:
            self.__Area_Recorte_Actual(self.__girl_move_right)
            self.rect.x += 10
            
       
        if direccion_movimiento is 'parada_izquierda':
            self.__Area_Recorte_Actual(self.__girl_stop[0])
        if direccion_movimiento is 'parada_derecha':
            self.__Area_Recorte_Actual(self.__girl_stop[1])
        self.image = self.__tapiz_completo.subsurface(self.__tapiz_completo.get_clip())
        

    def movimiento_por_teclado(self, evento):
        
        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_LEFT:
                self.__Actualizar('mov_izquierda')
                
            if evento.key == pygame.K_RIGHT:
                self.__Actualizar('mov_derecha')
                

        if evento.type == pygame.KEYUP:

            if evento.key == pygame.K_LEFT:
                self.__Actualizar('parada_izquierda')
            if evento.key == pygame.K_RIGHT:
                self.__Actualizar('parada_derecha')
           
           
           
           
