
class Prodotto:
    def __init__(self, nome, qt, prezzo):
        self.__nome = nome
        self.__qt = qt
        self.__prezzo = prezzo

    
    def get_nome(self):
        return self.__nome

    def get_qt(self):
        return self.__qt

    def get_prezzo(self):
        return self.__prezzo

    
    
    
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_qt(self, qt):
        self.__qt = qt

    def set_prezzo(self, prezzo):
        self.__prezzo = prezzo





class Fabrrica:

    def __init__(self, nome_fabbrica):
        self.nome_fabbrica = nome_fabbrica
        self.lista_prodotti = []
        self.lista_quantita = []
        self.lista_prezzi = []

    def aggiungi_prodotto(self, prodotto):
        self.lista_prodotti.append(prodotto.get_nome())
        self.lista_quantita.append(prodotto.get_qt())
        self.lista_prezzi.append(prodotto.get_prezzo())

    def cerca_proddotto(self, prodotto):

        if prodotto in self.lista_prodotti:

            indice = self.lista_prodotti.index(prodotto)

            print("nome prodotto:", prodotto,
                  "quantita:", self.lista_quantita[indice],
                  "prezzo:", self.lista_prezzi[indice])

            return True
        else:
            print("prodotto non trovato")
            return False

    def visualizza_produzione(self):

        for i in range(len(self.lista_prodotti)):

            print("nome prodotto:", self.lista_prodotti[i],
                  "quantita:", self.lista_quantita[i],
                  "prezzo:", self.lista_prezzi[i])

    def modifica_quantita(self, prodotto):
        if self.cerca_proddotto(prodotto):

            indice = self.lista_prodotti.index(prodotto)
            qt = int(input("inserisci la nuova quantita: "))
            self.lista_quantita[indice] = qt

    def rimuovi_prodotto(self, prodotto):
        if self.cerca_proddotto(prodotto):
            indice = self.lista_prodotti.index(prodotto)
            self.lista_prodotti.pop(indice)
            self.lista_quantita.pop(indice)
            self.lista_prezzi.pop(indice)

    def calcola_totale_prezzi(self):
        totale = 0

        for i in range(len(self.lista_prezzi)):
            totale += self.lista_prezzi[i] * self.lista_quantita[i]

        return totale
    
    

fabbrica = Fabrrica("fabbrica 1")

menu = True

while menu:

    print("===================================================================================================================\n")
    print("===================================================================================================================\n")
    print("===================================================================================================================\n")

    scelta = int(input(
        
        "1 crea prodotto e aggiungilo\n"
        "2 visualizzazione dei prodotti\n"
        "3 cerca prodotto\n"
        "4 modifica quantita\n"
        "5 rimuovi prodotto\n"
        "6 calcola totale prezzi\n"
        "7 esci\n"
        "dammi la scelta: \n"
    ))

    match scelta:

        case 1:
            nome_prodotto = input("dammi il nome del prodotto: ")
            qt = int(input("dammi la quantita del prodotto: "))
            prezzo = float(input("dammi il prezzo del prodotto: "))

            p = Prodotto(nome_prodotto, qt, prezzo)
            fabbrica.aggiungi_prodotto(p)

        case 2:
            fabbrica.visualizza_produzione()

        case 3:
            nome_prodotto = input("dammi il nome del prodotto: ")
            fabbrica.cerca_proddotto(nome_prodotto)

        case 4:
            nome_prodotto = input("dammi il nome del prodotto: ")
            fabbrica.modifica_quantita(nome_prodotto)

        case 5:
            nome_prodotto = input("dammi il nome del prodotto: ")
            fabbrica.rimuovi_prodotto(nome_prodotto)

        case 6:
            print(fabbrica.calcola_totale_prezzi())

        case 7:
            print("ciao")
            menu = False
