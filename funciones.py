"""Modulo encargado de definir las funciones que se usan en el ciclo While de la
ejecucion principal

Funciones:

pantalla_in()
cond_level2()
cond_level3()
colocar_img()
poner_muros()
mon_f()
mons_f()
cerezasf()
poderes()
cambio_estado_fantasmas()
vidas()
movimiento_fantasma()
"""

import pygame
import Datos as D
import muros 
import monedas as m
import MovimientoFantasma2 as mf
import cerezas as cr
import poderes as po
D.posPX, posPY = 310, 375
#Variables y condicionales iniciales
game = True
inicio = False # Condiconal que nos permite acceder a la ventana de inico y luego a la del juego 
switch = False # Condicional que nos permite que lista se va a usar en monedas normales 
switch2 = False # Condicion que nos permite saber que lista se va a usar en las monedas especiales
color_muros = D.cafe
color_monedas = D.dorado
color_monedaspp = m.gris
condicion = True # Condicional que nos hace que se pase de nivel y que se reinicien los valores solo unna vez 
poder_congelar = True
sengundos_velocidad = 0

puntos = 0
time = pygame.time.Clock() #iniciador de tiempo en el juego
power = po.Poder() #creacion de la clase donde van a estar los poderes
cerezas = cr.Cere() # creacion de la clase imagen y rectangulo de las cerezas 
level = 0 # nivel en el que esta
cereza1 = cerezas.fruits[0] # llamado de la de la tupla de las variahbles donde esta la imagen y el rectangulo de cereza

power1 = power.poderes[0] # llamado las imagenes y los rectangulos de poderes
power_inmortal= True # Condicional que activa el poder de transpasar los muros 
renderizar_power = True # Condicional que para mostrar imagen de poder
renderizar_cereza = True # Condicional para mostrar imagen de cereza
cont = 0 # condador de coliciones con fantasmas
sengundos_inmortal = 0 # Donde se va a guardar el tiempo de inicalizacion del poder muros
valor_de_estado = True # Condicional que nos permite saber si esta actiba la colicion con los fantasmas y que color tiene el fantasma
inicio = False
next_nivel = False

