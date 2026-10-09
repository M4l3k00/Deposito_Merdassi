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
    
    
    
    
    


#print(calcolatrice(3,"+",2))


   
