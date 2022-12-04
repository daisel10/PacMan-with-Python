"""Modulo usado para definir la lista de muros que se itera en la ejecución principal

Funciones: muro()"""
import pygame

def muro(posX, posY, width, height):
    """ Define los muros mediante un rectangulo de tipo pygame.Rect()
             Parametros
        ----------
        Obligatorios.

        posX : int
            Posicion horizontal de la esquina superior izquierda
        posY : int
            Posicion vertical de la esquina superior izquierda
        width : int
            Ancho del rectangulo
        height : int
            Alto del rectangulo
        
        -------
        Retorna un rectangulo

    """
    m = pygame.Rect(posX, posY, width, height)
    return m

#bordes
m1 = muro(28, 24, 7, 200) #izquierdo
m7 = muro(28, 425, 7, 120) #izquierdo
m20 = muro(28, 555, 7, 120)

m2 = muro(615, 24, 7, 200) #derecho
m6 = muro(615, 425, 7, 122) #derecho
m21 = muro(615, 555, 7, 120)

m3 = muro(28, 670, 594, 7) #inferior

m4 = muro(28, 20, 282, 7) #superior 1
m5 = muro(340, 20, 282, 7) #superior 2

m11 = muro(509, 295, 114 , 7)
m8 = muro(25, 295, 114 , 7)

m9 = muro(509, 349, 114 , 7)
m10 = muro(25, 349, 114 , 7)

m13 = muro(509, 423, 113 , 7)
m12 = muro(28, 423, 108 , 7)

m14 = muro(509, 220, 113 , 7)
m15 = muro(28, 220, 108 , 7)

m16 = muro(569, 555, 50 , 7)
m18 = muro(569, 540, 50 , 7)

m17 = muro(28, 540, 50 , 7)
m19 = muro(28, 555, 50 , 7)

m22 = muro(309, 20, 7, 90) #superior al lado
m23 = muro(333, 20, 7, 90)

m24 = muro(509, 220, 7, 80)
m25 = muro(135, 220, 7, 82)

m26 = muro(509, 350, 7, 80)
m27 = muro(135, 349, 7, 81)

m28 = muro(309, 108, 31 , 7) #borde superior bajito

m29 = muro(569, 540, 7, 20) #borde laterañ interno
m30 = muro(72, 540, 7, 22)

bordes = [m1, m2, m3, m4, m5, m6, m7, m8, 
m9, m10, m11, m12, m13, m14, m15, m16,
m17, m18, m19, m20, m21, m22, m23, 
m24, m25, m26, m27, m28, m29, 
m30]

#parte interna superior
j1 = muro(247, 152, 154 , 27) #t superior
j2 = muro(504, 153, 67 , 25)
j3 = muro(504, 70, 67 , 42)
j4 = muro(376, 70, 87 , 42)
j5 = muro(77, 70, 67 , 42)
j6 = muro(184, 70, 87 , 42)
j7 = muro(77, 153, 67 , 25)
j8 = muro(208, 217, 63 , 25)
j9 = muro(377, 217, 63 , 25)
j10 = muro(183, 153, 26, 153) #lateral vertical
j11 = muro(439, 153, 26, 153)
j12 = muro(311, 153, 26, 89)

interno_sup = [j1, j2, j3, j4, 
j5, j6, j7, j8, j9, j10, j11, j12]

#parte interna inferior
k1 = muro(311, 409, 26, 89) #vertical
k2 = muro(439, 346, 26, 89)
k3 = muro(183, 346, 26, 89)
k4 = muro(183, 538, 26, 80)
k5 = muro(439, 538, 26, 80)
k6 = muro(503, 474, 26, 87)
k7 = muro(118, 474, 26, 87)
k8 = muro(311, 537, 26, 89)
k9 = muro(247, 536, 154, 27) #horizontal
k10 = muro(247, 408, 154, 27)
k11 = muro(183, 471, 89,  27)
k12 = muro(376, 471, 89, 27)
k13 = muro(503, 472, 68, 27)
k14 = muro(77, 472, 67, 27)
k15 = muro(77, 601, 196, 27)
k16 = muro(376, 601, 196, 27)

interno_inf = [k1, k2, k3, k4, k5, k6, k7,
k8, k9, k10, k11, k12, k13, k14, k15, k16]

#caja del centro
n1 = muro(251, 359, 145, 7)
n2 = muro(251, 285, 47, 7)
n3 = muro(350, 285, 47, 7)
n4 = muro(251, 290, 7, 76)
n5 = muro(390, 290, 7, 76)

caja_centro = [n1, n2, n3, n4, n5]

#muros especiales(pacman los toca y aparece dle otro lado)
e1 = muro(616, 302, 7, 47) #derecho
e2 = muro(25, 302, 7, 47)

especiales = [e1, e2]

laberinto = [interno_sup, interno_inf, caja_centro]