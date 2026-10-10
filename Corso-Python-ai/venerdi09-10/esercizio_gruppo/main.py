
import ut as ut
scelta=input("")

#condizione che si fermera' all'input stop dell'utente 
while scelta!= "stop":
    scelta=input("Scegli un numero da 1 a 4 oppure stop")

#scelta utente degli operatori utilizzabili
    if scelta=="1":
        input_calcolatrice=input("Scegli un operatore tra +, -, *, /")
        ut.calcolatrice(input_calcolatrice) #calcolatrice importata dal file utility
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
          
          
          
          #dfghoiashfgois

