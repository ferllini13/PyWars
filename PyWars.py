import pygame
import sys
from pygame.locals import *
pygame.mixer.init()



pygame.mixer.music.load("sound.mp3")



#se crea la clase para los button para los botones
class button(pygame.sprite.Sprite):#se crea la clase para los botones
    def __init__(self,pic1,pic2,x,y):#se define cada boton con dos imagenes y las coordenadas
        self.unselected_pic=pic1#se define como se vera la imagen sin seleccionar
        self.selected_pic=pic2 #se define como se vera la imagen seleccionada
        self.basic_pic=self.unselected_pic #se define una imagen bacica qie inicia como la no seleccionada
        self.rect=self.basic_pic.get_rect()
        self.rect.left,self.rect.top=(x,y)
        
    def update(self,screen,cursor):#se actializa el boton
        if cursor.colliderect(self.rect):#se define la condicion cuando el cursor se pocisione sobre el boton
            self.basic_pic=self.selected_pic
        else: self.basic_pic=self.unselected_pic #condicion del boton en stand by
        screen.blit(self.basic_pic,self.rect)#que se actualiza la pantalla dependiendo de la accion condicional



def main():
    pygame.init()
    screen=pygame.display.set_mode([1000,720])
    pygame.display.set_caption("Tarea Corta")
    wallp=pygame.image.load("wall2.jpg").convert()
    pygame.mixer.music.play() 
    
    
    while True:
        screen.blit(wallp,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

                
        pygame.display.flip()
        
        
        
    
    
    
main()
