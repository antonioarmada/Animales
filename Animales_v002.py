
# para compiliar .exe:
# pip install pyinstaller
# pyinstaller --onefile <your_script_name>.py
# ojo que no copia las carpetas con otros archivos, mover manualmente a "dist"


import pygame
import random
import time
import os
import random

#os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0) # posiciona la pantalla ANTE DE INICIALIZAR PYGAME!!!

pygame.init()


infoPantalla = pygame.display.Info()

print (infoPantalla)

display_width = infoPantalla.current_w
display_height =infoPantalla.current_h
velocSol=80

gameDisplay = pygame.display.set_mode((display_width,display_height),pygame.FULLSCREEN) #,pygame.RESIZABLE ,pygame.FULLSCREEN
pygame.display.set_caption('ANIMALES')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
frameGeneral=0
solXactual=200
slideActual=0
mouseX, mouseY = pygame.mouse.get_pos()

clock = pygame.time.Clock()

class Sprite_animado:
	frame= 1 #aca pongo  atributos comunes a todos las instancias de esta clase no va self
	fin=False	

	def __init__(self,archivoIMG, archivoSND,anchoFrame,cantFrames): # se ejecuta al iniciar la clase y contiene los atributos
		self.imagen = pygame.image.load(archivoIMG).convert_alpha()
		self.ancho, self.alto = self.imagen.get_size()
		self.anchoFrame= anchoFrame
		self.cantFrames = cantFrames
		self.sonido = pygame.mixer.Sound(archivoSND)
		#self.invertido=False
	
	def mostrar(self,x,y,frame_,invertido): # es una accion que puede tomar la clase
		#print(self.invertido)
		if not invertido:
			gameDisplay.blit(self.imagen, (x,y),(self.anchoFrame*frame_,0,self.anchoFrame,self.alto)) #el ultimo parentisis es el recorte x_inicial,y_inicial,ancho,alto
		if invertido:
			gameDisplay.blit(pygame.transform.flip(self.imagen,True,False), (x,y),(self.anchoFrame*frame_,0,self.anchoFrame,self.alto))

	
	def playSND (self,reproducir):
		if not pygame.mixer.get_busy() and reproducir:
			self.sonido.play()
		elif pygame.mixer.get_busy() and not reproducir:
			self.sonido.fadeout(300)



def game_loop():
	x =  (display_width * 0.45)
	y = (display_height * 0.8)
	frameDer=0
	frameIzq=0
	cuadranteReproduciendo=0

	global frameGeneral
	global slideActual
	solX=80
	solXactual=solX

	iniciaColicion=True

	gameExit = False

	pygame.mouse.set_pos([display_width/2, display_height/2])

	while not gameExit:
		frameGeneral +=1
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if  pygame.key.name(event.key) == "escape":
					pygame.quit()
					quit()
				if  pygame.key.name(event.key) == "left":
					print("flecha izq")
					slideActual-=1
				if  pygame.key.name(event.key) == "right":
					print("flecha der")
					slideActual+=1
			if event.type == pygame.MOUSEMOTION:
				mouseX, mouseY = pygame.mouse.get_pos()
				if mouseX < display_width*0.38:
					solX= (display_width*.29)-sol.anchoFrame/2
					cuadrante=0
					frameDer=0
				elif mouseX > display_width*0.6:
					solX= (display_width/2)+sol.anchoFrame
					cuadrante=1
					frameIzq=0
				else:
					cuadrante=2
					frameIzq=0
					frameDer=0
					solX= (display_width*.27)+sol.anchoFrame

		# Desplaza Sol
		if solX>solXactual:
			solXactual+=velocSol
		if solX<solXactual:
			solXactual-=velocSol

		# Anima Sol
		if frameGeneral%6==0: # hago que sea mas lento el framerate de la planta
			if sol.frame < sol.cantFrames-1:
				sol.frame +=1
			else:
				sol.frame=1

		# Anima Animal Seleccionado
		if frameGeneral%3==0 and cuadrante==0: # hago que sea mas lento el framerate de la planta
			if frameIzq < perro.cantFrames-1:
				frameIzq +=1
			else:
				frameIzq=1
		if frameGeneral%3==0 and cuadrante==1: # hago que sea mas lento el framerate de la planta
			if frameDer < perro.cantFrames-1:
				frameDer +=1
			else:
				frameDer=1

		gameDisplay.fill(white)

		sol.mostrar(solXactual,100,sol.frame,False)
		
		if slideActual < 0: 
			slideActual=0
		if slideActual > 2: 
			slideActual=2

		slidesAnimales[slideActual][0].mostrar(170,350,frameIzq,False)
		slidesAnimales[slideActual][1].mostrar(820,350,frameDer,False)

		
		if not cuadrante==2:
			slidesAnimales[slideActual][cuadrante].playSND(True)
			cuadranteReproduciendo=cuadrante
		else:
			slidesAnimales[slideActual][cuadranteReproduciendo].playSND(False)


		pygame.display.update()
		clock.tick(30)

fuenteArial = pygame.font.SysFont('Arial', 15)
txtEscape = fuenteArial.render('presionar ESCAPE para salir', True, (200, 200, 200))

sol= Sprite_animado("img/sol_sprite.png","snd/gallo.wav",218,9)
perro=Sprite_animado("img/perro_sprite.png","snd/perro.wav",400,9)
oveja=Sprite_animado("img/oveja_sprite.png","snd/oveja.wav",400,9)
leon=Sprite_animado("img/leon_sprite.png","snd/leon.wav",400,9)
gato=Sprite_animado("img/gato_sprite.png","snd/gato.wav",400,9)
gallina=Sprite_animado("img/gallina_sprite.png","snd/gallo.wav",400,9)
elefante=Sprite_animado("img/elefante_sprite.png","snd/elefante.wav",400,9)

pygame.mixer.music.load('snd/musica.mp3') #music es streaming no esta en buffer como .sound
pygame.mixer.music.set_volume(0.2) #0 a 1
pygame.mixer.music.play(-1) #-1 para loop 

slidesAnimales=((gato,perro),(leon,elefante),(gallina,oveja))


game_loop()
pygame.quit()
quit()