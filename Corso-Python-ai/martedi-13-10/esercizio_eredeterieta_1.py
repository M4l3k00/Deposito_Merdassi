class Animale:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
    def fai_suono():
        print("suono generico di un animale\n")
        

class Lenone(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        
        
    def fai_suono(self):
        print("il leone rugge")
        
class Uccello(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        
        
    def fai_suono(self):
        print("l'uccello fischia")
        
    
class Toro(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        
        
    def fai_suono(self):
        print("il toro mugge")
        
           
lenone1 = Lenone("scarface", 10)
uccello1 = Uccello("mimi", 1)
toro1 = Toro("toretto", 2)

lenone1.fai_suono()

uccello1.fai_suono()

toro1.fai_suono()
    