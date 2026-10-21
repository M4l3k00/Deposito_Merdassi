import numpy as np

ripetibile = True

print("Creare una nuova matrice 2D di dimensioni specificate da utente con numeri casuali\n")
    
    
righe = int(input("dammi il numero delle righe: "))
colonne = int(input("dammi il numero delle colonne : "))
n1 = int(input("dammi il numero : "))
n2 = int(input("dammi il numero  : "))

matrice = np.random.randint(n1,n2,size=(righe,colonne))
print(matrice)

while ripetibile:
    

    print("\n"
          "1.Estrarre e stampare la sotto-matrice centrale.\n"
          "2.Trasporre la matrice e stamparla\n"
          "3.Calcolare e stampare la somma di tutti gli elementi della matrice\n"
          "4.Uscire dal programma\n"
          "5.scegliere di creare una seconda matrice delle stesse dimensioni della prima e moltiplicarle elemento per elemento e stampare il risultato.\n"
          "7.Calcolo della Media degli Elementi della Matrice\n")
    
    scelta = int(input("dammi la tua scelta: "))
    
    match scelta:
        
        case 1:
            centro_r = righe // 2
            centro_c = colonne // 2

            sotto_matrice = matrice[
            centro_r - 1:centro_r + 2,
            centro_c - 1:centro_c + 2
                        ]

            print("Sotto-matrice centrale:")
            print(sotto_matrice)
            
        case 2:
             
            print(matrice)
            print("=================")
            print(matrice.T)
            
        case 3:
            print(matrice.sum())
            
        case 4:
            ripetibile = False
           
                
            break
        
        case 5:
            n1 = int(input("dammi il numero : "))
            n2 = int(input("dammi il numero  : "))
            matrice2 = np.random.randint(n1,n2,size=(righe,colonne))
            print(matrice2)
            
            print("multiplicazione della matrice di prima con quella di adesso\n")
            
            print(matrice*matrice2)
            
            
        case 6:
            print(matrice.mean())

        case 7:
            
            if righe == colonne:
                
                determinante = np.linalg.det(matrice) #detereminante
                print(determinante)
                
            else:
                print("non è possibile fare il determinante della matrice\n")
                
        case _:
            print("scelta non valida")
            



