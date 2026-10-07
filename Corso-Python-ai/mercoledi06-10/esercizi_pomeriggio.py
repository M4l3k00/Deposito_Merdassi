#es1
'''
lista = []
a = -1
while(a!=0):
    a = int(input("dammi un numero, 0 per chiudere il programma"))
    lista.append(a)

c = 0
somma = 0
while(c< len(lista)):
    
    somma = somma + lista[c]
    c +=1
print(somma)

'''
#es 2
'''
parola = input("dammi una parola")

for i in parola:
    print(i)
    '''
    
    
    #es3
'''
n = int(input("dammi un numero"))
s = int(input("dammi il passo"))

for i in range(0,n, s):
    
    print(i)
    '''
    
    
#es4

lista = []
print("-------------programma gestisci la mia lista-------------")

r = True

while r :
    print("cosa vuoi fare?\n 1 visualizzare la lista \n 2 aggiungere un elemento alla lista \n 3 modificare un elemento della lista \n 4 rimuovere un elemnto")

    scelta = int(input("dammi la tua scelta: "))


    match scelta:
        
        case 1:
            print(lista)
            s = int(input("vuoi fare altre operazioni 1 si 2 no: "))
            if s == 0:
                r = False
            
        case 2:
            
            ni = int(input("scrivi un numero da aggiungere: "))
            s = int(input("vuoi fare altre operazioni 1 si 2 no: "))
            lista.append(s)
            if s == 0:
                r = False
        case 3: 
            print(lista)
            nm = int(input("scrivi il numero che vuoi modificare: "))
            
            c = 0
            while(c<len(lista)): 
                if lista[c] == nm:
                    lista[c] = nm 
                c += 1  
            s = int(input("vuoi fare altre operazioni 1 si 2 no: "))
            if s == 0:
                r = False
                
        case 4:        
            print(lista)
            nm = int(input("scrivi il numero che vuoi eliminare: "))
            
            c = 0
            while(c<len(lista)): 
                lista.pop(nm)
                c += 1  
            s = int(input("vuoi fare altre operazioni 1 si 2 no: "))
            if s == 0:
                r = False    #errato         