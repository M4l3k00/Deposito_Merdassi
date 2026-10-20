import numpy as np
#1

ripetibile = True

while ripetibile:

    array_casuale = np.random.randint(1,100, size=15)

    print(array_casuale.sum())
    print(array_casuale.mean())
    print(array_casuale)

    print("============")
#2

    matrice_5x5 = np.random.randint(1,100,size=(5,5))
    print(matrice_5x5)
    print("============")
    colonna_seconda = matrice_5x5[:,1]
    print(colonna_seconda)

    riga_terza = matrice_5x5[2]
    print(riga_terza)

    diagonale = np.diag(matrice_5x5)

    print(diagonale.sum())

#3

    matrice_4x4 = np.random.randint(10,51,size=(4,4))

    print(f"0,1: {matrice_4x4[0,1]} 1,3: {matrice_4x4[1,3]} 2,2: {matrice_4x4[2,2]} 3,0: {matrice_4x4[3,0]}")

    print(matrice_4x4[0])
    print(matrice_4x4[2])


    matrice_4x4[0,1] +=10
    matrice_4x4[1,3] +=10
    matrice_4x4[2,2] +=10
    matrice_4x4[3,0] +=10

    print(matrice_4x4)
    
    with open("dati_.txt", "w", encoding="utf-8") as file:
            file.write(f"somma di array di numeri casuali da 1 a 99: {array_casuale.sum()}\n")
            file.write(f"media di array di numeri casuali da 1 a 99: {array_casuale.mean()}\n")
            file.write(f"stampa di array di numeri casuali da 1 a 99: {array_casuale}\n")
            file.write(f"seconda colonna della matrice 5x5: {colonna_seconda}\n")
            file.write(f"terza riga della matrice 5x5: {riga_terza}\n")
            file.write(f"diagonale della matrice 5x5: {diagonale}\n")
            file.write(f"stampa della matrice 5x5: {matrice_5x5}\n")
            file.write(f"stampa della matrice 4x4: {matrice_4x4}\n")
            file.write(f"elementi 0,1: {matrice_4x4[0,1]} 1,3: {matrice_4x4[1,3]} 2,2: {matrice_4x4[2,2]} 3,0: {matrice_4x4[3,0]}")
            file.write(f"prima riga matrice 4x4: {matrice_4x4[0]}\n")
            file.write(f"terza riga matrice 4x4: {matrice_4x4[3]}\n")
            
    scelta = int(input("vuoi sovrascrivere il file 1 si 2 no: "))
    if scelta == 2:
        ripetibile = False





