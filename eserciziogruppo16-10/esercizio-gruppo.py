# 1. CLASSE PADRE
class Ticket:
    # Metodo costruttore per creare un nuovo ticket con attributi fortemente privati (__)
    def __init__(self, id_ticket: int, oggetto: str, testo: str, tipologia_ticket: str, stato: str):
        self.__id_ticket = id_ticket                # Salva l'ID univoco del ticket
        self.__oggetto = oggetto                    # Salva l'oggetto/titolo del ticket
        self.__testo = testo                        # Salva la descrizione del problema
        self.__tipologia_ticket = tipologia_ticket  # Salva l'urgenza (bassa, media, alta)
        self.__stato = stato                        # Salva lo stato (aperto, chiuso, ecc.)

    # --- GETTER E SETTER PER L'INCAPSULAMENTO ---
    def get_id_ticket(self) -> int:
        return self.__id_ticket                    # Restituisce l'ID del ticket

    def get_oggetto(self) -> str:
        return self.__oggetto                      # Restituisce l'oggetto del ticket

    def set_oggetto(self, oggetto: str):
        self.__oggetto = oggetto                    # Modifica l'oggetto del ticket

    def get_testo(self) -> str:
        return self.__testo                        # Restituisce il testo del ticket

    def set_testo(self, testo: str):
        self.__testo = testo                        # Modifica il testo del ticket

    def get_tipologia_ticket(self) -> str:
        return self.__tipologia_ticket              # Restituisce il livello di urgenza

    def set_tipologia_ticket(self, tipologia: str):
        self.__tipologia_ticket = tipologia         # Modifica il livello di urgenza

    def get_stato(self) -> str:
        return self.__stato                         # Restituisce lo stato attuale

    def set_stato(self, stato: str):
        self.__stato = stato                        # Modifica lo stato del ticket

    # Metodo speciale per formattare la stampa delle informazioni del ticket
    def __str__(self) -> str:
        return (
            "---DETTAGLI TICKET---\n"
            f"ID: {self.__id_ticket}\n"
            f"Oggetto: {self.__oggetto}\n"
            f"Urgenza: {self.__tipologia_ticket}\n"
            f"Stato: {self.__stato}\n"
            f"Testo: {self.__testo}\n"
        )



# 2. GERARCHIA UTENTI
# Classe base che rappresenta l'Utente Standard
class Utente:
    # Costruttore che salva il nome dell'utente
    def __init__(self, nome: str):
        self._nome = nome                          # Attributo protetto per il nome

    # Getter per ottenere il nome dell'utente
    def get_nome(self) -> str:
        return self._nome                           # Restituisce il nome dell'utente

    # Operazione: crea un nuovo ticket e lo aggiunge al sistema
    def crea_ticket(self, sistema, id_ticket: int, oggetto: str, testo: str, urgenza: str):
        nuovo_ticket = Ticket(id_ticket, oggetto, testo, urgenza, "aperto")  # Istanzia l'oggetto Ticket
        sistema.aggiungi_ticket(nuovo_ticket)       # Aggiunge il ticket al sistema
        print("Utente", self._nome, "ha creato il Ticket #", id_ticket)

    # Operazione: mostra i ticket aperti nel sistema
    def visualizza_ticket(self, sistema):
        print("--- TICKET APERTI ---")
        sistema.stampa_ticket_aperti() # Richiama la stampa dei ticket aperti

    # Metodo: mostra il ruolo dell'utente standard
    def mostra_ruolo(self):
        print("Ruolo: UTENTE STANDARD")


# Classe derivata Admin che eredita da Utente
class Admin(Utente):
    # Costruttore dell'amministratore
    def __init__(self, nome: str):
        super().__init__(nome) # Richiama il costruttore della classe padre Utente

    # sovrascrive il metodo mostra_ruolo per l'Admin
    def mostra_ruolo(self):
        print("Ruolo: AMMINISTRATORE")

    # Operazione: modifica un ticket esistente cercando per ID
    def modifica_ticket(self, sistema, id_ticket: int, nuovo_oggetto: str, nuovo_testo: str):
        ticket = sistema.cerca_ticket(id_ticket)    # Cerca il ticket nel sistema
        if ticket != None:
            ticket.set_oggetto(nuovo_oggetto)       # Aggiorna l'oggetto
            ticket.set_testo(nuovo_testo)           # Aggiorna il testo
            print("Admin", self._nome, "ha modificato il Ticket #", id_ticket)
        else:
            print("Ticket non trovato!")

    # Operazione: rimuove definitivamente un ticket per ID
    def elimina_ticket(self, sistema, id_ticket: int):
        sistema.rimuovi_ticket(id_ticket)# Rimuove il ticket dal sistema

    # Risolve/chiude un ticket e lo sposta nella lista dei chiusi
    def risolvi_ticket(self, sistema, id_ticket: int, nuovo_stato: str):
        sistema.chiudi_e_sposta_ticket(id_ticket, nuovo_stato) # Sposta il ticket tra i chiusi



