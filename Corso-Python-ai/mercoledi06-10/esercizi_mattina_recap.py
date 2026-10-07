#es 1
'''
numero = int(input("dammi un numero"))


if numero % 2 ==0:
    print("pari")
else:
    print("dispari")
'''

#es 2
'''
n=-1
while(n<=0):
        
    n = int(input("dammi un numero"))
    while(n>0):
        print(n)
        n -= 1
        if n == 0:
            scelta =int(input("vuoi inserire un'altro numer 1 si 2 no"))
            if scelta == 1:
                n = int(input("dammi un numero"))
                '''
                
                
#es 3

'''
lista_numeri = []
lista_q = []

print("scrivi una lista di numeri dicidendo numero di elementi e elementi\n")
d = int(input("dammi la dimensione della lista: "))

while len(lista_numeri)<d:
    
    e = int(input("scrivi il numero: "))
    lista_numeri.append(e)
    
print("la tua lista è ", lista_numeri)
    
for i in lista_numeri:
    
    q = i**2
    lista_q.append(q)

print("lista quadrata ", lista_q)
'''


#es 4

lista_x = []

p = int(input("dammi la dimensione della lista: "))

while len(lista_x)<p:
    
    n = int(input("scrivi il numero: "))
    lista_x.append(n)
    
max = 0
for i in lista_x:
    
    
    if i > max:
        max = i
print("numero massimo ", max)

dimensione_lista = len(lista_x)

#3

if dimensione_lista == 0:
    print("lista vuota")
else:
    print(max, " ", lista_x)



c = 0
#prenod gli elementi dalla posizione c
while lista_x[c:]:
    c=c+1 
    
print(c)
    