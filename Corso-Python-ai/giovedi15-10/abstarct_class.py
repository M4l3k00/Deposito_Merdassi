from abc import ABC, abstractmethod

class Impiegato(ABC):
    def __init__(self, nome, cognome, stipendio_base):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base
        
        
    @abstractmethod
    def calcola_stipendio(self):
        pass
    
    
class ImpiegatoFisso(Impiegato):
    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)
        
        
    def calcola_stipendio(self):
        
        
        return self.stipendio_base
             
class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_base, provvigioni):
        super().__init__(nome, cognome, stipendio_base)
        self.provvigioni = provvigioni
        
        
  
    def calcola_stipendio(self):
        stipendio_totale = self.stipendio_base + self.provvigioni
        return stipendio_totale
    


imF = ImpiegatoFisso("mario", "rossi", 1800)

print(imF.calcola_stipendio())



imPr = ImpiegatoAProvvigione("luigi", "verdi", 1500, 95)

print(imPr.calcola_stipendio())