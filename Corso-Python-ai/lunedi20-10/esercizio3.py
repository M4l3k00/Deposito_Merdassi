import numpy as np

scelta = True
while scelta:
    array_a = np.linspace(0,10,50)
    #print(array)

    array_b = np.random.random(50)
    #print(array_b)

    #3
    array_somma = array_a+array_b
    #print(array_somma)

    array_somma_ = array_somma[array_somma>5]
    #print(array_somma_)

    somma_array = array_somma_.sum()
    print(somma_array)
    
    with open("dati.txt", "w", encoding="utf-8") as file:
        file.write(f"Primo array: {array_a}\n")
        file.write(f"Random array: {array_b}\n")
        file.write(f"Array somma: {array_somma}\n")
        file.write(f"Array con elementi maggiori di 5: {array_somma_}\n")
        file.write(f"Somma degli elementi: {somma_array}\n")
        
    i = int(input("vuoi sovrascrivere 1 si 2 no: "))
    if i == 2:
        scelta = False
                
        
    
    