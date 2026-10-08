import random


#1 
def inserisci_numero():
    n = int(input("dDammi un numero intero positivo: "))
    while n <= 0:
        n = int(input("il numero deve essere positivo: "))
    return n


#2 
def genera_lista(n):
    lista = []
    while len(lista) < n:
        lista.append(random.randint(1, n))  
    return lista


#3 
def somma_pari(lista):
    somma = 0
    for i in lista:
        if i % 2 == 0:
            somma = somma + i
    print("somma dei numeri pari:", somma)
    return somma






#4 
def stampa_dispari(lista):
    
    
    dispari = []
    
    
    for i in lista:
        
        if i % 2 != 0:
            dispari.append(i)
    print("numeri dispari:", dispari)


#5 
def e_primo(numero):
    
    if numero < 2:  
        return False
    
    for i in range(2, numero):
        if numero % i == 0:
            return False
    
    return True


#6 
def stampa_primi(lista):
    lista_primi = []
    for i in lista:
        if e_primo(i):
            lista_primi.append(i)
    print("numeri primi nella lista:", lista_primi)


# 
def somma_totale_prima(lista):
    somma_totale = 0
    for i in lista:
        somma_totale = somma_totale + i

    if e_primo(somma_totale):
        print( somma_totale, "è un numero primo")
    else:
        print( somma_totale, "no  primo")


n = 0
lista = []
scelta = -1
 
while scelta != 0:
   
    print("1. inserisci un numero ")
    print("2. genera la lista")
    print("3. somma dei numeri pari ")
    print("4. stampa i numeri dispari ")
    
    print("5. erifica se un numero è primo")
    print("6. stampa i numeri primi della lista")
    print("7. la somma di tutti i numeri è primo?")
    print("0. Esci")
 
    scelta = int(input("Scegli un'opzione: "))
 
    match scelta:
        case 1:
            n = inserisci_numero()
            lista = []
            print(n)
        case 2:
            if n == 0:
                print("prima devi inserire n op 1.")
            else:
                lista = genera_lista(n)
                print(lista)
        case 3:
            if len(lista) == 0:
                print("Prima devi generare la lista op 2.")
            else:
                somma_pari(lista)
        case 4:
            if len(lista) == 0:
                print("Prima devi generare la lista op2")
            else:
                stampa_dispari(lista)
        case 5:
            numero = int(input("verifica numero primo "))
            print(numero, "è primo:", e_primo(numero))
        case 6:
            if len(lista) == 0:
                print("Prima devi generare la lista op2")
            else:
                stampa_primi(lista)
        case 7:
            if len(lista) == 0:
                print("Prima devi generare la lista op2")
            else:
                somma_totale_prima(lista)
        case 0:
            print("ciao")
        case _:
            print("opzione non esistente.")
 