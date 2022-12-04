"""Modulo usado para definir la ejecucion principal en la cual se inicializa la libreria pygame, la
ventana donde se despliegan los elementos visuales y de funcionalidad y el ciclo While donde se llaman
todas las funciones creadas en los diferentes modulos.

Se definien las imagenes de pantallas de juego.

Al ejecutarse presenta el juego.

Se requieren los modulos "pygame", "Datos", "MovimientoPacman", "cerezas" y "funciones".

"""
import pygame, sys
import Datos as D
import MovimientoPacman as mp
import cerezas as cr
import funciones as f

pygame.init() #Inicializar los modulos
  
#Ventana
ventana = pygame.display.set_mode((D.tamaño_pantalla)) #Ventana 
pantalla_inicio = pygame.transform.scale(pygame.image.load("img\inicio.jpg"),(D.tamaño_pantalla))
gameover = pygame.image.load("cerezas1/game_over.jpg")
netxlevel = pygame.image.load("img\signivel.jpeg")
win = pygame.image.load("img\ganar.jpeg")
pygame.display.set_caption("Pacman") #Nombre visible de la superficie
mapa = pygame.image.load("img\level1.jpeg") # Enlace de la imagen al terminal
color_m = D.cafe
mapa = pygame.transform.scale(mapa,(D.tamaño_pantalla))


#Bucle de juego
while True:    
    f.time.tick(60)

    #Pantalla de inicio de juego
    f.pantalla_in(ventana,pantalla_inicio)
     
    if f.cont != 3 and f.inicio:
        #El juego inicia en el nivel 0

        #Cuando se cambvia de nivel, se reinician las coordenadas y las condiciones de todos los elementos en la pantalla
        if f.level == 1 and f.condicion:
            mapa = pygame.image.load("img\level2.jpeg")
            mapa = pygame.transform.scale(pygame.image.load("img\level2.jpeg"),(D.tamaño_pantalla))
            f.cond_level2()
            #Se declaran otra vez los objetos de la clase Rect que contienen las imagenes de los personajes para resetear las posiciones
            

        #Inicia el ultimo nivel, se reinician las posiciones y condiciones de todos los elementos   
        elif f.level == 2 and f.condicion == False:
            mapa = pygame.image.load("img\level3.jpeg")
            mapa = pygame.transform.scale(pygame.image.load("img\level3.jpeg"),(D.tamaño_pantalla))
            f.cond_level3()
        
        #Se colocan en la ventana las imagenes del fondo y los personajes
        f.colocar_img(ventana,mapa)

        segundos = pygame.time.get_ticks()/3000 #Preguntar a David
        cr.puntos(f.puntos,ventana) #Preguntar a David
        
        f.mon_f(ventana) #Monedas normales (funcionamiento y las dibuja)
        f.mons_f(ventana,D.pacR,segundos) #Monedas especiales (funcionamiento y las dibuja)
        f.cerezasf(D.pacR,ventana,segundos) #
        f.poderes(ventana,segundos,D.pacR) #Poderes de cada nivel
        f.cambio_estado_fantasmas(segundos) #Maneja el cambio de estado de los fantasmas al comer las monedad especiales
        f.poner_muros(ventana,D.pacR) #Dibuja y maneja el funcionamiento de los muros
        f.vidas(ventana) #Maneja las vidas de pacman
           
    elif f.cont == 3: #Se activa al perder todas las vidas para indicar que el juego termino
        ventana.fill(D.negro)
        gameover = pygame.transform.scale(pygame.image.load("img\gameover.jpeg"),(D.tamaño_pantalla))
        ventana.blit(gameover, (0, 0))
        pygame.display.flip()

    if f.level > 2: #Se activa si se superaron los 3 niveles para indicar que se gano el juego
        D.pacR = pygame.Rect(D.posPX, D.posPY, D.anchoP, D.altoP)
        ventana.fill(D.negro)
        win = pygame.transform.scale(pygame.image.load("img\ganar.jpeg"),(D.tamaño_pantalla))
        ventana.blit(win, (0, 0))
        pygame.display.flip()
        

    f.movimiento_fantasma() #Maneja el funcionamiento del movimiento de los fantasmas
    
    for evento in pygame.event.get(): # Mirar si se cierra la ventana
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        mp.movement(evento, D.pacR) #controla el movimiento
 
    pygame.display.update() #Si no se cierra la ventana se actualiza
    
    
