"""Modulo usado para definir la lista de monedas que se itera en la ejecución principal y la recoleccion de
   las mismas.
   
   Funciones:
   moneda()
   recojer_moneda()
   moneda_plus()
   recojer_monedapp()"""
import pygame

#Monedas normales
def moneda(posX, posY):
    """ Define los monedas mediante un cuadrado de tipo pygame.Rect()
             Parametros
        ----------
        Obligatorios.

        posX : int
            Posicion horizontal de la esquina superior izquierda
        posY : int
            Posicion vertical de la esquina superior izquierda
        -------
        Retorna un cuadrado

     """
    m = pygame.Rect(posX, posY, 6, 6)
    return m


#Fila 1
m1 = moneda(50,40)
m2 = moneda(80,40)
m3 = moneda(110,40)
m4 = moneda(140,40)
m5 = moneda(170,40)
m6 = moneda(200,40)
m7 = moneda(230,40)
m8 = moneda(260,40)
m9 = moneda(290,40)

m10 = moneda(355,40)
m11 = moneda(385,40)
m12 = moneda(415,40)
m13 = moneda(445,40)
m14 = moneda(475,40)
m15 = moneda(505,40)
m16 = moneda(535,40)
m17 = moneda(565,40)
m18 = moneda(595,40)

#Filas intermedias
m19 = moneda(50,70)
m20 = moneda(595,70) #Alineada con la ultima
m21 = moneda(290,70) #Alineada con la 9
m43 = moneda(355,70) #Alineada con la 10
m46 = moneda(165,70) #Antes de la 5
m48 = moneda(475,70) #Alineada con la 14

m22 = moneda(50,100)
m23 = moneda(595,100) #Alineada con la ultima
m24 = moneda(290,100) #Alineada con la 9
m44 = moneda(355,100) #Alineada con la 10
m47 = moneda(165,100) #Antes de la 5
m49 = moneda(475,100) #Alineada con la 14

#Fila 2
m25 = moneda(50,130)
m26 = moneda(80,130)
m27 = moneda(110,130)
m28 = moneda(140,130)
m29 = moneda(170,130)
m30 = moneda(200,130)
m31 = moneda(230,130)
m32 = moneda(260,130)
m33 = moneda(290,130)
m45 = moneda(320,130)

m34 = moneda(355,130)
m35 = moneda(385,130)
m36 = moneda(415,130)
m37 = moneda(445,130)
m38 = moneda(475,130)
m39 = moneda(505,130)
m40 = moneda(535,130)
m41 = moneda(565,130)
m42 = moneda(595,130)

#columnas intermedia
m50 = moneda(50,160)
m51 = moneda(165,160) #Antes de la 5
m52 = moneda(220,160)
m53 = moneda(415,160)
m54 = moneda(475,160) #Alineada con la 14
m55 = moneda(595,160) #Alineada con la ultima
m56 = moneda(50,190)
m57 = moneda(165,190) #Antes de la 5
m58 = moneda(220,190)
m59 = moneda(415,190) #Alineada con 12
m60 = moneda(475,190) #Alineada con la 14
m61 = moneda(595,190) #Alineada con la ultima

m62 = moneda(80,190)
m63= moneda(110,190)
m64 = moneda(140,190)
m65= moneda(290,190)
m66 = moneda(355,190)
m67 = moneda(385,190)
m68= moneda(415,190)
m69 = moneda(260,190)
m70 = moneda(505,190)
m71 = moneda(535,190)
m72 = moneda(565,190)

m73 = moneda(165,220) #Antes de la 5
m74 = moneda(290,220) #Alineada con la 9
m76 = moneda(355,220)
m77 = moneda(475,220)
m78 = moneda(165,260) #Antes de la 5
m79 = moneda(290,260) #Alineada con la 9
m80 = moneda(220,260)
m81 = moneda(355,260)
m82 = moneda(475,260)
m75 = moneda(260,260)
m83 = moneda(415,260)
m84 = moneda(385,260)
m85 = moneda(320,260)

