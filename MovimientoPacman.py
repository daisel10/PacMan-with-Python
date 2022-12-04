"""Modulo usado para definir el movimiento del personaje interactivo Pacman 
mediante la funcion movement.Tambien, se define la limitacion del movimiento
mediante la colision con los muros."""
import pygame 
import Datos as D
import muros as m



def movement(evento, pacR):
    """
        Cambia la posicion del rectangulo e imagen de Pacman.

         Parametros
        ----------
        Obligatorios.

        evento : objeto de pygame.event.get()
            Dato de la cola de posibles eventos 
        pacR : objeto de pygame.Rect()
            Rectangulo de pygame

        Funcionamiento
        ------------
        Al recibir el evento de presionar tecla, detectar que tecla fue presionada,
        segun esta suma a la posicion del rectangulo y la imagen la velocidad. 

        La imagen de pacman varia segun la direccion del movimiento.

        Mediante el metodo colliderect() se anula la velocidad al colisionar 
        con un elemento de la lista laberinto.
        """
    if pacR.x>623:
            pacR.x=-D.anchoP+5
    if pacR.x<-D.anchoP:
        pacR.x=600
    #MOVIMIENTO PACMAN KEYDOWN
    
    if evento.type == pygame.KEYDOWN:# detecta si se esta tocando alguna tecla
        if evento.key == pygame.K_a:
            D.pacman = D.pacman3
            D.velocidadPacmanX = -D.velocidad
        elif evento.key == pygame.K_d:
            D.pacman = D.pacman1
            D.velocidadPacmanX = D.velocidad
        #moverse de arriba abajo
        elif evento.type == pygame.KEYDOWN:# detecta si se esta tocando alguna tecla
            if evento.key == pygame.K_w:
                D.pacman = D.pacman4
                D.velocidadPacmanY = -D.velocidad
            elif evento.key == pygame.K_s:
                D.pacman = D.pacman2
                D.velocidadPacmanY = D.velocidad
                    
        #MOVIMIENTO PACMAN KEYUP
    elif evento.type == pygame.KEYUP: #detecta si NO se esta tocando ninguna tecla
        if evento.key == pygame.K_a:
            D.velocidadPacmanX = 0
        elif evento.key == pygame.K_d:
            D.velocidadPacmanX = 0
        elif evento.type == pygame.KEYUP:#detecta si NO se esta tocando ninguna tecla
            if evento.key == pygame.K_w:
                D.velocidadPacmanY = 0
            elif evento.key == pygame.K_s:
                D.velocidadPacmanY = 0

    pacR.x += D.velocidadPacmanX
    pacR.y += D.velocidadPacmanY

    for lista in m.laberinto:
        for muro in lista:
           if pacR.colliderect(muro):
               pacR.x -= D.velocidadPacmanX
               pacR.y -= D.velocidadPacmanY

    for muro in m.bordes:
        if pacR.colliderect(muro):
            pacR.x -= D.velocidadPacmanX
            pacR.y -= D.velocidadPacmanY

    pygame.display.update()