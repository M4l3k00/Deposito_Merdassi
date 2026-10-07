
verifica = False
lista_risultati = []


while verifica == False : 


    n = int(input("dammi un numero positivo: "))
    if n<0:
        verifica = False
    else:
        verifica = True
        
        lista_risultati.append(n)
        
        somma = 0
        for i in range(1,n+1):
            if i % 2 == 0:
                somma = i + somma
        print(somma)
        
        lista_risultati.append(somma)
        
       
        
        lista_dispari = []
        
        lista_risultati.append("inizio numeri dispari")
        for i in range(1, n+1):
            
            
            if i % 2 !=0:
                lista_dispari.append(i)
                lista_risultati.append(i)
            
        lista_risultati.append("fine numeri dispari")
        print(lista_dispari)
        
        primo = True

        for i in range(2, n):
            if n % i == 0:
                primo = False
                break

        if primo:
            print("numero primo", n)
            lista_risultati.append(n)
        else:
            print(n, "non è primo")
print(lista_risultati)