class Persona:
    
    def __init__(self, nome: str, eta: int):
        self.nome = nome
        self.eta = eta
    
    def presentazione(self):
        return f"ciao sono {self.nome}, e ho {self.eta} anni \n"
    
    
    
class Studente(Persona):
    
    def __init__(self, nome, eta, voti: list):
        super().__init__(nome, eta)   
        self.__voti = voti
        
    def get_voti(self):
        return self.__voti
    
    def presentazione(self):
        
        #voti = []
        voti = self.get_voti()
        
        somma_voti = 0
        
        for voto in voti:
            #somma_voti = voto + somma_voti
            somma_voti += voto
        
        media = somma_voti/len(voti) 
            
        return f"Ciao sono lo studente {self.nome} e la mia media è {media}"
        
            
class Professore(Persona):
    
    def __init__(self, nome, eta, materia: str):
        super().__init__(nome, eta) 
        self.__materia = materia
        
        
    def get_materia(self):
        return self.__materia
            
            
    def presentazione(self):
        materia = self.get_materia() 
        return f"ciao sono il professore {self.nome}, e insegno {materia}  \n"
    
    
    

class Scuola:
    
    def __init__(self, nome: str):
        
        self.nome = nome
        self.__lista_studenti = []
        self.__lista_professori = []
        
    def get_lista_studenti(self):
        
        return self.__lista_studenti
    
    def get_lista_professori(self):
        
        return self.__lista_professori


    def aggiungi_studente(self, studente: Studente):
        
       self.__lista_studenti.append(studente)
        
        
        
    
    
    
    def aggiungi_professore(self, professore: Professore):
        
        self.__lista_professori.append(professore)
        
        
        
prof_rossi = Professore("Mario Rossi", 45, "Matematica")

stud_luca = Studente("Luca", 16, [8, 9, 7])      
stud_marco = Studente("Marco", 17, [5, 6, 5.5])  

mia_scuola = Scuola("Liceo Scientifico ")

print(prof_rossi.presentazione())


mia_scuola.aggiungi_professore(prof_rossi)
mia_scuola.aggiungi_studente(stud_luca)
mia_scuola.aggiungi_studente(stud_marco)


print(mia_scuola.get_lista_studenti())




        
        
        
         