m86 = moneda(165,380) #Antes de la 5
m87 = moneda(290,380) #Alineada con la 9
m88 = moneda(220,380) #La moneda que no va
m89 = moneda(355,380)
m90 = moneda(475,380)
m91 = moneda(260,380)
m92 = moneda(415,380)
m93 = moneda(385,380)
m94 = moneda(320,380)

m95 = moneda(50,320)
m96 = moneda(80,320)
m97 = moneda(110,320)
m98 = moneda(140,320)
m99 = moneda(170,320)
m100 = moneda(200,320)
m101 = moneda(230,320)



m106 = moneda(415,320)
m107 = moneda(445,320)
m108 = moneda(475,320)
m109 = moneda(505,320)
m110 = moneda(535,320)
m111 = moneda(565,320)
m112 = moneda(595,320)

m102 = moneda(165,350)
m103 = moneda(165,380)
m104 = moneda(165,410)
m105 = moneda(415,350)
m113 = moneda(415,380)
m114 = moneda(415,410)
m115 = moneda(475,350) #Alineada con la 14
m116 = moneda(475,380) #Alineada con la 14
m117 = moneda(475,410) #Alineada con la 14
m118 = moneda(230,350)
m119 = moneda(230,380)
m120 = moneda(230,410)

#Fila 1
m88 = moneda(50,450)
m121 = moneda(80,450)
m122 = moneda(110,450)
m123 = moneda(140,450)
m124 = moneda(170,450)
m125 = moneda(200,450)
m126 = moneda(230,450)
m127 = moneda(260,450)
m128 = moneda(290,450)

m129 = moneda(355,450)
m130 = moneda(385,450)
m131 = moneda(415,450)
m132 = moneda(445,450)
m133 = moneda(475,450)
m134 = moneda(505,450)
m135 = moneda(535,450)
m136 = moneda(565,450)
m137 = moneda(595,450)

m138 = moneda(50,480)  #Alineada con el 1
m139 = moneda(165,480) #Antes de la 5
m140 = moneda(290,480) #Alineada con la 9
m141 = moneda(355,480)
m142 = moneda(595,480)
m143 = moneda(475,480) #Alineada con la 14

m144 = moneda(50,510)
m145 = moneda(80,510)
m146 = moneda(102,510)

m148 = moneda(170,510)
m149 = moneda(200,510)
m150 = moneda(230,510)
m151 = moneda(260,510)
m152 = moneda(290,510)

m153 = moneda(355,510)
m154 = moneda(385,510)
m155 = moneda(415,510)
m156 = moneda(445,510)

m158 = moneda(475,510)
m159 = moneda(535,510)
m160 = moneda(565,510)
m161 = moneda(595,510)

m147 = moneda(100,540)
m157 = moneda(165,540)
m162 = moneda(230,540)
m183 = moneda(415,540)
m184 = moneda(475,540)
m185 = moneda(535,540)

m163 = moneda(50,580)
m164 = moneda(80,580)
m166 = moneda(140,580)
m167 = moneda(170,580)
m168 = moneda(110,580)
m170 = moneda(230,580)
m171 = moneda(260,580)
m172 = moneda(290,580)

m173 = moneda(355,580)
m174 = moneda(385,580)
m175 = moneda(415,580)
m177 = moneda(475,580)
m178 = moneda(505,580)
m179 = moneda(535,580)
m180 = moneda(565,580)
m181 = moneda(595,580)

m169 = moneda(50,610)
m165 = moneda(290,610) #Se va
m176 = moneda(355,610) #Se va
m182 = moneda(595,610) #Se va

m186 = moneda(50,645)
m187 = moneda(80,645)
m188 = moneda(110,645)
m189 = moneda(140,645)
m190 = moneda(170,645)
m191 = moneda(200,645)
m192 = moneda(230,645)
m193 = moneda(260,645)
m194 = moneda(290,645)

m195 = moneda(355,645)
m196 = moneda(385,645)
m197 = moneda(415,645)
m198 = moneda(445,645)
m199 = moneda(475,645)
m200 = moneda(505,645)
m201 = moneda(535,645)
m202 = moneda(565,645)
m203 = moneda(595,645)
m204 = moneda(320,645)

