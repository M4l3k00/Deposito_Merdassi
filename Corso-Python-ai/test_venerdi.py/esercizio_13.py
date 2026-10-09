

con = True
lista = []
while con:
    
    scelta = int(input("dammi la tua scelta\n 1. inserisci elemento nel fondo nella lista\n 2. inserisci elemento in una posizione specifica\n3. modifica un elemento\n 4. elimina la lista,\n 5. stampare la lista\n 6. uscire dal programma"))
    
    match scelta:
        case 1:
            
            elemento = input("dammi l'elemento che vuoi inserire: ")
            lista.append(elemento)
        
        case 2:
            
            elemento = input("dammi l'elemento che vuoi inserire: ")
            posizione = int(input("dammi la posizione dove inserire l'elemento"))
            lista.insert(posizione,elemento)
            print(lista)
            
        case 3:
            
            elemento = input("dammi l'elemento che vuoi modificare: ")
            
            for i in range(len(lista)):
                
                if lista[i] == elemento:
                    nele = input("inserisci un nuovo valore: ")
                    lista[i] = nele
            print(lista)    
        
        case 4:
            lista.clear()
            print(lista)
                
        case 5:
            print(lista)
            
            
        case 6:
            con = False
            
        case _:
            print("scelta non valida")