# 3. CLASSE SISTEMA GESTIONALE

class SistemaGestionale:
    # Costruttore che crea le due liste per i ticket aperti e chiusi
    def __init__(self):
        self.ticket_aperti = []  # Lista per salvare i ticket aperti
        self.ticket_chiusi = []  # Lista per salvare i ticket chiusi

    # Aggiunge un ticket alla lista dei ticket aperti
    def aggiungi_ticket(self, ticket: Ticket):
        self.ticket_aperti.append(ticket)# Inserisce il ticket nella lista

    # Stampa l'elenco dei ticket aperti
    def stampa_ticket_aperti(self):
        if len(self.ticket_aperti) == 0:  # Se la lista dei ticket aperti è vuota
            print("Nessun ticket aperto.")
        else:
            for t in self.ticket_aperti:  # Scorre ciascun ticket aperto
                print(t) # Stampa il ticket usando __str__

    # Stampa l'elenco dei ticket chiusi
    def stampa_ticket_chiusi(self):
        print("--- TICKET CHIUSI ---")
        if len(self.ticket_chiusi) == 0: # Se la lista dei ticket chiusi è vuota
            print("Nessun ticket chiuso.")
        else:
            for t in self.ticket_chiusi: # Scorre ciascun ticket chiuso
                print(t)  # Stampa il ticket usando __str__

    # Cerca un ticket per ID tra quelli aperti
    def cerca_ticket(self, id_ticket: int):
        for t in self.ticket_aperti:  # Scorre tutti i ticket aperti
            if t.get_id_ticket() == id_ticket:  # Se l'ID corrisponde
                return t  # Restituisce l'oggetto ticket
        return None # Restituisce None se non lo trova

    # Rimuove un ticket dalla lista dei ticket aperti
    def rimuovi_ticket(self, id_ticket: int):
        ticket = self.cerca_ticket(id_ticket) # Cerca il ticket da rimuovere
        if ticket != None:
            self.ticket_aperti.remove(ticket) # Cancella il ticket dalla lista
            print("Ticket #", id_ticket, "eliminato!")
        else:
            print("Ticket non trovato!")

    # Cambia lo stato del ticket e lo sposta nella lista dei chiusi
    def chiudi_e_sposta_ticket(self, id_ticket: int, nuovo_stato: str):
        ticket = self.cerca_ticket(id_ticket)  # Cerca il ticket tra quelli aperti
        if ticket != None:
            ticket.set_stato(nuovo_stato) # Modifica lo stato dell'oggetto
            self.ticket_aperti.remove(ticket) # Lo elimina dalla lista dei ticket aperti
            self.ticket_chiusi.append(ticket) # Lo aggiunge alla lista dei ticket chiusi
            print("Ticket #", id_ticket, "spostato nei chiusi con stato:", nuovo_stato)
        else:
            print("Ticket non trovato!")



# ESECUZIONE DEL PROGRAMMA

# 1. Istanziazione del sistema e creazione degli utenti
sistema = SistemaGestionale()  # Crea il sistema gestionale
utente1 = Utente("Maccarone") # Crea l'utente standard Maccarone
admin1 = Admin("Fresella") # Crea l'amministratore Fresella

# Mostra i ruoli degli utenti
utente1.mostra_ruolo() # Stampa il ruolo dell'Utente
admin1.mostra_ruolo() # Stampa il ruolo dell'Admin

# 2.L'utente crea due ticket
utente1.crea_ticket(sistema, 1, "Stampante rotta", "Non si accende", "alta")
utente1.crea_ticket(sistema, 2, "Mouse difettoso", "Tasto rotto", "bassa")

# 3. L'utente visualizza i ticket aperti
utente1.visualizza_ticket(sistema)

# 4. L'Admin modifica il ticket 1
admin1.modifica_ticket(sistema, 1, "Stampante guasta", "Foglio incastrato")

# 5. L'Admin chiude il ticket 1 e lo sposta nei chiusi
admin1.risolvi_ticket(sistema, 1, "chiuso")

# 6. L'Admin elimina il ticket 2
admin1.elimina_ticket(sistema, 2)

# 7. Stampa della situazione finale delle due liste
print("--- SITUAZIONE FINALE ---")
sistema.stampa_ticket_aperti() # Stampa i ticket rimasti aperti
sistema.stampa_ticket_chiusi() # Stampa i ticket archiviati/chiusi