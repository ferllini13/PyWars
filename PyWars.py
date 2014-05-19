import pygame
import sys
import string
from pygame.locals import *

pygame.mixer.init()
pygame.mixer.music.load("sound.mp3")
back_sound= pygame.mixer.Sound("back.wav")
pygame.mixer.music.play(loops=-1)


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
		if cursor.colliderect(self.rect):#se define la condicion cuando el cursor se pocisione sobre el bot
			self.basic_pic=self.selected_pic
		else: self.basic_pic=self.unselected_pic #condicion del boton en stand by
		screen.blit(self.basic_pic,self.rect)#que se actualiza la pantalla dependiendo de la accion condicional


class ConfigError(KeyError): pass

class Config:
	""" A utility for configuration """
	def __init__(self, options, *look_for):
		assertions = []
		for key in look_for:
			if key[0] in options.keys(): exec('self.'+key[0]+' = options[\''+key[0]+'\']')
			else: exec('self.'+key[0]+' = '+key[1])
			assertions.append(key[0])
		for key in options.keys():
			if key not in assertions: raise ConfigError(key+' not expected as option')

class Input:
	""" A text input for pygame apps """
	def __init__(self, **options):
		""" Options: x, y, font, color, restricted, maxlength, prompt """
		self.options = Config(options, ['x', '0'], ['y', '100'], ['font', 'pygame.font.Font(None, 32)'],
							['color', '(0,0,0)'], ['restricted', '\'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\\\'()*+,-./:;<=>?@[\]^_`{|}~\''],
								['maxlength', '-1'], ['prompt', '\'\''])
		self.x = self.options.x; self.y = self.options.y
		self.font = self.options.font
		self.color = self.options.color
		self.restricted = self.options.restricted
		self.maxlength = self.options.maxlength
		self.prompt = self.options.prompt; self.value = ''
		self.shifted = False

	def set_pos(self, x, y):
		""" Set the position to x, y """
		self.x = x
		self.y = y

	def set_font(self, font):
		""" Set the font for the input """
		self.font = font

	def draw(self, surface):
		""" Draw the text input to a surface """
		text = self.font.render(self.prompt+self.value, 1, self.color)
		surface.blit(text, (self.x, self.y))

	def update(self, events):
		""" Update the input based on passed events """
		for event in events:
			if event.type == KEYUP:
				if event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = False
			if event.type == KEYDOWN:
				if event.key == K_BACKSPACE: self.value = self.value[:-1]
				elif event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = True
				elif event.key == K_SPACE: self.value += ' '
				elif event.key==pygame.K_RETURN: return self.value
				if not self.shifted:
					if event.key == K_a and 'a' in self.restricted: self.value += 'a'
					elif event.key == K_b and 'b' in self.restricted: self.value += 'b'
					elif event.key == K_c and 'c' in self.restricted: self.value += 'c'
					elif event.key == K_d and 'd' in self.restricted: self.value += 'd'
					elif event.key == K_e and 'e' in self.restricted: self.value += 'e'
					elif event.key == K_f and 'f' in self.restricted: self.value += 'f'
					elif event.key == K_g and 'g' in self.restricted: self.value += 'g'
					elif event.key == K_h and 'h' in self.restricted: self.value += 'h'
					elif event.key == K_i and 'i' in self.restricted: self.value += 'i'
					elif event.key == K_j and 'j' in self.restricted: self.value += 'j'
					elif event.key == K_k and 'k' in self.restricted: self.value += 'k'
					elif event.key == K_l and 'l' in self.restricted: self.value += 'l'
					elif event.key == K_m and 'm' in self.restricted: self.value += 'm'
					elif event.key == K_n and 'n' in self.restricted: self.value += 'n'
					elif event.key == K_o and 'o' in self.restricted: self.value += 'o'
					elif event.key == K_p and 'p' in self.restricted: self.value += 'p'
					elif event.key == K_q and 'q' in self.restricted: self.value += 'q'
					elif event.key == K_r and 'r' in self.restricted: self.value += 'r'
					elif event.key == K_s and 's' in self.restricted: self.value += 's'
					elif event.key == K_t and 't' in self.restricted: self.value += 't'
					elif event.key == K_u and 'u' in self.restricted: self.value += 'u'
					elif event.key == K_v and 'v' in self.restricted: self.value += 'v'
					elif event.key == K_w and 'w' in self.restricted: self.value += 'w'
					elif event.key == K_x and 'x' in self.restricted: self.value += 'x'
					elif event.key == K_y and 'y' in self.restricted: self.value += 'y'
					elif event.key == K_z and 'z' in self.restricted: self.value += 'z'
					elif event.key == K_0 and '0' in self.restricted: self.value += '0'
					elif event.key == K_1 and '1' in self.restricted: self.value += '1'
					elif event.key == K_2 and '2' in self.restricted: self.value += '2'
					elif event.key == K_3 and '3' in self.restricted: self.value += '3'
					elif event.key == K_4 and '4' in self.restricted: self.value += '4'
					elif event.key == K_5 and '5' in self.restricted: self.value += '5'
					elif event.key == K_6 and '6' in self.restricted: self.value += '6'
					elif event.key == K_7 and '7' in self.restricted: self.value += '7'
					elif event.key == K_8 and '8' in self.restricted: self.value += '8'
					elif event.key == K_9 and '9' in self.restricted: self.value += '9'
					elif event.key == K_BACKQUOTE and '`' in self.restricted: self.value += '`'
					elif event.key == K_MINUS and '-' in self.restricted: self.value += '-'
					elif event.key == K_EQUALS and '=' in self.restricted: self.value += '='
					elif event.key == K_LEFTBRACKET and '[' in self.restricted: self.value += '['
					elif event.key == K_RIGHTBRACKET and ']' in self.restricted: self.value += ']'
					elif event.key == K_BACKSLASH and '\\' in self.restricted: self.value += '\\'
					elif event.key == K_SEMICOLON and ';' in self.restricted: self.value += ';'
					elif event.key == K_QUOTE and '\'' in self.restricted: self.value += '\''
					elif event.key == K_COMMA and ',' in self.restricted: self.value += ','
					elif event.key == K_PERIOD and '.' in self.restricted: self.value += '.'
					elif event.key == K_SLASH and '/' in self.restricted: self.value += '/'
				elif self.shifted:
					if event.key == K_a and 'A' in self.restricted: self.value += 'A'
					elif event.key == K_b and 'B' in self.restricted: self.value += 'B'
					elif event.key == K_c and 'C' in self.restricted: self.value += 'C'
					elif event.key == K_d and 'D' in self.restricted: self.value += 'D'
					elif event.key == K_e and 'E' in self.restricted: self.value += 'E'
					elif event.key == K_f and 'F' in self.restricted: self.value += 'F'
					elif event.key == K_g and 'G' in self.restricted: self.value += 'G'
					elif event.key == K_h and 'H' in self.restricted: self.value += 'H'
					elif event.key == K_i and 'I' in self.restricted: self.value += 'I'
					elif event.key == K_j and 'J' in self.restricted: self.value += 'J'
					elif event.key == K_k and 'K' in self.restricted: self.value += 'K'
					elif event.key == K_l and 'L' in self.restricted: self.value += 'L'
					elif event.key == K_m and 'M' in self.restricted: self.value += 'M'
					elif event.key == K_n and 'N' in self.restricted: self.value += 'N'
					elif event.key == K_o and 'O' in self.restricted: self.value += 'O'
					elif event.key == K_p and 'P' in self.restricted: self.value += 'P'
					elif event.key == K_q and 'Q' in self.restricted: self.value += 'Q'
					elif event.key == K_r and 'R' in self.restricted: self.value += 'R'
					elif event.key == K_s and 'S' in self.restricted: self.value += 'S'
					elif event.key == K_t and 'T' in self.restricted: self.value += 'T'
					elif event.key == K_u and 'U' in self.restricted: self.value += 'U'
					elif event.key == K_v and 'V' in self.restricted: self.value += 'V'
					elif event.key == K_w and 'W' in self.restricted: self.value += 'W'
					elif event.key == K_x and 'X' in self.restricted: self.value += 'X'
					elif event.key == K_y and 'Y' in self.restricted: self.value += 'Y'
					elif event.key == K_z and 'Z' in self.restricted: self.value += 'Z'
					elif event.key == K_0 and ')' in self.restricted: self.value += ')'
					elif event.key == K_1 and '!' in self.restricted: self.value += '!'
					elif event.key == K_2 and '@' in self.restricted: self.value += '@'
					elif event.key == K_3 and '#' in self.restricted: self.value += '#'
					elif event.key == K_4 and '$' in self.restricted: self.value += '$'
					elif event.key == K_5 and '%' in self.restricted: self.value += '%'
					elif event.key == K_6 and '^' in self.restricted: self.value += '^'
					elif event.key == K_7 and '&' in self.restricted: self.value += '&'
					elif event.key == K_8 and '*' in self.restricted: self.value += '*'
					elif event.key == K_9 and '(' in self.restricted: self.value += '('
					elif event.key == K_BACKQUOTE and '~' in self.restricted: self.value += '~'
					elif event.key == K_MINUS and '_' in self.restricted: self.value += '_'
					elif event.key == K_EQUALS and '+' in self.restricted: self.value += '+'
					elif event.key == K_LEFTBRACKET and '{' in self.restricted: self.value += '{'
					elif event.key == K_RIGHTBRACKET and '}' in self.restricted: self.value += '}'
					elif event.key == K_BACKSLASH and '|' in self.restricted: self.value += '|'
					elif event.key == K_SEMICOLON and ':' in self.restricted: self.value += ':'
					elif event.key == K_QUOTE and '"' in self.restricted: self.value += '"'
					elif event.key == K_COMMA and '<' in self.restricted: self.value += '<'
					elif event.key == K_PERIOD and '>' in self.restricted: self.value += '>'
					elif event.key == K_SLASH and '?' in self.restricted: self.value += '?'
		if len(self.value) > self.maxlength and self.maxlength >= 0: self.value = self.value[:-1]




