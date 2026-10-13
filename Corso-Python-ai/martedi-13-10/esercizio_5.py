

class Convertitore:
    
    @staticmethod
    def  euro_in_dollari(euro):
        dollari = euro * 1.08
        return dollari
    
    @staticmethod
    def km_in_miglia(km):
        miglia = km * 0.62
        return miglia
    

print(Convertitore.euro_in_dollari(10))

print(Convertitore.km_in_miglia(10))



class Animale:
    numero_animali = 0
    
    def __init__(self, nome, specie):
        
        self.nome = nome
        self.specie = specie
        Animale.numero_animali +=1
        
        
    @classmethod
    def quanti_animali(cls):
        return "numero istanze create: ", cls.numero_animali
    
    


cane = Animale("pippo", "chiwawa")

ucello = Animale("ala nera", "rondine")


print(Animale.quanti_animali())



