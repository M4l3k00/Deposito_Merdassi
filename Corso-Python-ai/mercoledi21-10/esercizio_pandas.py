import pandas as pd
import numpy as np
#dataframe
df_csv = pd.read_csv("Corso-Python-ai/mercoledi21-10/persone.csv")

#le prime 5 righe
print("==============================")
print(df_csv.head(5)) #stampa le prime due righe

print("==============================")
print(df_csv.tail(5))

print("==============================")
print(df_csv.info())

print("=================")
print(df_csv["salario"].mean()) #media
print(df_csv["salario"].median()) #median
print(df_csv["salario"].std()) #deviazione standard


print("=========duplicati========")
print(df_csv.duplicated)

print(df_csv.duplicated(keep=False))

print("=========valori mancanti========")
print(df_csv.isna())

print(df_csv[df_csv["salario"].isna()])

df_csv["salario"] = df_csv["salario"].fillna(df_csv["salario"].mean())

print(df_csv)


print("==============================")


df_csv["categoria_eta"] = np.where(
    df_csv["eta"] >= 18,
    "Maggiorenne",
    "Minorenne"
)
print(df_csv)
df_csv.to_csv("Corso-Python-ai/mercoledi21-10/persone_a.csv", index=True)