m205 = moneda(165,290) #Antes de la 5
m206 = moneda(230,290)
m207 = moneda(415,290)
m208 = moneda(475,290)
monedas_normales=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,
                  m23,m24,m25,m26,m27,m28,m29,m30,m31,m32,m33,m34,m35,m36,m37,m38,m39,m40,m41,m42,
                  m43,m44,m45,m46,m47,m48,m49,m50,m51,m52,m53,m54,m55,m56,m57,m58,m59,m60,m61,m62,
                  m63,m64,m65,m66,m67,m68,m69,m70,m71,m72,m73,m74,m75,m76,m77,m78,m79,m80,m81,m82,
                  m83,m84,m85,m86,m87,m88,m89,m90,m91,m92,m93,m94,m95,m96,m97,m98,m99,m100,m101,m102,
                  m103,m104,m105,m106,m107,m108,m109,m110,m111,m112,m113,m114,m115,m116,m117,m118,
                  m119,m120,m121,m122,m123,m124,m125,m126,m127,m128,m129,m130,m131,m132,m133,m134,
                  m135,m136,m137,m138,m139,m140,m141,m142,m143,m144,m145,m146,m147,m148,m149,m150,
                  m151,m152,m153,m154,m155,m156,m157,m158,m159,m160,m161,m162,m163,m164,m165,m166,
                  m167,m168,m169,m170,m171,m172,m173,m174,m175,m176,m177,m178,m179,m180,m181,m182,
                  m183,m184,m185,m186,m187,m188,m189,m190,m191,m192,m193,m194,m195,m196,m197,m198,m199,m200,
                  m201,m202,m203,m204,m205,m206,m207,m208]
monedas_list2=[]

def recojer_moneda(pacR, moneda, suit):
    """ Define la recolección de monedas normales
             Parametros
        ----------
        Obligatorios.

        pacR : objeto de pygame.Rect()
            Rectangulo de pygame
        moneda : objeto de pygame.Rect()
            elemto de la lista de monedas correspondiente

        suit : bool
            Condicional que indica que lista se va a usar en monedas normales 
    """
    import monedas as m
    a = 0
    if suit == False:
        if pacR.colliderect(moneda):
            m.monedas_list2.append(moneda)
            m.monedas_normales.remove(moneda)
            a = 9
            
    elif suit:
        if pacR.colliderect(moneda):
            m.monedas_normales.append(moneda)
            m.monedas_list2.remove(moneda)
            
            a = 9
    
    return(a)


#Monedas especiales
def moneda_plus(posX, posY):
    """ Define las monedas que cambian el estado de los fantasmas mediante un cuadrado de tipo pygame.Rect()
        
        Parametros
        ----------
        Obligatorios.

        posX : int
            Posicion horizontal de la esquina superior izquierda
        posY : int
            Posicion vertical de la esquina superior izquierda
        -------
        Retorna un cuadrado

    """
    m = pygame.Rect(posX, posY, 12, 12)
    return m

gris = (128, 128, 128)
m1 = moneda_plus(48, 65)
m2= moneda_plus(48,475)
m3= moneda_plus(595,475)
m4= moneda_plus(595,65)
monedas_especiales= [m1,m2,m3,m4]
monedas_especiales2=[]

def recojer_monedapp(pacR, monedapp, suit):
    """ Define la recolección de monedas especiales
             Parametros
        ----------
        Obligatorios.

        pacR : objeto de pygame.Rect()
            Rectangulo de pygame
        moneda : objeto de pygame.Rect()
            elemto de la lista de monedas correspondiente

        suit : bool
            Condicional que indica que lista se va a usar en monedas especiales
    """
    
    if suit == False:
        if pacR.colliderect(monedapp):
            monedas_especiales2.append(monedapp)
            monedas_especiales.remove(monedapp)
            return True

    elif suit:
        if pacR.colliderect(monedapp):
            monedas_especiales.append(monedapp)
            monedas_especiales2.remove(monedapp)
            return True
    
