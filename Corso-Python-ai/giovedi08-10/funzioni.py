'''

def somma(x,y):
    return x+y


print(somma(3,4))




def saluta(nome):
    print("ciao ", nome)


nomeSalutare = input("dammi nil nome da salutare")

saluta(nomeSalutare)
'''

def materiaP(materia = " 'non hai iserito la materia' "):
    print("materia preferita: ", materia)

def studente(matricola, nome, cognome):
    print("sei ",nome," ", cognome, " con matricola: ", matricola)
    
    materia = input("dammi la tua materia preferita: ")
    
    while materia =="":
        
            materia = input("dammi la tua materia preferita: ")
            
    materiaP(materia) 
    
studente(333,"abc","ttt")   
    