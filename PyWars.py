import pygame
import sys
from pygame.locals import *

pygame.mixer.init()
pygame.mixer.music.load("sound.mp3")
select_sound= pygame.mixer.Sound("select.wav")

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
    
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
            self.basic_pic=self.selected_pic
            select_sound.play
        else: self.basic_pic=self.unselected_pic #condicion del boton en stand by
        screen.blit(self.basic_pic,self.rect)#que se actualiza la pantalla dependiendo de la accion condicional


def sizesWin(text1,screen):
					
	#Title picture and buttons
	crear=pygame.image.load("play.png")
	unirse=pygame.image.load("play.png")
	salir=pygame.image.load("play.png")
	
	#Define buttons
	bcrear= button(crear,crear,50,250)
	
	#Variables
	lenghtW=0
	textBuffer = ''
	begin=True
	place=120
	cursor1=cursor()
					
	pygame.init()
	
	#Events and updates
	while begin==True:
		cursor1.update()
		
		#Updates
		bcrear.update(screen,cursor1)	
		
		#Makes the labels
		myfont= pygame.font.SysFont("monospace",25)
		myfont2= pygame.font.SysFont("monospace",16)
	
		labelInd= myfont.render(text1,1,BLACK)		
		
		
		screen.blit(labelInd,(10,120))
    
		
		for event in pygame.event.get():
			#Events on keyboard, for the entry
			if event.type==pygame.KEYDOWN:
				
				#Limit the keys allowed to numbers
				if	event.key<=122 and event.key>=97 and lenghtW<12*10:
					#This creates the text of the entry
					textBuffer=textBuffer+chr(event.key)
					lenghtW+=15
					place=place+15
					myfont= pygame.font.SysFont("monospace",25)
					label=myfont.render(chr(event.key),1,BLACK)
					screen.blit(label,(place,120))
					
				elif    event.key<=57 and event.key>=48 and lenghtW<12*10:
					#This creates the text of the entry
					textBuffer=textBuffer+chr(event.key)
					lenghtW+=15
					place=place+15
					myfont= pygame.font.SysFont("monospace",25)
					label=myfont.render(chr(event.key),1,BLACK)
					screen.blit(label,(place,120))
				
				#To delete the words
				elif event.key == pygame.K_BACKSPACE and len(textBuffer)>0:
					textBuffer=textBuffer[:-1]
					lenghtW-=15
					place=place-15
					myfont= pygame.font.SysFont("monospace",25)
					label=myfont.render(textBuffer,1,BLACK)
					screen.fill(WHITE)
					screen.blit(label,(130,120))
				
				#This saves the entry
				elif event.key==pygame.K_RETURN:
					if len(textBuffer)>0:
						begin=False
						return textBuffer

			#Submit button		
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if cursor1.colliderect(bcrear.rect):
					if len(textBuffer)>0:
						begin=False
						return textBuffer
						
			#To Close the window
			elif event.type == pygame.QUIT:
				return sys.exit(0)

		#Update the window		
		pygame.display.flip()


def main():
    pygame.init()
    screen=pygame.display.set_mode([1000,720])
    pygame.display.set_caption("PYWARS")
    wallp=pygame.image.load("wall2.jpg").convert()
    pygame.mixer.music.play()
    cursor1=cursor()

    #se inportan las imagenes de los botones
    play=pygame.image.load("play.png")
    play2=pygame.image.load("play2.png")
    instruc=pygame.image.load("instruc.png")
    instruc2=pygame.image.load("instruc2.png")
    salir=pygame.image.load("exit.png")
    salir2=pygame.image.load("exit2.png")
    
    bplay=button(play,play2,600,200)
    binstruc=button(instruc,instruc2,650,300)
    bexit=button(salir,salir2,700,400)
    
    
    
    
    while True:
        screen.blit(wallp,(0,0))
        cursor1.update()

        #se actualizan los botones
        bplay.update(screen,cursor1)
        bexit.update(screen,cursor1)
        binstruc.update(screen,cursor1)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(bplay.rect):
                    screen=pygame.display.set_mode([1000,720])
                    screen.blit(wallp,(0,0))
                    pygame.display.set_caption("PYWARS")
                    wallp=pygame.image.load("wall2.jpg").convert()
                    pygame.mixer.music.load("select.wav")
                    pygame.mixer.music.play()
                    usuario=sizesWin('Usuario:',screen)
                    print('Welcome'+usuario)
                elif cursor1.colliderect(binstruc.rect):
                    return main2(square)
                elif cursor1.colliderect(bexit.rect):
                    return main2(rectangle)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)         
        pygame.display.flip()
    
    
main()
