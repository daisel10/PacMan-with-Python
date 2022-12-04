"""Modulo usado para definir el movimiento predeterminado de los fantasmas.
   
   Funciones:
   move_horizontal()
   move_vertical()
   """

velx = 1
vely = 1
margen_error = 10

def move_horizontal(fantasma, muro_izq, muro_der):
    """
        Cambia la posicion del rectangulo e imagen de del fantasma.

         Parametros
        ----------
        Obligatorios.

        fantasma : objeto de pygame.Rect()
            Rectangulo correspondiente al fantasma
        muro : objeto de pygame.Rect()
            Elemento de la lista muro con el que va a chocar el fantasma

        Funcionamiento
        ------------
        Se le suma la velocidad en x al fantasma hasta que este colisiona con
        el muro, entonces se invierte la direccion cambiando el signo de la velocidad
        que se le suma
        """
    global velx

    fantasma.x += velx
    if fantasma.colliderect(muro_izq):
        if abs(muro_izq.right - fantasma.left) < margen_error:
            velx *= -1
    if fantasma.colliderect(muro_der):
        if abs(muro_der.left - fantasma.right) < margen_error:
            velx *= -1

def move_vertical(fantasma, muro_top, muro_abajo):
    """
        Cambia la posicion del rectangulo e imagen de del fantasma.

         Parametros
        ----------
        Obligatorios.

        fantasma : objeto de pygame.Rect()
            Rectangulo correspondiente al fantasma
        muro : objeto de pygame.Rect()
            Elemento de la lista muro con el que va a chocar el fantasma

        Funcionamiento
        ------------
        Se le suma la velocidad en y al fantasma hasta que este colisiona con
        el muro, entonces se invierte la direccion cambiando el signo de la velocidad
        que se le suma
        """
    global vely
    
    fantasma.y += vely
    if fantasma.colliderect(muro_abajo):
        if abs(muro_abajo.top - fantasma.bottom) < margen_error:
            vely *= -1
    if fantasma.colliderect(muro_top):
        if abs(muro_top.bottom - fantasma.top) < margen_error:
            vely *= -1


            
            


