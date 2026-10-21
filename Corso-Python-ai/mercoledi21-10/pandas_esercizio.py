import pandas as pd


df_csv = pd.read_csv("Corso-Python-ai/mercoledi21-10/studenti.csv")

print(df_csv)

df_csv["materia_preferita"] = [
    "Informatica",
    "Matematica",
    "Storia",
    "Inglese",
    "Scienze",
    "Italiano",
    "Fisica",
    "Arte",
    "Educazione fisica",
    "Geografia"
]


print("=================")
print(df_csv)

print("=================")
df_csv["media_alta"] = df_csv["media_voti"] >= 7
print(df_csv)

print("=================")
print(df_csv["media_voti"].mean()) #stampa la media dei voti


print("=================")
print(df_csv["media_voti"].max()) #maggiore dei voti


print("=================")
print(df_csv[df_csv["media_voti"]>7]) #stampa le righe con media maggiore di 7


df_csv.to_csv("Corso-Python-ai/mercoledi21-10/studenti_a.csv", index=True)