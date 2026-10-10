# Importa il modulo random e lo rinomina come 'r' per poter generare numeri casuali
import random as r
# Creaiamo due liste vuote per memorizzare i nomi utente registrati e le password
lista_username = []
lista_password = []

# Definisce la funzione calcolatrice che accetta due numeri e l'operatore
def calcolatrice(n1,op,n2):
    
    # Controllo degli operatori
    if op == "+":
        return n1+n2
    
    elif op == "-":
        return n1-n2
    
    elif op == "*":
        return n1*n2
    
    # Controlla se l'operatore è la divisione (sia con lo slash che con i due punti)
    elif (op == "/") or (op == ":"):
        
        # Verifica preventiva per evitare l'errore matematico di divisione per zero
        if n2 == 0:
            return "non puoi dividere per 0"
        
        return n1/n2 
    
    # Controlla se l'operatore scelto è l'esponenziale (potenza)
    elif op == "^":
        # Restituisce il primo numero elevato alla potenza del secondo
        return n1**n2
    
    # Controlla se l'operatore scelto è il modulo (resto della divisione)
    elif op == "%":
        # Restituisce il resto della divisione tra i due numeri
        return n1%n2
    
    # Se l'operatore inserito non corrisponde a nessuno dei precedenti
    else:
        return "operazione non valida"  
    
# Definisce la funzione per registrare un nuovo utente nel sistema  
def regi(username, pas, rpas):
    
    # Controlla se la password e la password di conferma sono diverse
    if pas != rpas:
        
        return "le password non coincidono"
    
    # Controlla se uno qualsiasi dei campi di input è vuoto
    elif not username or not pas or not rpas:
        
        return "tutti i campo sono obbligatori"
    
    # Controlla se la lunghezza della password è inferiore a 3 caratteri
    elif len(pas)<3:
        return "password troppo corta"
    
    # Aggiunge il nome utente e la password registrato alla lista globale degli username e password
    lista_username.append(username)
    lista_password.append(pas)
    # Restituisce la conferma che la registrazione è andata a buon fine
    return "registrazione completata"    

# Definisce la funzione per eseguire il login verificando le credenziali
def login(username, pas):
    
    # Controlla che l'utente e la password esistano nelle liste e che si trovino esattamente allo stesso indice
    if username in lista_username and pas in lista_password and lista_username.index(username) == lista_password.index(pas):
        
        # Restituisce un messaggio di benvenuto personalizzato con il nome utente
        return f"benvenuto {username} accesso effettuato\n"
    # Se le condizioni falliscono
    else:
        return "credenziali errate"
    
    
# Definisce la funzione per indovinare un numero casuale
def indovina_numero(n):
           
           # Genera un numero intero casuale compreso tra 1 e 10 usando il modulo random
           x = r.randint(1,10)
           print("indovina il numero da 1 a 10\n")
           
           #fintanto che il numero inserito dall'utente è diverso da quello segreto
           while n!= x:
               print("tenta di nuovo: ")
               # Legge il nuovo input numerico inserito dall'utente e lo converte in intero
               n = int(input("inserisci di nuovo: "))
               
           return "hai indovinato" 
    
    #[1,4,6,7]   
#davide questa deve prendere in input una lista       
def pari_dispari(lista_numeri):
    
    lista_pari=[]
    lista_dispari=[]
    
    for n in lista_numeri:
        
        if n%2 == 0:
            lista_pari.append(n)
        else:
            lista_dispari.append(n)
            
    return f"questa è la lista dei numeri pari: {lista_dispari}, questa è la lista dei numeri pari:  {lista_dispari}"
            

# Definisce la funzione per pari e dispari
def pari_dispari(lista_numeri):
    
    # Inizializza due liste vuote per raccogliere i numeri pari e dispari
    lista_pari=[]
    lista_dispari=[]
    
    # Scorre ciclicamente ogni numero presente nella lista ricevuta in argomento
    for n in lista_numeri:
        # Controlla se il resto della divisione per 2 è zero (condizione di numero pari)
        if n%2==0:
            # Aggiunge il numero alla lista dei pari
            lista_pari.append(n)
        else:
            # Aggiunge il numero alla lista dei dispari
            lista_dispari.append(n)
    
    # Stampa i risultati all'interno della funzione
    print("Numeri pari:", lista_pari)
    print("Numeri dispari:", lista_dispari)
        


   
