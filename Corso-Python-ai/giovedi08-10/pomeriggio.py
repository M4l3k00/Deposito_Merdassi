

def esempio():
    print("Inizio")
    yield "primo"
    print("Dopo il primo")
    yield "secondo"
    print("Fine")

gen = esempio()
print(next(gen))
print(next(gen))
#print(next(gen)) errore


def decoratore(funzione):

    def wrapper():

        print("Prima dell'esecuzione della funzione")

        funzione()

        print("Dopo l'esecuzione della funzione")

    return wrapper


@decoratore
def saluta():

    print("Ciao!")


saluta()