lista_username = []

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

    return "registrazione completata"    


#print(calcolatrice(3,"+",2))
   
