import modulo as m



con = True


while con:
    
    print("che operazione vipi fare:\n")
    scelta = int(input("1 somma\n 2 sottrazione\n 3 moltiplicazione \n 4 divisione \n 5 esci "))
    
    match scelta:
        case 1:
            n1 = int(input("dammi il primo numero: "))
            n2 = int(input("dammi il secondo numero: "))
            
            print(m.somma(n1,n2))
            
        case 2:
            n1 = int(input("dammi il primo numero: "))
            n2 = int(input("dammi il secondo numero: "))
            
            print(m.sottrazione(n1,n2))
            
        case 3:
            n1 = int(input("dammi il primo numero: "))
            n2 = int(input("dammi il secondo numero: "))
            
            print(m.moltiplicazione(n1,n2))
            
        case 4:
            n1 = int(input("dammi il primo numero: "))
            n2 = int(input("dammi il secondo numero: "))
            
            print(m.divisione(n1,n2))
            
        case 5:
            con: False
            
        case _:
            print("ko")
                        
                        
                        