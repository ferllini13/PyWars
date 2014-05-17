import pygame
import sys
from pygame.locals import *

pygame.mixer.init()
pygame.mixer.music.load("sound.mp3")
select_sound= pygame.mixer.Sound("select.wav")

#se cra la clase cursor, que es un rectangulo qeu sigue al mouse
class cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)#cursos inicia en coordenadas 0,0 y es de 1x1
    def update(self):#actualiza la pocision del cursos dependiendo de la del mouse
        self.left,self.top=pygame.mouse.get_pos()#capta la posicion del mouse

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
            select_sound.play
            self.basic_pic=self.selected_pic
        else: self.basic_pic=self.unselected_pic #condicion del boton en stand by
        screen.blit(self.basic_pic,self.rect)#que se actualiza la pantalla dependiendo de la accion condicional



def main():
    pygame.init()
    screen=pygame.display.set_mode([1000,720])
    pygame.display.set_caption("Tarea Corta")
    wallp=pygame.image.load("wall2.jpg").convert()
    cursor1=cursor()
    pygame.mixer.music.play() 
    
    
    while True:
        screen.blit(wallp,(0,0))
        cursor1.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)         
        pygame.display.flip()
    
    
main()
