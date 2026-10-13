
class UnitaMilitare:
    def __init__(self, nome:str, numero_soldati:int):
        self.nome = nome
        self.numero_soldati = numero_soldati
    
    
    def muovi(self):
        return f"l'unita{self.nome} si sta muovendo"
    
    def attacca(self):
            return f"l'unita{self.nome} sta attaccando"
        
    def ritira(self):
            return f"l'unita{self.nome} si sta ritirando"
        
    def __repr__(self):
        return f"unita: {self.nome} (Soldati: {self.numero_soldati})"
        
        
        
class Fanteria(UnitaMilitare):
    
    def __init__(self, nome, numero_soldati):
         super().__init__(nome, numero_soldati)
         
    def costruisci_trincea(self):
        return f"la fanteria {self.nome} costruisce difese temporanee"
    
class Arteglieria(UnitaMilitare):
    
    def __init__(self, nome, numero_soldati):
         super().__init__(nome, numero_soldati)
         
         
    def calibra_arteglieria(self):
        return f"l'arteglieria {self.nome} calibra i pezzi di artiglieria per la precisione."
    
class Cavalleria(UnitaMilitare):
    
    def __init__(self, nome, numero_soldati):
         super().__init__(nome, numero_soldati)
         
    def esplora_terreno(self):
        return f"la cavalleria {self.nome}  esplora l'area per raccogliere informazioni sul nemico"
    
    
class Rincognizione(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
         super().__init__(nome, numero_soldati)
         
    def esplora_terreno(self):
        return f"la rincognizione {self.nome} conduce missioni di sorveglianza "
            
class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
         super().__init__(nome, numero_soldati)
         
    def rifornisce_unita(self):
        return f"il suppporto logistico: {self.nome}  gestisce il rifornimento e la manutenzione "
    
    

class ControlloMilitare(Fanteria, Arteglieria, Cavalleria, SupportoLogistico, Rincognizione):
    
    unita_registrate_nomi = []
    unita_registrate_unita = []
    
    def __init__(self, nome, numero_soldati):
         super().__init__(nome, numero_soldati)
         
    @classmethod
    def registra_unita(cls, unita):
        if unita.nome not in cls.unita_registrate_nomi:
            cls.unita_registrate_nomi.append(unita.nome)
            cls.unita_registrate_unita.append(unita)
        
    
    def mostra_unita(self):
        
        for nome_regist in self.unita_registrate_nomi:
            print(nome_regist)
    
            
            
    def __repr__(self, nome):
         
         return f"l'unita nome {self.nome} numero unita {self.numero_soldati}"
        
    
    @classmethod
    def dettagli_unita(cls, nome):
        for unita in cls.unita_registrate_unita:
            if unita.nome == nome:
                return repr(unita)
        return f"unita'{nome}' non trovata."
    
    

f1 = Fanteria("fanteria 1", 200)
a1 = Arteglieria("arteglieria 1", 100)
c1 = Cavalleria("cavalli", 20)


ControlloMilitare.registra_unita(f1)
ControlloMilitare.registra_unita(a1)
ControlloMilitare.registra_unita(c1)


controllo = ControlloMilitare("Comnda centrale", 5)

controllo.mostra_unita()


print(ControlloMilitare.dettagli_unita("fanteria 1"))
print(f1.costruisci_trincea())

print(a1.calibra_arteglieria())

        
                    
        