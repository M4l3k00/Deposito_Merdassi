import random
 #random
'''
def indovina(n , x):
     
     if n == x:
         print("hai indovinato il numero: ")
         
         return  True
     else:
         if n > x:
             print("il numero che hai inserito è maggiore")
         else:
             print("il numero che hai inserito è minore")
         return False


uscire = 0  
x = random.randint(1, 10)
while uscire == 0:
    
    
    n = int(input("prova ad indovinare il numero: "))
    
    if indovina(n,x):
        uscire = 1
    else:
        uscire = int(input("vuoi uscire dal gioco 1 si 0 no: "))
        
     '''   
# esercizio 2


def fibonacci(f):
    lf = []
    n1 = 0
    n2 = 1
    
    while(len(lf) < f):
        lf.append(n1)
        somma = n1 + n2
        
        n1 = n2
        n2 = somma
      
    print(lf)
    
    
    
f = int(input("dammi un numero: "))
fibonacci(f)