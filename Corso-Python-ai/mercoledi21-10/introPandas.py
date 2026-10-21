import pandas as pd

# Creazione di un DataFrame con dati di esempio
data = {
'Nome': ['Alice', 'Bob', 'Carla'],
'Età': [25, 30, 22],
'Città': ['Roma', 'Milano', 'Napoli']
}

# aggiunta di una chiave al dizionario
data["Sesso"] = ["F","M","F"]

df = pd.DataFrame(data)


#print(df.rank())

print(df.head(2)) #stampa le prime due righe
print("=============")
print(df.tail(2)) #le ultime due

print("=============")
print(df.describe())

print("=============")
print(df.info())

print("=======================================")

df_cvs = pd.read_csv("Corso-Python-ai\mercoledi21-10\studenti.csv")


