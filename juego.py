import random as rd
#Clase principal es para jugadores 
class Personaje:
    def __init__ (self,vida,daño,puntuacion,dado):
        self.vida = vida
        self.daño = daño
        self.puntuacion = puntuacion
        self.dado = dado
    def atacar(self,enemigo):
        dado = rd.randint(1,5)
        daño = self.daño*dado
        enemigo.vida -= daño
        print(f"hiciste {daño} puntos de daño el enemigo tiene {enemigo.vida}")
        
    def estado(self):
        print(f"tu estado es: vida: {self.vida} tu Daño base es: {self.daño} tu puntuacion es: {self.puntuacion}") 
 #Clases enemigos   
class Enemigo ():
    def __init__(self,vida,daño,puntuacion,dado):
        self.vida = vida
        self.daño=daño
        self.puntuacion=puntuacion
        self.dado=dado
    def atacar(self,jugador):
        dado = rd.randint(1,5)
        daño = self.daño*dado
        jugador.vida -= daño
        print(f"El enemigo hace {daño} puntos de daño al jugador.")

class Esqueleto(Enemigo):
    def __init__(self):
        super().__init__(vida=60, daño=4, puntuacion=0, dado=0)

    def atacar(self, jugador):
        super().atacar(jugador)
        # habilidad: 20% de probabilidad de hacer un ataque doble
        dado = rd.randint(1,5)
        daño = self.daño*dado
        if rd.randint(1, 5) == 1:
            daño *= 2
            print("¡El Esqueleto hace un ataque doble!")


class Orco(Enemigo):
    def __init__(self):
        super(). __init__(vida=100,daño=8,puntuacion=0,dado=0)
    def atacar(self, jugador):
        super().atacar(jugador)
        

class Mago(Enemigo):
    def __init__(self):
        super().__init__(vida=50,daño=5,puntuacion=0,dado=0)
    def atacar(self,jugador):

        dado = rd.randint(1,5)
        daño = self.daño*dado
        if daño==5:
            self.vida +=5
            print("EL mago recupero vida")
        jugador.vida -=daño
        print(f"El mago hizo {daño} de daño ")
                
 #Personaje jugable       
class Vampiro(Personaje):
    
    def __init__(self):
        super().__init__(vida=40,daño=6,puntuacion=0,dado=0)
    def atacar(self,enemigo):
        
        dado = rd.randint(1,5)
        daño = self.daño *dado
        self.vida += dado
        enemigo.vida -= daño
        print(f"hiciste {daño} de daño y robaste vida al contincante ahora tu vida es de {self.vida}")
       
    def estado(self):
        super().estado()
#Falta otro personaje

#asi se elije el personaje para que pueda pelear        
#eleccion = int(input("Elije tu personaje |1 vampiro(menos vida pero puede roba vida del enemigo con cada ataque) |2 Barbaro mas vida y ataque mayor"))
#if eleccion == 1:
#    #jugador = Vampiro()
    
    
        
        
        
        