#Funciones del juego
def pantalla_in(ventana, pantalla_inicio):
    """
        Añade a la pantalla la imagen de pantalla inicial del juego y lo inicia posteriormente

         Parametros
        ----------
        Obligatorios.

        ventana : objeto de pygame.display()
            Ventana donde se colocan todos los aspectos visuales
        pantalla_inicio : objeto de pygame.image()
            Imagen que cubre la pantalla

        Funcionamiento
        ------------
        Si se esta en condicion de inicio y no se cambia la variable de next_level,
        la cual varia al completar las condiciones de pasar el nivel, se añade a la
        pantalla la imagen de inicio y se detecta si se presiona alguna tecla para
        romper el condicional inicial con el cambio de la variable "inicio"
        """
    global inicio, next_nivel
    if inicio == False and next_nivel == False:
        segundos = 0
        ventana.blit(pantalla_inicio, (0, 0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                inicio = True #Al tocar cualquier tecla inicia el juego

    if next_nivel and inicio == False:
        ventana.blit(pantalla_inicio, (0, 0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    inicio = True
                    next_nivel = False #Al tocar cualquier tecla inicia el juego
                    
def mon_f(ventana):
    """
        Añade las monedas, recoge las monedas, cambia los puntos y mediante el cambio
        de puntos activa la condicion del paso de nivel cuando se recogen todas las monedas

         Parametros
        ----------
        Obligatorios.

        ventana : objeto de pygame.display()
            Ventana donde se colocan todos los aspectos visuales en este caso las monedas

        Funcionamiento
        ------------
        Si la variable "switch" es verdadera se escoge la primera lista de monedas para
        iterar su colocacion en el primer nivel, si "switch" es falsa se escoge la segunda 
        lista para el otro nivel.
        La funcion recoger monedas va sumando puntos y quitandolas de la lista cuando pacman 
        colisiona con ellas al ser la longitud de la lista 0 cambia de nivel.

        """
    global level,switch,lista_m,puntos, color_monedas
    if switch: 
            lista_m =  m.monedas_list2 #Asigna la lista de monedas que luego se va a dibujar 
            if len(m.monedas_list2) == 0: #Si la lista se vuelve vacia (se recogen todas las monedas), pasa al siguiente nivel 
                level = level+1
                switch = False

    elif switch == False:
        lista_m = m.monedas_normales
        if len(m.monedas_normales) == 0:#Si la lista se vuelve vacia (se recogen todas las monedas), pasa al siguiente nivel
            level = level + 1
            switch = True
            
    for moneda in lista_m: #Recoje las monedas cuando pacman pasa por encima, el valor de lista_m depende del condicional switch
        a = m.recojer_moneda(D.pacR, moneda, switch)
        puntos += a
        pygame.draw.rect(ventana, color_monedas, moneda) #Dibuja todas las monedas en pantalla

def colocar_img(ventana,mapa):
    """
        Añade a la pantalla la imagen de mapa y los personajes definidos en el modulo
        Datos

         Parametros
        ----------
        Obligatorios.

        ventana : objeto de pygame.display()
            Ventana donde se colocan todos los aspectos visuales
        mapa : objeto de pygame.image()
            Imagen que cubre la pantalla en el nivel

        Funcionamiento
        ------------
        Usa la funcion pygame.display.blit() para poner en pantalla las 
        imagenes de el mapa, pacman y los monstruos en las posiciones 
        establecidas
        """
    ventana.blit(mapa, (0, 0))
    ventana.blit(D.pacman, (D.pacR.x, D.pacR.y))
    ventana.blit(D.m_rojo, (D.m_rojoR.x, D.m_rojoR.y))
    ventana.blit(D.m_naranja, (D.m_naranjaR.x, D.m_naranjaR.y))
    ventana.blit(D.m_rosa, (D.m_rosadoR.x, D.m_rosadoR.y))
    ventana.blit(D.m_azul, (D.m_azulR.x, D.m_azulR.y))

def mons_f(ventana,pacR,segundos):
    """
        Añade las monedas especiales, recoge las monedas especiales, cambia los puntos, activa la
        condicion del paso de nivel cuando se recogen todas las monedas y cambia el estado de los
        fantasmas

         Parametros
        ----------
        Obligatorios.

        ventana : objeto de pygame.display()
            Ventana donde se colocan todos los aspectos visuales en este caso las monedas
        pacR : objeto de pygame.Rect()
            Rectangulo en la posicion de pacman
        segundos : int
            Referente del cronometro de pygame
        Funcionamiento
        ------------
        Si la variable "switch2" es verdadera se escoge la primera lista de monedas para
        iterar su colocacion en el primer nivel, si "switch2" es falsa y se cambia el nivel
        se escoge la segunda lista para el otro nivel.
        La funcion recoger monedas va sumando puntos y quitandolas, ademas al colisionar con
        ellas cambia la imagen de los fantasmas y la variable "valor_de_estado" a False para 
        cambiar su estado.

        """
    global level, switch2, lista_m, coli, inicio_de_estado, valor_de_estado, puntos, color_monedaspp
    mppp = m.monedas_especiales
    if switch2 and level == 1:
            mppp = m.monedas_especiales2
            if len(m.monedas_especiales2) == 0: #Si la lista esta vacia, cambia el condicional switch2 
                switch2 = False

    elif switch2 == False and level == 0 or level == 2:
        mppp = m.monedas_especiales
        if len(m.monedas_especiales) == 0:
            switch2 = True
    
    for monedapp in mppp:
        if m.recojer_monedapp(pacR, monedapp, switch2): #Permite que pacman recoja las monedas
            valor_de_estado = False #Condicional que detemrina si los fantasmas estan normales o azules
            coli = False
            inicio_de_estado = segundos
            puntos = puntos + 20
            D.m_rojo = pygame.transform.scale((pygame.image.load("img/tile072.png")), D.tamaño_personajes)
            D.m_naranja = pygame.transform.scale((pygame.image.load("img/tile072.png")), D.tamaño_personajes)
            D.m_rosa = pygame.transform.scale((pygame.image.load("img/tile072.png")), D.tamaño_personajes)
            D.m_azul = pygame.transform.scale((pygame.image.load("img/tile072.png")), D.tamaño_personajes)
        pygame.draw.rect(ventana, color_monedaspp, monedapp)

def cerezasf(pacR,ventana,segundos):
    """
        Añade las frutas de puntaje en los niveles y define su recoleccion.

         Parametros
        ----------
        Obligatorios.

        ventana : objeto de pygame.display()
            Ventana donde se colocan todos los aspectos visuales en este caso las monedas
        pacR : objeto de pygame.Rect()
            Rectangulo en la posicion de pacman
        segundos : int
            Referente del cronometro de pygame
        Funcionamiento
        ------------
        Cuando segundos>5 añade la imagen y el rectangulo a la pantalla, los cuales se
        encuentran en una tupla, al colisionar con pacman se deshabilita el condicional
        que renderiza la cereza y suma puntos

        """

    global renderizar_cereza,  puntos, cereza1
    if renderizar_cereza and segundos > 5:
        ventana.blit(cereza1[0], (310, 505))
        if pacR.colliderect(cereza1[1]):
            renderizar_cereza = False
            puntos = 50 + puntos

def poner_muros(ventana,pacR):
    """
        Coloca en pantalla los rectangulos que conforman el laberinto y limita el
        movimiento de pacman a traves de ellos.
         Parametros
        ----------
        Obligatorios.

        ventana : objeto de pygame.display()
            Ventana donde se colocan todos los aspectos visuales en este caso las monedas
        pacR : objeto de pygame.Rect()
            Rectangulo en la posicion de pacman
        Funcionamiento
        ------------
        Itera las listas de muros y cuando se detecta una colision mediante colliderect()
        se anula la velocided de pacman.
        Itera las listas de muros y mediante la funcion pygame.display.blit() los añade a 
        la pantalla.

        """
    global color_muros
    for lista in muros.laberinto:
        for muro in lista:
            if pacR.colliderect(muro) :
                pacR.x -= D.velocidadPacmanX
                pacR.y -= D.velocidadPacmanY
            pygame.draw.rect(ventana, color_muros, muro)  # dibuja los muros
    for borde in muros.bordes:
        pygame.draw.rect(ventana, color_muros, borde)
        if pacR.colliderect(borde):
            pacR.x -= D.velocidadPacmanX
            pacR.y -= D.velocidadPacmanY
        
    for borde in muros.bordes:
        pygame.draw.rect(ventana, color_muros, borde)

    for muro in muros.especiales:
        pygame.draw.rect(ventana, D.dorado, muro)    

def poderes(ventana,segundos,pacR):
    """
        Define los 3 poderes usados alrededor de los niveles del juego: velocidad, congelar fantasmas e
        inmortalidad

         Parametros
        ----------
        Obligatorios.

        ventana : objeto de pygame.display()
            Ventana donde se colocan todos los aspectos visuales en este caso las monedas
        pacR : objeto de pygame.Rect()
            Rectangulo en la posicion de pacman
        segundos : int
            Referente del cronometro de pygame
        Funcionamiento
        ------------
        Poderes :Dependiendo del numero 0,1,2 de la variable "Level" se añade a la pantalla la imagen
        del poder hallado en la lista "power1" y cuando pacman colisiona con ella se activa la condicion
        correspondiente por 5 segundos.
        
        Velocidad:cambia su velocidad a 15 por 5 segundos. 

        Poder congelar: Deshabilita la funcion movimiento fantasma. 

        Poder inmortal: Deshabilita la funcion vidas.
        """
    global level, renderizar_power, sengundos_velocidad, power1,poder_congelar, sengundos_muros
    if level == 0:
        ### poder de velocidad
        if renderizar_power and segundos > 1:
            ventana.blit(power1[0], (285, 285))
            if pacR.colliderect(power1[1]):
                D.velocidad = 15
                sengundos_velocidad = segundos
                renderizar_power = False
        elif renderizar_power  == False and sengundos_velocidad+5 < segundos: 
            D.velocidad = 5

    elif level == 1:
    ### poder de congelar
        if renderizar_power and segundos > 1:
            ventana.blit(power1[0], (285, 285))
                
            if pacR.colliderect(power1[1]):
                    
                sengundos_velocidad = segundos
                poder_congelar = False
                renderizar_power = False
        elif renderizar_power  == False and sengundos_velocidad+5 < segundos: 
            poder_congelar = True
                

    elif level == 2:
    ### poder de muros
        if renderizar_power and segundos > 1:
            ventana.blit(power1[0], (285, 285))
            if pacR.colliderect(power1[1]):
                power_inmortal = False
                sengundos_muros = segundos
                renderizar_power= False
        elif renderizar_power == False and sengundos_muros +5 < segundos:
            power_inmortal = True

def movimiento_fantasma():
    """
        Llama las funciones de movimiento vertical y horizontal de los fantasmas y 
        la anula en el caso de detectar el poder congelar.
         Parametros
        ----------
        ------------
        Si no se activa el poder congelar, aplica la funcion move_horizontal y
        move_vertical a los fantasmas y sus rectangulos.

        """
    if level == 1 and poder_congelar == False:
        pass

    else:
        mf.move_horizontal(D.m_rojoR, muros.m1, muros.m2)
        mf.move_horizontal(D.m_naranjaR, muros.m20, muros.m2)
        mf.move_vertical(D.m_rosadoR, muros.m4, muros.k15)
        mf.move_vertical(D.m_azulR, muros.m5, muros.k16)   

def vidas(ventana):
    """
        Añade los corazones en representacion de las vidas, las cuales se usan para
        definir en el main el fin del juego.

         Parametros
        ----------
        Obligatorios.

        ventana : objeto de pygame.display()
            Ventana donde se colocan todos los aspectos visuales en este caso las monedas
        
        Funcionamiento
        ------------
        Mientras no este activado el poder inmortal o el estado de monedas especiales se 
        verifica si pacman colisiona con un fantasma, si lo hace se suma 1 al contador lo
        cual cambia la condicion de tener las vidas en pantalla, disminuyendo en 1.

        """
    global cont
    for i in D.list_fanta:
        if cont == 0 and valor_de_estado and D.pacR.colliderect(i) and power_inmortal:
            cont += 1
            D.pacR = pygame.Rect(D.posPX, D.posPY, D.anchoP, D.altoP) 
            
        elif cont == 1 and valor_de_estado and D.pacR.colliderect(i) and power_inmortal:
            cont += 1
            D.pacR = pygame.Rect(D.posPX, D.posPY, D.anchoP, D.altoP)
       
        elif cont == 2 and valor_de_estado and D.pacR.colliderect(i) and power_inmortal:
            cont +=1
        
        if inicio and cont == 0 or cont == 1 or cont == 2:
            ventana.blit(cr.vidas, (650, 620))
        if inicio and cont == 0 or cont == 1:
            ventana.blit(cr.vidas, (725, 620))
        if inicio and cont == 0:
            ventana.blit(cr.vidas, (800, 620))

def cond_level2():
    """
        Devuelve los valores iniciales a las variables afectadas en el nivel 1

         Parametros
        ----------
        Funcionamiento
        ------------
        Define nuevamente los valores de la variables globales
        """
    global color_muros, color_monedas, color_monedaspp, renderizar_cereza, renderizar_power, poder_muros, poder_congelar, cont, sengundos_muros, valor_de_estado, game, next_nivel, poder, power1, cereza1, condicion, inicio
    color_muros = D.azul
    color_monedas = D.dorado
    color_monedaspp = D.naranja
    renderizar_cereza = True
    renderizar_power = True
    poder_muros= True
    poder_congelar = True
    cont = 0
    sengundos_muros = 0
    valor_de_estado = True
    game = True
    next_nivel = True
    poder = False
    power1= power.poderes[1]
    cereza1 = cerezas.fruits[1]
    condicion = False
    inicio = False
    D.pacR = pygame.Rect(D.posPX, D.posPY, D.anchoP, D.altoP)
    D.m_rojo = pygame.transform.scale(
        (pygame.image.load("img/m_rojo1.png")), D.tamaño_personajes)
    D.m_naranja = pygame.transform.scale(
        (pygame.image.load("img/m_naranja.png")), D.tamaño_personajes)
    D.m_rosa = pygame.transform.scale(
        (pygame.image.load("img/m_rosa.png")), D.tamaño_personajes)
    D.m_azul = pygame.transform.scale(
        (pygame.image.load("img/m_azul.png")), D.tamaño_personajes)

def cond_level3():
    """
        Devuelve los valores iniciales a las variables afectadas en el nivel 2

         Parametros
        ----------
        Funcionamiento
        ------------
        Define nuevamente los valores de la variables globales
        """
    global color_muros, color_monedas, color_monedaspp, renderizar_cereza, renderizar_power, poder_muros, poder_congelar, cont, sengundos_muros, valor_de_estado, game, next_nivel, poder, power1, cereza1, condicion, inicio
    color_muros = D.gris
    color_monedas = D.negro
    color_monedaspp = D.blanco
    renderizar_cereza = True
    renderizar_power = True
    cont = 0
    valor_de_estado = True
    game = True
    next_nivel = True
    poder = False
    power1 = power.poderes[2]
    cereza1 = cerezas.fruits[2]
    condicion = True
    inicio = False
    D.pacR = pygame.Rect(D.posPX, D.posPY, D.anchoP, D.altoP)
    D.m_rojo = pygame.transform.scale(
        (pygame.image.load("img/m_rojo1.png")), D.tamaño_personajes)
    D.m_naranja = pygame.transform.scale(
        (pygame.image.load("img/m_naranja.png")), D.tamaño_personajes)
    D.m_rosa = pygame.transform.scale(
        (pygame.image.load("img/m_rosa.png")), D.tamaño_personajes)
    D.m_azul = pygame.transform.scale(
        (pygame.image.load("img/m_azul.png")), D.tamaño_personajes)

def cambio_estado_fantasmas(segundos):
    """
        Devuelve a la estetica original a los fantasmas depues de su cambio de estado.

         Parametros
        ----------
        Obligatorios.

        segundos : int
            Recibe el valor del cronometro

        Funcionamiento
        ------------
        Detecta si ya han pasado 5 segundos despues de la colision de pacman con una
        moneda especial y actualiza las variables de las imagenes de los fantasmas a
        los archivos originales.

        """
    global valor_de_estado
    
    if valor_de_estado == False:
        segundos_de_estado = inicio_de_estado + 5

        if segundos > segundos_de_estado:
            D.m_rojo = pygame.transform.scale((pygame.image.load("img/m_rojo1.png")), D.tamaño_personajes)
            D.m_naranja = pygame.transform.scale((pygame.image.load("img/m_naranja.png")), D.tamaño_personajes)
            D.m_rosa = pygame.transform.scale((pygame.image.load("img/m_rosa.png")), D.tamaño_personajes)
            D.m_azul = pygame.transform.scale((pygame.image.load("img/m_azul.png")), D.tamaño_personajes)
            
            valor_de_estado = True

