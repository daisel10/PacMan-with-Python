"""Modulo que contiene la clase Poder, referente a los poderes del juego que determinan los puntos"""
import pygame

class Poder:
    """Clase usada como representacion de poderes
        Atributos
        --------------
        fotos_poder : list
        Incluye las imagenes de los poderes

        poderes : list
        Incluye las imagenes de los caragadas al terminal con la escala correcta 
        y los recatangulos respectivos en la posicion de las imagenes
     """
    def __init__(self):
        """    Inicializador de la clase Cere
         Funcionamiento
         ------------
         Mediante un ciclo for, se añaden al atributo self.poderes las imagenes cargadas al terminal
         y se crean los rectangulos centrados en la poscicion requerida mediante la funcion pygame.get_rect()
         """
        
        self.fotos_poder = ["img\speed.png",
                          "img\congelar.png", "img\melt.png"]
        self.poderes = []

        for i in range(3):
            x = pygame.transform.scale(
                (pygame.image.load(self.fotos_poder[i])), (80, 80))

            z = x.get_rect(center=(310, 310))
            self.poderes.append((x, z))

        
        
