import ut as ut

# --- 1. PRIMO DECORATORE: Aggiunge una cornice sopra e sotto ---
def decoratore_cornice(funzione):
    # Funzione wrapper interna che accetta qualsiasi numero di argomenti
    def wrapper(*args, **kwargs):
        # Stampa una linea superiore della cornice prima di eseguire la funzione
        print("=================================")
        # Esegue la funzione originale passando gli argomenti e salva il risultato
        risultato = funzione(*args, **kwargs)
        # Stampa una linea inferiore della cornice dopo che la funzione ha finito
        print("=================================")
        # Restituisce il risultato ottenuto dall'esecuzione della funzione
        return risultato
    # Restituisce la funzione wrapper decorata
    return wrapper

# --- 2. SECONDO DECORATORE: Aggiunge un messaggio di avviso ---
def decoratore_avviso(funzione):
    def wrapper(*args, **kwargs):
        # Stampa un messaggio di avviso prima di avviare l'azione
        print("-> [AVVISO]: Stiamo eseguendo l'azione...")
        # Esegue la funzione originale e salva il risultato
        risultato = funzione(*args, **kwargs)
        # Stampa un messaggio di avviso quando l'azione Ã¨ completata
        print("-> [AVVISO]: Azione completata!")
        return risultato
    return wrapper

# --- PROGRAMMA PRINCIPALE ---

# Chiede all'utente di inserire la scelta iniziale del menu o 'stop' per uscire
scelta = input("Scegli un numero da 1 a 6" " oppure stop: ")

# Condizione che si fermera' all'input stop dell'utente 
while scelta != "stop":

    # Scelta utente con il match
    match scelta:
        case "1": #Gestione della calcolatrice
            # Applica il decoratore della cornice alla funzione interna 'esegui'
            @decoratore_cornice
            def esegui():
                # Chiede all'utente di inserire il primo numero convertendolo in float
                n1 = float(input("Inserisci il primo numero: "))
                # Chiede all'utente di inserire l'operatore matematico desiderato
                op = input("Scegli un operatore tra +, -, *, /:, ^, % ")
                # Chiede all'utente di inserire il secondo numero convertendolo in float
                n2 = float(input("Inserisci il secondo numero: "))
                # Chiama la funzione calcolatrice dal modulo ut e ne restituisce il risultato
                print(ut.calcolatrice(n1, op, n2))
            # Esegue la funzione decorata appena definita
            esegui()
            

        case "2": #Gestione della registrazione utente
            @decoratore_cornice
            def esegui():
                # Chiede all'utente di inserire il nome utente,password e ripeti password
                # per la registrazione
                username = input("Inserisci username: ")
                pas = input("Inserisci password: ")
                rpas = input("Ripeti password: ")
                # Chiama la funzione regi dal modulo ut e ne stampa l'esito
                print(ut.regi(username, pas, rpas))
            esegui()
            

        case "3":#Gestione del login
            # Applica il decoratore di avviso alla funzione interna 'esegui'
            @decoratore_avviso
            def esegui():
                # Chiede all'utente di inserire il proprio username e password
                username = input("Inserisci username: ")
                pas = input("Inserisci password: ")
                # Chiama la funzione login dal modulo ut e ne stampa l'esito
                print(ut.login(username, pas))
            esegui()
            

        case "4": # Gestione del gioco 'indovina il numero'
            @decoratore_avviso
            def esegui():
                # Chiede all'utente di inserire un numero intero da tentare di indovinare
                n = int(input("Inserisci un numero da 1 a 10: "))
                # Chiama la funzione indovina_numero dal modulo ut e ne stampa l'esito
                print(ut.indovina_numero(n))
            esegui()

        case "5": #Gestione della funzione pari e dispari
            @decoratore_cornice
            def esegui():
                # Chiede il primo e il secondo numero intero da inserire nella lista
                n1 = int(input("Inserisci il primo numero: "))
                n2 = int(input("Inserisci il secondo numero: "))
                #Salviamo i risultati della funzione in due variabili separate
                pari, dispari = ut.pari_dispari([n1, n2])
                #Stampiamo l'elenco dei numeri pari identificati
                print("Numero pari:",pari)
                print("Numero dispari:",dispari)
            esegui()


        case "6": #somma dei numeri pari e dispari
            @ut.somma_num_pari_dispari
            def esegui():
                #n3 = int(input("Inserisci il primo numero: "))
                #n4 = int(input("Inserisci il secondo numero: "))
                listar= [1,2,3,4,5,6]
            
                return ut.somma_num_pari_dispari()
            esegui()
            
        #Interrompe il programma se l'utente digita 'stop'
        case "stop":
            print("Grazie per aver usato il programma")
            break # Esce immediatamente dal ciclo while terminando il programma

        case _: #Gestisce qualsiasi input errato inserito dall'utente
            print("hai sbagliato")
    
    #Chiede di nuovo all'utente un nuovo input all'interno del ciclo per continuare o uscire
<<<<<<< HEAD
    scelta = input("Scegli un numero da 1 a 5 oppure stop: ")




=======
    scelta = input("Scegli un numero da 1 a 5 oppure stop: ")
>>>>>>> 7f3822e22e997a3f622996adc30806aab7dee2b9
