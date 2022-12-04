"""Modulo usado para definir las variables que se utilizan a traves del programa y cargar
    al terminal las imagenes de los personajes.
    Se definen dimensiones de pantalla y de los personajes, velocidad de Pacman y colores
    en sistema RGB"""
import pygame
#Dimensiones
tamaño_pantalla = ancho,alto = (900,700)
tamaño_monedas = ancho_m,alto_m = (10,10)

#Posiciones
posPX, posPY = 310, 375  # posiciones en pantalla
posMRX ,posMRY = 80, 113
posMnaranjaX , posMnaranjaY = 310, 635
posMrosaX ,posMrosaY = 150, 30
posMazulX ,posMazuklY = 468, 30

#Velocidades
velocidadPacmanX = 0
velocidadPacmanY = 0
velocidad = 5

#Colores
negro = (1,1,1)
blanco = (255,255,255)
dorado = (250, 189, 0)
cafe = (142, 91, 40)
naranja = (255, 128, 0)
gris = (96, 96, 96)
azul = (0, 0, 139)


#Datos de los personajes 
anchoP= 30
altoP= 30
tamaño_personajes = anchoP,altoP

pacman = pygame.transform.scale((pygame.image.load("img/imagen_pacman.png")),tamaño_personajes)

pacman1 = pygame.transform.scale((pygame.image.load("img/imagen_pacman.png")),tamaño_personajes)

pacman2 = pygame.transform.scale((pygame.image.load("img/imagen_pacman2.png")),tamaño_personajes)

pacman3 = pygame.transform.scale((pygame.image.load("img/imagen_pacman3.png")),tamaño_personajes)

pacman4 = pygame.transform.scale((pygame.image.load("img/imagen_pacman4.png")),tamaño_personajes)

m_rojo = pygame.transform.scale((pygame.image.load("img/m_rojo1.png")), tamaño_personajes)
m_naranja = pygame.transform.scale((pygame.image.load("img/m_naranja.png")), tamaño_personajes)
m_rosa = pygame.transform.scale((pygame.image.load("img/m_rosa.png")), tamaño_personajes)
m_azul = pygame.transform.scale((pygame.image.load("img/m_azul.png")), tamaño_personajes)

#Crear los rectangulos que contienen las imagenes de los personajes
pacR = pygame.Rect(posPX, posPY, anchoP, altoP)
m_rojoR = pygame.Rect(posMRX, posMRY, anchoP, altoP)
m_naranjaR = pygame.Rect(posMRX, 635, anchoP, altoP)
m_rosadoR = pygame.Rect(150, 30, anchoP, altoP)
m_azulR = pygame.Rect(468, 30, anchoP, altoP)

list_fanta=[m_rojoR, m_naranjaR, m_rosadoR, m_azulR]



