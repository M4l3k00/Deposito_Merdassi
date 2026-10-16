import random as r
from datetime import date


class Elettrodomestico:
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str):
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = None
        self.__guasto = guasto
       
        self.setAnnoAcquisto(anno_acquisto)

    def getMarca(self) -> str:
        return self.__marca

    def setMarca(self, marca: str):
        self.__marca = marca

    def getModello(self) -> str:
        return self.__modello

    def setModello(self, modello: str):
        self.__modello = modello

    def getAnnoAcquisto(self) -> int:
        return self.__anno_acquisto

    def setAnnoAcquisto(self, anno_acquisto: int):
        if anno_acquisto > date.today().year:
            raise ValueError("L'anno di acquisto non può essere nel futuro")
        self.__anno_acquisto = anno_acquisto

    def getGuasto(self) -> str:
        return self.__guasto

    def setGuasto(self, guasto: str):
        self.__guasto = guasto

    def __str__(self) -> str:
        return (
            "---DESCRIZIONE ELETTRODOMESTICO---\n"
            f"Marca: {self.__marca}\n"
            f"Modello: {self.__modello}\n"
            f"Anno acquisto: {self.__anno_acquisto}\n"
            f"Guasto: {self.__guasto}"
        )

    def stima_costo_base(self) -> float:
       
        return r.randint(50, 100)


class Lavatrice(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto,
                 capacita_kg: int, giri_centrifuga: int):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.capacita_kg = capacita_kg
        self.giri_centrifuga = giri_centrifuga

    def stima_costo_base(self) -> float:
        return r.randint(2, 6) * self.capacita_kg


class Frigorifero(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto,
                 litri: int, ha_freezer: bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.litri = litri
        self.ha_freezer = ha_freezer

    def stima_costo_base(self) -> float:
        if self.ha_freezer and self.litri > 50:
            return r.randint(1, 10) * self.litri + 50
        elif self.litri > 50:
            return r.randint(1, 10) * self.litri
        elif self.ha_freezer:
            return r.randint(1, 10) + 5
        else:
            return r.randint(1, 10)


class Forno(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto,
                 tipo_alimentazione: str, ha_ventilato: bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.tipo_alimentazione = tipo_alimentazione
        self.ha_ventilato = ha_ventilato
        
        
        
    def stima_costo_base(self) -> float:
        if self.tipo_alimentazione.lower() == "gas":
            costo_diagnosi = r.randint(60, 120)
        else:  # elettrico
            costo_diagnosi = r.randint(40, 90)

        if self.ha_ventilato:
            costo_diagnosi += 30

        return costo_diagnosi
   







class TicketRiparazione:
    STATI_VALIDI = ["Aperto", "In lavorazione", "Chiuso", "Annullato"]

    def __init__(self, id_ticket: int, elettrodomestico: Elettrodomestico):
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico
        self.__stato = "Aperto"
        self.__note = []

    def getId_ticket(self) -> int:
        return self.__id_ticket

    def getElettrodomestico(self) -> Elettrodomestico:
        return self.__elettrodomestico

    def getStato(self) -> str:
        return self.__stato

    def get_note(self) -> list:
        return self.__note

    def setStato(self, nuovo_stato: str):
        if nuovo_stato in self.STATI_VALIDI:
            self.__stato = nuovo_stato
        else:
            raise ValueError(f"Stato non valido. Scegli tra: {self.STATI_VALIDI}")

    def setElettrodomestico(self, elettrodomestico: Elettrodomestico):
        self.__elettrodomestico = elettrodomestico

    def aggiungi_nota(self, nota: str):
        if nota.strip():
            self.__note.append(nota)

    def calcola_preventivo(self, *costi_voci_extra) -> float:
        totale = self.__elettrodomestico.stima_costo_base()
        for costo_voce in costi_voci_extra:
            totale += costo_voce
        return totale


class Officina:
    def __init__(self, nome: str):
        self.nome = nome
        self.tickets = []

    def aggiungi_ticket(self, ticket: TicketRiparazione):
        self.tickets.append(ticket)
        print("Ticket aggiunto alla lista\n")

    def chiudi_ticket(self, id_ticket: int):
        for t in self.tickets:
            if t.getId_ticket() == id_ticket:
                t.setStato("Chiuso")
                print("Ticket chiuso!\n")
                return
        print("Ticket non trovato.\n")


    def stampa_tickets_aperti(self):
        print(f"--- TICKETS APERTI {self.nome} ---")
        for t in self.tickets:
            if t.getStato() == "Aperto":
                e = t.getElettrodomestico()
                print(f"ID: {t.getId_ticket()} | Elettrodomestico: "
                      f"{e.getMarca()} {e.getModello()} | Stato: {t.getStato()}")

    def totale_preventivi(self) -> float:
        somma = 0
        for t in self.tickets:
            somma += t.calcola_preventivo()
        return somma
    
    def statistiche_per_tipo(self):
        n_lavatrici = 0
        n_frigoriferi = 0
        n_forni = 0

        for t in self.tickets:
            e = t.getElettrodomestico()

            if isinstance(e, Lavatrice):
                n_lavatrici += 1
            elif isinstance(e, Frigorifero):
                n_frigoriferi += 1
            elif isinstance(e, Forno):
                n_forni += 1

        print(f"--- STATISTICHE {self.nome} ---")
        print(f"Numero di lavatrici in riparazione: {n_lavatrici}")
        print(f"Numero di frigoriferi in riparazione: {n_frigoriferi}")
        print(f"Numero di forni in riparazione: {n_forni}")


if __name__ == "__main__":
    officina = Officina("Officina Rossi")

    lav = Lavatrice("Bosch", "Serie 6", 2020, "Non centrifuga", 8, 1400)
    fri = Frigorifero("Samsung", "RB38", 2019, "Non raffredda", 300, True)
    forno = Forno("Electrolux", "EOB", 2018, "Resistenza guasta", "Elettrico", True)

    for i, apparecchio in enumerate([lav, fri, forno], start=1):
        officina.aggiungi_ticket(TicketRiparazione(i, apparecchio))

    officina.stampa_tickets_aperti()
    officina.chiudi_ticket(2)
    officina.stampa_tickets_aperti()
    print(f"Totale preventivi: {officina.totale_preventivi()}")
    
    
    
    
    