def main():
	pygame.init()
	screen=pygame.display.set_mode([1000,720])
	pygame.display.set_caption("PYWARS")
	wallp=pygame.image.load("wall.jpg").convert()
	wallp2=pygame.image.load("wall2.jpg").convert()
	wallp3=pygame.image.load("wall3.jpg").convert()
	wallp4=pygame.image.load("wall4.jpg").convert()
	cursor1=cursor()

	#se inportan las imagenes de los botones
	play=pygame.image.load("play.png")
	play2=pygame.image.load("play2.png")
	instruc=pygame.image.load("instruc.png")
	instruc2=pygame.image.load("instruc2.png")
	salir=pygame.image.load("exit.png")
	salir2=pygame.image.load("exit2.png")
	back=pygame.image.load("back.png")
	back2=pygame.image.load("back2.png")
	start=pygame.image.load("start.png")
	start2=pygame.image.load("start2.png")
	join=pygame.image.load("join.png")
	join2=pygame.image.load("join2.png")
	
	bplay=button(play,play2,600,200)
	binstruc=button(instruc,instruc2,650,300)
	bexit=button(salir,salir2,700,400)
	bback=button(back,back2,10,5)
	bstart=button(start,start2,0,400)
	bjoin=button(join,join2,700,400)


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
					return play_main()
				elif cursor1.colliderect(binstruc.rect):
					return game_instruc()
				elif cursor1.colliderect(bexit.rect):
					pygame.quit()
					sys.exit()
			elif event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.flip()


		def play_main():
			while True:
				screen.blit(wallp2,(0,0))
				bback.update(screen,cursor1)
				bstart.update(screen,cursor1)
				bjoin.update(screen,cursor1)
				cursor1.update()
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN:
						if cursor1.colliderect(bback.rect):
							pygame.mixer.pre_init(44100, -16, 1024)
							back_sound.play()
							return main()
						elif cursor1.colliderect(bstart.rect):
							return start_join_game()
						elif cursor1.colliderect(bjoin.rect):
							return start_join_game()
					elif event.type==pygame.QUIT:
						pygame.quit()
						sys.exit()
				pygame.display.flip()

		def game_instruc():
			while True:
				screen.blit(wallp3,(0,0))
				bback.update(screen,cursor1)
				cursor1.update()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					if event.type == pygame.MOUSEBUTTONDOWN:
						if cursor1.colliderect(bback.rect):
							pygame.mixer.pre_init(44100, -16, 1024) 
							back_sound.play()
							return main()
				pygame.display.flip()
				
		def start_join_game():
			wallp4=pygame.image.load("wall4.jpg").convert()
			txtbx=Input(maxlength=20, color=(0,255,255), prompt='Username: ')
		
			
			while True:
				screen.blit(wallp4,(0,0))
				events=pygame.event.get()
				user=txtbx.update(events)
				txtbx.draw(screen)
				for event in events:
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
					if event.type == KEYDOWN:
						if event.key==pygame.K_RETURN:
							print(user)
					#if cursor1.colliderect(

				pygame.display.flip()


main()
