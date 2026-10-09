<<<<<<< HEAD
import ut

scelta=input("")

while scelta!= "stop":
    scelta=input("Scegli un numero da 1 a 4 oppure stop")

    if scelta=="1":
        input_calcolatrice=input("Scegli un operatore tra +, -, *, /")
        ut.calcolatrice(input_calcolatrice)
    elif scelta=="2":
        pass
    elif scelta=="3":
        pass
    elif scelta=="4":
        pass
    elif scelta=="stop":
        print ("Grazie per aver usato la calcolatrice")
        break
    
    else: 
          print("hai sbagliato")

    
=======
import ut as u



>>>>>>> 3ad5e5ebfa8f250e5d44548e3ab895b37ab6ea6f
