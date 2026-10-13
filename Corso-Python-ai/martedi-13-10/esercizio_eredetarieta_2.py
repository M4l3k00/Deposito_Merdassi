class Prodotto:
    def __init__(self, nome,costo_produzione, prezzo_vendita):
        
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        
        
    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        return profitto
    
    
class Elettronica(Prodotto):
     def __init__(self, nome, costo_produzione, prezzo_vendita, tipo_garanzia):
         super().__init__(nome, costo_produzione, prezzo_vendita)
         self.tipo_garanzia = tipo_garanzia
         
         
class Abbigliamento(Prodotto):
     def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
         super().__init__(nome, costo_produzione, prezzo_vendita)
         self.materiale = materiale
         
         
class Fabbrica:
    def __init__(self):
      
        self.inventario = {}

    def aggiungi_prodotto(self, nome, costo_produzione, prezzo_vendita, quantita):
      
        if nome in self.inventario:
            self.inventario[nome]["quantita"] += quantita
        
        else:
            
            self.inventario[nome] = {
                "costo_produzione": costo_produzione,
                "prezzo_vendita": prezzo_vendita,
                "quantita": quantita
            }
            
        print(f"prodotto '{nome}' aggiunto  qt e totale: {self.inventario[nome]['quantita']}")


    def vendi_prodotto(self, nome, quantita):
            
        if nome not in self.inventario:
            print("prodotto non trovato")
            

        prodotto = self.inventario[nome]

        if prodotto["quantita"] < quantita:
            print(f"quantita insufficiente'. disponibili: {prodotto['quantita']}.")
            

        
        prodotto["quantita"] -= quantita

        
        profitto_u= prodotto["prezzo_vendita"] - prodotto["costo_produzione"]
        profitto_totale = profitto_u * quantita

        print(f"venduti {quantita}  di '{nome}'.")
        print(f"Profitto: {profitto_totale}")

    def resi_prodotto(self, nome, quantita):
        
        if nome in self.inventario:
            self.inventario[nome]["quantita"] += quantita
            print("reso registrato")
        else:
            print("prodotto non esiste")

fabbrica = Fabbrica()
#nome, costo_produzione, prezzo_vendita, quantita
fabbrica.aggiungi_prodotto("quaderno", 0.50, 1.5 ,10)            
fabbrica.aggiungi_prodotto("penna", 0.50, 1, 15)    
fabbrica.aggiungi_prodotto("gomma", 0.20, 1, 20)    

print(fabbrica.inventario)



fabbrica.vendi_prodotto("penna", 10)