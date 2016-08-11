import pygame,sys
from pygame.locals import *
from random import randint
from Tkinter import *

#Funcion Pagina de Inicio
def pagina(): 
	cuadro = Tk()
	canvas = Canvas(cuadro, width=900, height=400)
	cuadro.title("CRAZY FROG")
	fondo = PhotoImage(file="sapoloco.gif")
	lblImagen= Label(cuadro, image=fondo).place(x=0 , y=0) #definida como pantalla de fondo
	inicio= PhotoImage(file="btninicio.gif")
	boton= Button(cuadro,image= inicio ,command=cuadro.quit).place(x=300, y=50) # definida como imagen en un punto especifico
	canvas.pack()
	cuadro.mainloop()

vidas =5
#pagina() #Llamado a la funcion

pygame.init()

pagina() 

Fuente=pygame.font.SysFont("Arial",30)
pygame.mixer.music.load("juego.mp3")
pygame.mixer.music.play(1)
ventana=pygame.display.set_mode((1040,600))#ancho 1400, alto 900
pygame.display.set_caption("CRAZY FROG")
imagen=pygame.image.load("imagen2.png").convert_alpha()
imagenf=pygame.image.load("fondo.jpg").convert_alpha()
imagent=pygame.image.load("arbol.png").convert_alpha()
imagenc=pygame.image.load("carro.png").convert_alpha()
carro2=pygame.image.load("carro2.png").convert_alpha()
carro3=pygame.image.load("carro3.png").convert_alpha()
carro4=pygame.image.load("carro4.png").convert_alpha()

Fuente = pygame.font.SysFont("Times New Roman	",20,)

#poxa=randint(10,300)
#posya=randint(10,200)
posx=500
posy=500

posxa=0
posya=39

posxa1=0
posya1=400

posxa2=0
posya2=300

posxa3=0
posya3=350

posxa4=0
posya4=450

posxa5=0
posya5=250


velocidadO=1
velocidad=2
velocidad3=3
velocidads=50
blanco=(255,255,100)
derecha=True
aux=1


while True:
	ventana.fill((255,255,255))
	Tiempo =pygame.time.get_ticks()/1000
	if aux == Tiempo:
		aux+=1
		print (Tiempo)
	#ventana.fill(blanco)
	ventana.blit(imagenf,(0,0))
	ventana.blit(imagent,(posxa,posya))
	ventana.blit(imagen,(posx,posy))
	ventana.blit(imagenc,(posxa2,posya2))
	ventana.blit(carro2,(posxa3,posya3))
	ventana.blit(carro3,(posxa4,posya4))
	ventana.blit(carro4,(posxa5,posya5))
	##tiempo()

	for event in pygame.event.get():
		if event.type ==QUIT:
			pygame.quit()
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			if event.key==K_LEFT:
				posx-=velocidads
			elif event.key==K_RIGHT:
				posx+=velocidads
		if event.type ==QUIT:
			pygame.quit()
			sys.exit()
		elif event.type==pygame.KEYUP:
			if event.key==K_UP:
				posy-=velocidads
			elif event.key==K_DOWN:
				posy+=velocidads

	if derecha==True:	
		if posxa  <900 :
			posxa+=velocidadO
			posxa2+=velocidad
			posxa3+=velocidad
			posxa4+=velocidad
			posxa5+=velocidad
		else:
			derecha=False
	else:
		if posxa >1:
			posxa-=velocidadO
			posxa2=-80
			posxa3=-230
			posxa4=-80
			posxa5=-80
			posxa2+=velocidad
			posxa3+=velocidad
			posxa4+=velocidad
			posxa5+=velocidad
		else:
			derecha=True
#colisiones
	
	def perder (vidas): #Funcion de la vidas del sapo
		vidas= vidas-1
		aux = vidas
		print ("Te restan "+ str(aux) +" vidas")
		if vidas == 0:
			print ("Has agotado todas tus vidas")
			pygame.display.quit()
			final = Tk()
			canvas = Canvas(final, width=440, height=440)
			final.title("CRAZY FROG")
			lblfinal= Label(final,text="GAME OVER")
			lblfinal.pack()
			canvas.pack()
			final.mainloop()
			final.quit


	if posx == posxa4  and posy ==posya4 :
		posx=500
		posy=500
		vidas-=1
		perder(vidas)
		#print ("perdiste")

	elif posx == posxa5 and posy == posya5:
		posx=500
		posy=500
		vidas-=1
		perder(vidas)
		#print ("perdiste")

	if posx == posxa2 and posy == posya2 :
		posx=500
		posy=500
		vidas-=1
		perder(vidas)
		#print ("perdiste")

	elif posx == posxa3 and posy == posya3:
		posx=500
		posy=500
		vidas=-1
		perder(vidas)
		#print ("perdiste")

	contador = Fuente.render("Tiempo :" +str(Tiempo)+" seg.",0,(250,250,250))
	ventana.blit(contador,(0,550))
	pygame.display.update()    