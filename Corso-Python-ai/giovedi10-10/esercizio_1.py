
class contoBancario:
    
    def __init__(self, nome_titolare, saldo):
        
        self.__nome = nome_titolare
        self.__saldo = saldo
        
    def get_nome(self):
            return self.__nome
        
    def set_nome(self, nome_nuovo):
            
        if len(nome_nuovo) < 0 :
            print("sei un pippo")
        else:
            self.__nome = nome_nuovo
            
            
            
    def get_saldo(self):
            return self.__saldo
        
    def set_saldo(nuovo_saldo):
        
        saldo = nuovo_saldo
    
    def deposita(self, importo_da_aggiugere):
        
        importo = self.get_saldo()
        
        if importo>=0:
            
            importo = importo + importo_da_aggiugere
            return f"nuovo importo {importo}"
        
        else:
            
            return "saldo negativo"
        
    def preleva(self, importo_da_prelevare):
        
        importo = self.get_saldo()
        
        if importo_da_prelevare>importo:
            
            return "saldo insufficiente"
        else:
            
            importo = importo - importo_da_prelevare
            
            return f"nuovo saldo {importo}"
        
        
c1 = contoBancario("mario" ,1000)

print(c1.get_nome())

print(c1.deposita(1000))

print(c1.preleva(10000))