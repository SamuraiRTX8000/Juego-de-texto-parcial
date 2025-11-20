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
        super().__init__(vida=120,daño=5,puntuacion=0,dado=0)
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
        
class Asesino(Personaje):
    def _int_(self):
        super()._init_(vida=30, daño=4, puntuacion=0, dado=0)
    def ataca(self,enemigo):

        dado=rd.randint (1,6)
        if dado >= 4:
            daño = (self.daño*dado)*3

        else:
            
            daño =(self.daño *dado)*2
        enemigo.vida -= daño
        print (f"hiciste {daño} puntos de daño ")
    def estado(self):
        super().estado()
        
#criaturas amigables y eventos
class amigable ():
    def _init_(self,vida,puntuacion):
        self.vida = vida
        self.puntuacion= puntuacion
    def evento_amigable(self,jugador):
        print(f"Te encontraste a un anciano al que se le cayeron sus monedas ")
        decision = int(input("¿Quieres ayudarlo? oprime 1 o 2  |1 ayudarlo| |2 robarle| "))
        if decision==1:
            print(f"El anciano te ha dado una bendicion por tus buenas acciones")
            print("te has fortalecido (+10 puntos de vida y  +1 puntos de daño)")
            jugador.vida += 10
            jugador.daño +=1
        else:
            print("El anciano te maldice por tus malas acciones")
            jugador.vida -= 5
            jugador.daño -=1
            print("la maldicion te debilita (pierdes 5 puntos de vida y 1 punto de daño)")


niveles = 0
#asi se elije el personaje para que pueda pelear        
eleccion = int(input("Elije tu personaje |1 vampiro(menos vida pero puede roba vida del enemigo con cada ataque) |2 asesino menos vida pero mayor ataque"))
if eleccion == 1:
   jugador = Vampiro()
else:
    juagador = Asesino()

print("Entraste al bosque magico buscando derrotar al mago oscuro")
while jugador.vida>0:
    niveles += 1
    if niveles == 1:
        print("Te encontraste al orco malvado")
        enemigo = Orco()
        while jugador.vida > 0 or enemigo.vida>0:
            decision = int(input("elije una accion |1. atacar | |2. curarse"))
            if decision == 1:
                jugador.atacar(enemigo)
                enemigo.atacar(jugador)
                jugador.estado()
            else:
                jugador.curar()
                enemigo.atacar(jugador)
                jugador.estado()
            if jugador.vida<=0:
                print("| PERDISTE |")
            elif enemigo.vida<=0:
                print("mataste al enemigo sigues avanzando por el bosque")
                
    print("Te encontraste el general de esqueleto")
    enemigo = Esqueleto()
    if niveles==3:
        while jugador.vida > 0 or enemigo.vida>0:
            decision = int(input("elije una accion |1. atacar | |2. curarse"))
            if decision == 1:
                jugador.atacar(enemigo)
                enemigo.atacar(jugador)
                jugador.estado()
            else:
                jugador.curar()
                enemigo.atacar(jugador)
                jugador.estado()
            if jugador.vida<=0:
                print("| PERDISTE |")
            elif enemigo.vida<=0:
                print("mataste al general esqueleto sigues avanzando por el bosque buscando la forma de vengar a tu padre")
                
    