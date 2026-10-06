#esercizio 1 

'''
x = int(input("dammi un numero"))

if x == 10:
    y = int(input("quanto fa 10 -3"))
    if y == x-3: 
        print("risposta corretta")
        z = int(input("dammi il modulo di 7 / 2"))
        if z == 1:
            print("corretto")
    

        else :
            print("sbagliato")
    
#esercizio 2
print("hai una lista di numeri e puoi usare questo programma crud\n")
print("programma crud, operazioni 1: modifica, 2 aggiungi, 3 elimina\n")

lista = [1,2,3,4,5,88,9,3]

print(lista)


operazione = int(input("dammi l'operazione da fare"))

if operazione == 1 :
    
    i = int(input("dammi l'indice dell'elemento della lista che vuoi modificare"))
    e = int(input("dammi l'elemento"))
    
    lista[i] = e
    print(lista)
    
elif operazione == 2:
    
    a = int(input("dammi l'elemento che vuoi aggiungere alla lista"))
    lista.append(a) 
    print(lista)
    
elif operazione == 3:
    
    d = int(input("dammi l'elemento che vuo eliminare"))
    lista.remove(d)
    print(lista)
    
else :
    
    print("operazione non valida")    
    '''

# esercizio mattina 
'''

listap = ["mare","perer","acqua", "pomodoro"]
listan= [1,2,3,4,5,6]

print(listap, '\n')
print(listan, '\n')

scelta = int(input("1 l1 2 l2"))



if scelta ==1 :
    sceltap = int(input("op 1 aggiungere 2 modificare"))
    
    if sceltap == 1:
        p = input("cosa vuoi aggiunere")
        listap.append(p) 
        print(listap)  
    
    elif sceltap ==2:
         print(listap)
         elemento_indice =  int(input("dammi l'indice da modificare"))
         elemento = input("dammi l'elemento")
         listap[elemento_indice] = elemento
    
    else:
        print("scelta non v")
         
elif scelta == 2:
    
    sceltan = int(input("op 1 aggiungere 2 eliminare"))
    
    if sceltan == 1:
          pn = int(input("cosa vuoi aggiunere"))
          listan.append(pn) 
          print(listan)  
        
    elif sceltan == 2:
         
         print(listan)
         elemento_r = int(input("dammi l'elemento che vuoi rimuovere"))
         listan.remove(elemento_r)
         print(listan)

    else:
        print("scelta non v")
                
else :
    print("scelta non v")


'''


#esercizio pomeriggio 1

eta = int(input("dammi la tua eta: "))

maggiorenne = eta >= 18

#print(maggiorenne)


match maggiorenne:
    
    case True: 
        print("sei maggiorenne gurada")
    case False:
        print("non puoi guardare")
        
        
        
#esercizio 2
numero1 = int(input("dammi il primo numero: "))

numero2 = int(input("dammi il secondo numero: "))


op = input("dammi l'operazione: ")

match op:
    
    case "+":
        print(numero1+numero2)
    case "-":
        print(numero1-numero2)
    case "*":
        print(numero1*numero2)
    case "/":
        if numero2 == 0:
            print("non puoi dividere per 0")
        else:
            print(numero1/numero2)
    case "%":
        print(numero1%numero2)
    case _:
        print("op non valida")