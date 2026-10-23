import numpy as np
import pandas as pd

matrice = np.array([[1,2],[3,4],[5,6]]) #ndarray

print(matrice)


matrice2 = matrice[0, 0:2]

#print(matrice2)



array =np.linspace(1,100,15)

print(array)
print(array.sum())
print(array.mean())


matrice5x5 = np.random.randint(10,20, size=(5,5))
print(matrice5x5)
print("===================================================")


data = {
    'nome':["giada", "marco", "francesco", "francesca"],
    'Età': [84, 30, 22,60],
    'Città': ['Roma', 'Milano', 'Napoli', "foggia"]
}

df = pd.DataFrame(data)





