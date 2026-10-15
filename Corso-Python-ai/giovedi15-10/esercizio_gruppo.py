from abc import ABC, abstractmethod


class VeicoloTrasporto(ABC):

  def __init__(self, targa, pesoMassimo):
    self._targa = targa  # Attributo protetto
    self._pesoMassimo = pesoMassimo  # Attributo protetto
    self._caricoAttuale = 0

  def carico(self, peso):
    if self._caricoAttuale + peso <= self._pesoMassimo:
      self._caricoAttuale += peso
      print(f"Carico effettuato sulla targa {self._targa}")
      return True
    else:
      print(f"Superata capacità massima per {self._targa}")
      return False

  def scarico(self):
    self._caricoAttuale = 0
    print(f"Veicolo {self._targa} scaricato")

  @abstractmethod
  def costo_manutenzione(self):
    pass


class Camion(VeicoloTrasporto):

  def __init__(self, targa, pesoMassimo, numero_assi):
    self.__numero_assi = numero_assi  
    super().__init__(targa, pesoMassimo)

  def getNumeroAssi(self):
    return self.__numero_assi

  def setNumeroAssi(self, numero_assi):
    self.__numero_assi = numero_assi

  def costo_manutenzione(self):
    
    costo = self.getNumeroAssi() * 100 + 1 * self._pesoMassimo
    return costo


class Furgone(VeicoloTrasporto):

  def __init__(self, targa, pesoMassimo, alimentazione):
    self.__alimentazione = alimentazione
    super().__init__(targa, pesoMassimo)

  def getAlimentazione(self):
    return self.__alimentazione

  def setAlimentazione(self, alimentazione):
    print("Non puoi cambiare l'alimentazione del veicolo")

  def costo_manutenzione(self):
    
    if self.getAlimentazione() == "elettrico":
      return 200
    else:
      return 150


class Motocarro(VeicoloTrasporto):

  def __init__(self, targa, pesoMassimo, anni_servizio):
    self.__anni_servizio = anni_servizio
    super().__init__(targa, pesoMassimo)

  def getAnniServizio(self):
    return self.__anni_servizio

  def setAnniServizio(self, anni_servizio):
    self.__anni_servizio = anni_servizio

  def costo_manutenzione(self):
    
    return self.getAnniServizio() * 50


class GestoreFlotta:

  def __init__(self, nome_flotta):
    self.nome_flotta = nome_flotta
    self.listaVeicoli = []

  def aggiungi_veicolo(self, veicolo):
    self.listaVeicoli.append(veicolo)
    
    print(f"Veicolo targa {veicolo._targa} aggiunto alla flotta")

  def rimuovi_veicolo(self, targa):
    
    for veicolo in self.listaVeicoli:
      if veicolo._targa == targa:  
        self.listaVeicoli.remove(veicolo)
        print(f"Veicolo con targa {targa} eliminato")
        return  
    print("Veicolo non trovato")

  def costo_totale_manutenzione(self):
    costo_totale = 0
    for veicolo in self.listaVeicoli:
      costo_totale += veicolo.costo_manutenzione()
    return costo_totale

  def stampa_veicoli(self):
      
      for veicolo in self.listaVeicoli:
          print("targa: ", veicolo._targa, " Peso massimo", veicolo._pesoMassimo, " Carico attuale", veicolo._caricoAttuale)
          
    