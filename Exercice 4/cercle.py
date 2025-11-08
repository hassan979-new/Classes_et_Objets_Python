import math

class Cercle :
    def __init__(self,rayon : float):
        self.__rayon = rayon

    @property
    def rayon(self) :
        return self.__rayon

    @rayon.setter
    def rayon(self, rayon : float) :
        if rayon <= 0 :
            raise ValueError("Le rayon doit etre strictement positif")
        self.__rayon = rayon

    @property
    def perimetre(self) :
        return 2*math.pi*self.__rayon
    
    @property
    def surface(self) :
        return math.pi * math.pow(self.__rayon,2)
    