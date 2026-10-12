class Persona:
    
    # __init__ inizializzazione
    
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    
    def saluta(self):
        print(f"Ciao, sono {self.nome}, e ho {self.eta} anni")