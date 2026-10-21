lista_numeri = [1,4,6,9,22,18,2,3,14]
target =0


def two_sum(lista_numeri, target):
    
    for numero1 in lista_numeri:
        
        for numero2 in lista_numeri:
            
            if numero1 + numero2 == target:
                
                print(lista_numeri.indexOf(numero1))