"""Modulo que contiene la clase Cere, referente a las Frutas especiales del juego que determinan los puntos
   y en la funcion puntos()" se define el contador en pantalla"""
import pygame
ancho_v= 50
alto_v = 50
tamaño_vida = ancho_v, alto_v
vidas = pygame.transform.scale((pygame.image.load("cerezas1/descarga.png")), tamaño_vida)

class Cere:
    """Clase usada como representacion de las frutas especiales 
        Atributos
        --------------
        list_cere : list
        Incluye las imagenes de las frutas

        fruits : list
        Incluye las imagenes de las frutas caragadas al terminal con la escala correcta 
        y los recatangulos respectivos en la posicion de las imagenes
     """
    def __init__(self):
        """    Inicializador de la clase Cere
         Funcionamiento
         ------------
         Mediante un ciclo for, se añaden al atributo self.fruits las imagenes cargadas al terminal
         y se crean los rectangulos centrados en la poscicion requerida mediante la funcion pygame.get_rect()
         """
        self.list_cere = ["cerezas1/tile080.png",
                        "cerezas1/tile082.png", "cerezas1/tile081.png"]
        self.fruits = []

        for i in range(3):
            x = pygame.transform.scale(
                (pygame.image.load(self.list_cere[i])), (30, 30))

            z = x.get_rect(center=(310, 505))
            self.fruits.append((x, z))



def puntos (puntos,ventana):
    """ Presenta el contador de los puntos en pantalla

         Parametros
         ----------
         Obligatorios.

         puntos : int
            variable con el puntaje a mostrar
         ventana : objeto de pygame.display()
            Superficie donde se va a localizar la imagen del contador

         Funcionamiento
         ------------
         Al recibir el puntaje saca la variables m,c,d las cuales corresponde a las milesimas, centesimas y decenas mediante
         multiplicación y division. Con el uso de los valores de la variables se determina que imagen de numero debe ser puesta en 
         pantalla"""
    ancho = 50
    alto = 50
    tamaño = ancho, alto
    m =  int(puntos*0.001)
    if m == 0:
       num = pygame.transform.scale(
            (pygame.image.load("num/tile032.png")), tamaño)
       ventana.blit(num, (650, 120))
    elif m == 1:
         num = pygame.transform.scale(
            (pygame.image.load("num/tile033.png")), tamaño)
         ventana.blit(num, (650, 120))
    elif m == 2:
        num = pygame.transform.scale(
            (pygame.image.load("num/tile034.png")), tamaño)
        ventana.blit(num, (650, 120))
    elif m == 3:
        num = pygame.transform.scale(
            (pygame.image.load("num/tile035.png")), tamaño)
        ventana.blit(num, (650, 120))
    elif m == 4:
        num = pygame.transform.scale(
            (pygame.image.load("num/tile036.png")), tamaño)
        ventana.blit(num, (650, 120))
    elif m == 5:
        num = pygame.transform.scale(
            (pygame.image.load("num/tile037.png")), tamaño)
        ventana.blit(num, (650, 120))
    elif m == 6:
        num = pygame.transform.scale(
            (pygame.image.load("num/tile038.png")), tamaño)
        ventana.blit(num, (650, 120))
    elif m == 7:
        num = pygame.transform.scale(
            (pygame.image.load("num/tile039.png")), tamaño)
        ventana.blit(num, (650, 120))
    elif m == 8:
        num = pygame.transform.scale(
            (pygame.image.load("num/tile040.png")), tamaño)
        ventana.blit(num, (650, 120))
    elif m == 9:
        num = pygame.transform.scale(
            (pygame.image.load("num/tile041.png")), tamaño)
        ventana.blit(num, (650, 120))
    ###############################################################################3
    c = int((puntos-(int(puntos*0.001)*1000))*0.01)
    
    if c == 0:
        h = pygame.transform.scale(
           (pygame.image.load("num/tile032.png")), tamaño)
        ventana.blit(h, (710, 120))
    elif c == 1:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile033.png")), tamaño)
        ventana.blit(h, (710, 120))
        
    elif c == 2:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile034.png")), tamaño)
        ventana.blit(h, (710, 120))
    elif c == 3:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile035.png")), tamaño)
        ventana.blit(h, (710, 120))
    elif c == 4:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile036.png")), tamaño)
        ventana.blit(h, (710, 120))
    elif c == 5:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile037.png")), tamaño)
        ventana.blit(h, (710, 120))
    elif c == 6:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile038.png")), tamaño)
        ventana.blit(h, (710, 120))
    elif c == 7:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile039.png")), tamaño)
        ventana.blit(h, (710, 120))
    elif c == 8:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile040.png")), tamaño)
        ventana.blit(h, (710, 120))
    elif c == 9:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile041.png")), tamaño)
        ventana.blit(h, (710, 120))
    #############################################
    d = int((puntos-int(int(int(puntos*0.001)*1000)+ (c*100)))*0.1)
    if d == 0:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile032.png")), tamaño)
        ventana.blit(h, (770, 120))
    elif d == 1:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile033.png")), tamaño)
        ventana.blit(h, (770, 120))
    elif d == 2:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile034.png")), tamaño)
        ventana.blit(h, (770, 120))
    elif d == 3:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile035.png")), tamaño)
        ventana.blit(h, (770, 120))
    elif d == 4:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile036.png")), tamaño)
        ventana.blit(h, (770, 120))
    elif d == 5:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile037.png")), tamaño)
        ventana.blit(h, (770, 120))
    elif d == 6:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile038.png")), tamaño)
        ventana.blit(h, (770, 120))
    elif d == 7:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile039.png")), tamaño)
        ventana.blit(h, (770, 120))
    elif d == 8:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile040.png")), tamaño)
        ventana.blit(h, (770, 120))
    elif d == 9:
        h = pygame.transform.scale(
            (pygame.image.load("num/tile041.png")), tamaño)
        ventana.blit(h, (770, 120))
    
    p = pygame.transform.scale(
        (pygame.image.load("num/tile032.png")), tamaño)
    ventana.blit(p, (830, 120))

