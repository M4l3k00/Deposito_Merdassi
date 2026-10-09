nomi = []
codici = []
risultati = []  

def registrazione(nome, codice):
    
    
    if nome and codice:
        nome = nome
        codice = codice
        
        nomi.append(nome)
        codici.append(codice)
        print("registrazione ok")
        return True
    
    
    else:
        nome = ""
        codice = ""
        print("registrazione ko")
        return False



def login(nome, codice):
    
    if nome in nomi and codice in codici and nomi.index(nome) == codici.index(codice):
        
        print("accesso effettuato ")
        return True
    else:
        print("accesso negato ")
        
        return False


con = True

while con:
    print("\n--- MENU A ---")
    print("1. Registrazione")
    print("2. Login")
    print("3. Esci")
    
    
    scelta = int(input("Dammi la tua scelta: "))
    
    match scelta:
        case 1:
            print("registrati")
            nome = input("dammi il nome per la registrazione: ")
            codice = input("dammi il codice per la registrazione: ")
            registrazione(nome, codice)


        case 2:
            nome = input("fammi il nome per il login: ")
            codice = input("dammi il codice per il login: ")
            

            
            if login(nome, codice):
                in_sessione = True
                
                
                
                
                while in_sessione:
                    print("menu operazioni")
                    print("1. somma")
                    print("2.sottrazione")
                    print("3. visualizza Risultati")
                    print("4. esci")
                    
                 
                        
                    scelta_op = int(input("Scegli un'operazione: "))
                    

                    match scelta_op:
                        case 1:
                            num1 = int(input("inserisci il primo numero: "))
                            num2 = int(input("inserisci il secondo numero: "))
                            res = num1 + num2
                            risultati.append(res)
                            print("risultato della somma: ", res)

                        case 2:
                            num1 = float(input("Inserisci il primo numero: "))
                            num2 = float(input("Inserisci il secondo numero: "))
                            res = num1 - num2
                            
                            risultati.append(res)
                            print("risultato della somma: ", res)
                            
                        case 3:
                            print(risultati)

                        case 4:
                            print("logout effettuato.")
                            in_sessione = False

                        case _:
                            print("Scelta non valida no menu operazioni!")

        case 3:
            
            con = False

        case _:
            print("Opzione non valida nel menu principale!")