
class Punto:
    
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
        
    def muovi(self,dx,dy):
        
        self.x = dx
        self.y = dy
        
        
    def distanza_da_origine(self):
        
        if self.x >= 0:
            dx = self.x-(2*self.x)
        else:
            dx = self.x = self.x-(2*self.x)
        if self.y >= 0: 
            dy = self.y-(2*self.y)
        else:
            dy = self.y+(2*self.y)
            
            
        return f"distanza dall'origine per il punto x {dx}, distanza dall'origine per il punto y {dy} "
                 
        
    
'''   
p1 = Punto(5,5)

dx = int(input("dammi la nuova x :"))
dy = int(input("dammi la nuova y :"))

p1.muovi(dx,dy) 
print(p1.x, p1.y)

print(p1.distanza_da_origine())

print(p1.x, p1.y)
'''
       
class Libro:
    def __init__(self, titolo: str, autore: str, pagine: int):
        
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    
    def descrizione(self):
        
        return f"autore: {self.autore}, titolo: {self.titolo}, pagine: {self.pagine}"
    
    
autore = input("dammi l'autore del libro: ")
titolo = input("titolo libro: ")
pagine = int(input("il numero delle pagine: "))


p1 = Libro(titolo, autore, pagine)

print(p1.descrizione())
    
qt = int(input(" inserisci il numero dei libri che vuoi creare "))

lista_libri = []

while len(lista_libri)<qt:
    
   autore = input("dammi l'autore del libro: ")
   titolo = input("titolo libro: ")
   pagine = int(input("il numero delle pagine: "))
   
   p = Libro(titolo, autore, pagine)
   
   lista_libri.append(p)
        
        
        
 
        
for i in lista_libri:
    
    i = Libro(autore, titolo, pagine)
    
    print(i.descrizione())
   
    
          