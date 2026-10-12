class Automobile:
    numero_ruote = 4
    def __init__(self, marca: str, modello: str):
        self.marca = marca
        self.modello = modello
    
    def stampaInfo(self):
        print(self.marca, " ", self.modello, self.numero_ruote)
        
        
a1 = Automobile("fiat", "panda")
a1.stampaInfo()


class Calcolatrice:
    
    @staticmethod #inidipendente dalla classe e non modifica dati non ha bisogno del self
    def somma(a,b):
        return a+b
    
risultato = Calcolatrice.somma(5,3)

print(risultato)



class Contatore:
    numero_istanza = 0
    
    def __init__(self):
        Contatore.numero_istanza += 1
    
    @classmethod
    def mostra_numero_istanza(cls):
        print(f"sono stati creati {cls.numero_istanza} oggetti")
        
c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanza()