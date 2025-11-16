import random as rd
class Personaje:
    def __init__ (self,dado,vida,daño,puntuacion):
        self.vida = 100
        self.daño = 5
        self.puntuacion = 0
        self.dado = 0
    def Atacar(self,daño,vida_enem):
        dado = rd.randint(1,5)
        match dado:
            case 1:
                daño = 5
            case 2:
                daño = daño*2
            case 3:
                daño = daño*3
            case 4:
                daño = daño*4
            case 5:
                daño = daño*5
        vida_enem= vida_enem-daño
    def estado(self,vida,daño,puntuacion):
        print(f"tu estado es: vida:{self.vida} tu Daño base es: {self.daño} tu puntacion es: {self.puntuacion}") 
    
class Vampiro(Personaje):
    def __init__(self,vida,daño):
        super().__init__(vida,daño,dado)
        self.vida = 40
        self.daño = 6
    def Atacar(self):
        super().Atacar
        
    
        
        
        
        