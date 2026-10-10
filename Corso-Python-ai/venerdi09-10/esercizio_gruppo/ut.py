import random as r

lista_username = []
lista_password = []

def calcolatrice(n1,op,n2):
    
    if op == "+":
        return n1+n2
    
    elif op == "-":
        return n1-n2
    
    elif op == "*":
        return n1*n2
    
    elif (op == "/") or (op == ":"):
        
        if n2 == 0:
            return "non puoi dividere per 0"
        
        return n1/n2 
    
    elif op == "^":
        return n1**n2
    
    elif op == "%":
        return n1%n2
    
    else:
        return "operazione non valida"  
    
    
def regi(username, pas, rpas):
    
    if pas != rpas:
        
        return "le password non coincidono"
    
    #username == "" or pas == "" or rpas == ""
    
    #conferma
    elif not username or not pas or not rpas:
        
        return "tutti i campo sono obbligatori"
    
    elif len(pas)<3:
        return "password troppo corta"
    
    lista_username.append(username)
    lista_password.append(pas)
    return "registrazione completata"    


def login(username, pas):
    
    if username in lista_username and pas in lista_password and lista_username.index(username) == lista_password.index(pas):
        
        return f"benvenuto {username} accesso effettuato\n"
    else:
        return "credenziali errate"
    
    
    
def indovina_numero(n):
           
           x = r.randint(1,10)
           print("indovina il numero da 1 a 10\n")
           
           while n!= x:
               print("tenta di nuovo: ")
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
            


#print(calcolatrice(3,"+",2))


   
