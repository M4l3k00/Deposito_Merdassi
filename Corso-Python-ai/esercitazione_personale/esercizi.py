"""Data una lista di numeri interi, crea una nuova lista contenente gli stessi numeri senza 
duplicati, mantenendo l'ordine della prima occorrenza.
Esempio: [4, 2, 4, 7, 2, 9]
Risultato atteso: [4, 2, 7, 9]
Vincolo: prova a risolverlo usando un ciclo for, senza trasformare la lista in un set."""

lista_dup = [4, 2, 4, 7, 2, 9]

lista_nuova = []


for numero in lista_dup:
    
    if numero not in lista_nuova:
        lista_nuova.append(numero)
        
        
print(lista_nuova)
        
        
"""Trovare il secondo numero più grande
Base
Liste e confronti
15 min

Scrivi una funzione che restituisca il secondo valore più grande di una lista di interi.

Esempio: [10, 5, 20, 8, 20, 15]

Risultato atteso: 15

Vincoli: non usare sort() o sorted(). Decidi come gestire una lista che non contiene due valori distinti."""



lista = [10, 5, 20, 8, 20, 15]
lista_new = []
max = 0
secondoMax = 0

for numero in lista:
    
    if numero>max:
        max = numero
        

for numero in lista:
    
    if numero != max:
        lista_nuova.append(numero)
        

for numero in lista_nuova:
    
    if numero>secondoMax:
        secondoMax = numero
    
print(secondoMax)



"""Scrivi una funzione che restituisca True se una parola si legge allo stesso modo da sinistra a destra e viceversa.

Esempi: "anna" → True; "python" → False.

Estensione: ignora spazi e differenze tra maiuscole e minuscole. Per esempio, "I topi non avevano nipoti" deve essere riconosciuta come palindroma."""
        
        
parola = "parola"

parola2 = "anna"



def verifica_palindroma(parola: str):
    parolaApp = ""
    
    i = len(parola)-1
    
    while i >=0:
        
        parolaApp += parola[i]
        i -=1
        
    if parola == parolaApp:
        return True
    else:
        return False
        

print(verifica_palindroma(parola2)) 