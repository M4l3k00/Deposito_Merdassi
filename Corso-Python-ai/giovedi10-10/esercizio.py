lista_numeri = [[1, 3], 
                [2, 6], 
                [1,7],
                [5, 8]]

risultato = []

fine_precedente = lista_numeri[0][0]

for i in range(len(lista_numeri)):

    inizio = lista_numeri[i][0]
    fine = lista_numeri[i][1]

    # se parte prima della fine del precedente, taglio la parte sovrapposta
    if inizio < fine_precedente:
        inizio = fine_precedente

    # se dopo il taglio resta qualcosa, lo salvo
    if fine > inizio:
        risultato.append([inizio, fine])
        fine_precedente = fine

for i in range(len(risultato)):
    if i > 0:
        print("  ", end="")
    print(str(risultato[i][0]) + str(risultato[i][1]), end="")
print()