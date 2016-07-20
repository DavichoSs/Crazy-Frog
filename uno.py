import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()
ventana=pygame.display.set_mode((1040,600))#ancho 1040, alto 600
pygame.display.set_caption("JUEGO SAPO LOCO")
imagen=pygame.image.load("imagen2.png").convert_alpha()
imagenf=pygame.image.load("fondo.jpg").convert_alpha()
imagent=pygame.image.load("arbol.png").convert_alpha()

#poxa=randint(10,300)
#posya=randint(10,200)
posx=100
posy=500

posxa=0
posya=0

velocidad=2
blanco=(255,255,255)
derecha=True

while True:
	ventana.fill(blanco)
	ventana.blit(imagenf,(0,0))
	ventana.blit(imagent,(posxa,posya))
	ventana.blit(imagen,(posx,posy))
	for event in pygame.event.get():
		if event.type ==QUIT:
			pygame.quit()
			sys.exit()
		
	if derecha==True:
		if posxa<950:
			posxa+=velocidad
		else:
			derecha=False
	else:
		if posxa>1:
			posxa-=velocidad
		else:
			derecha=True
	pygame.display.update()