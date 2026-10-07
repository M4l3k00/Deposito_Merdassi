'''n = int(input("dammi un numero: "))



while n>=0:
    n-=1
    print(n)
    
    if n == 0:
        ri = int(input("vuoi ripetere il ciclo 1 si 2 no: "))
        if ri == 1:
            n = int(input("dammi un numero: "))
     '''       
            
#esercizio 2
'''
numeri_primi = []

while len(numeri_primi) < 5:
    x = int(input("dammi un numero: "))

    primo = x > 1
    
    for i in range(2, x):
        if x % i == 0:
            primo = False
    if primo:
        numeri_primi.append(x)
        print("numero primo")
    else:
        print("non è un numero primo")

print(numeri_primi)
'''


#esercizio 3

numeri_pari = []
numeri_disp = []



while (len(numeri_pari) < 5 or len(numeri_disp)<5 ):
    
    num = int(input("dammi un numero: "))
    if num % 2 == 0:
        print("numero pari ")
        if len(numeri_pari) >= 5:
            print("non puoi piu inserire numeri pari")
        else:
            numeri_pari.append(num)
    else:
        print("numero disp")
        if len(numeri_disp) >= 5:
            print("non puoi piu inserire numeri dispari")
        
        else:
            
            numeri_disp.append(num)

print(numeri_disp)
print(numeri_pari)