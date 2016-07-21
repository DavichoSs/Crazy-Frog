import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()
ventana=pygame.display.set_mode((1040,600))#ancho 1400, alto 900
pygame.display.set_caption("JUEGO SAPO LOCO")
imagen=pygame.image.load("imagen2.png").convert_alpha()
imagenf=pygame.image.load("fondo.jpg").convert_alpha()
imagent=pygame.image.load("arbol.png").convert_alpha()
#arbol=pygame.image.load("obs.png")

#poxa=randint(10,300)
#posya=randint(10,200)
posx=500
posy=500

posxa=0
posya=0

posxa1=0
posya1=250

velocidadO=2
velocidad=20
blanco=(255,255,255)
derecha=True

while True:
	#ventana.fill(blanco)
	ventana.blit(imagenf,(0,0))
	ventana.blit(imagent,(posxa,posya))
	#ventana.blit(arbol,(posxa1,posya1))
	ventana.blit(imagen,(posx,posy))

	for event in pygame.event.get():
		if event.type ==QUIT:
			pygame.quit()
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			if event.key==K_LEFT:
				posx-=velocidad
			elif event.key==K_RIGHT:
				posx+=velocidad
		if event.type ==QUIT:
			pygame.quit()
			sys.exit()
		elif event.type==pygame.KEYUP:
			if event.key==K_UP:
				posy-=velocidad
			elif event.key==K_DOWN:
				posy+=velocidad

	'''posx,posy=pygame.mouse.get_pos()
	posx=posx-50
	posy=posy-50'''


	if derecha==True:
		if posxa<950:
			posxa+=velocidadO
		else:
			derecha=False
	else:
		if posxa>1:
			posxa-=velocidadO
		else:
			derecha=True

	

	pygame.display.update()