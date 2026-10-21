import pandas as pd

df_csv = pd.read_csv("Corso-Python-ai/mercoledi21-10/dataset_vendite_pandas.csv")

print(df_csv)
#aggiungere una colonna quantita * prezzo unitario

df_csv["Totale vendite"] = df_csv["Prezzo Unitario"] * df_csv["Quantità"]

print(df_csv)

#raggruppare i dati per prodotto e calcolare il totale venddita di ciascuno

groupped_df = df_csv.groupby("Prodotto")["Totale vendite"].sum()
print(groupped_df)


#trovare il prodotto piu venduto per quantita

prodotto_quantita = df_csv.groupby("Prodotto")["Quantità"].sum()
print(prodotto_quantita)
print("========================")
prodotto_quantita.idxmax()
quantita_max = prodotto_quantita.max()
print(prodotto_quantita.idxmax(), " ", prodotto_quantita.max() )

print("========================")
#citta con maggior numero di vendite

citta_vendite = df_csv.groupby("Città")["Totale vendite"].sum()
print(citta_vendite)

print("========================")


nuovo_data = df_csv[df_csv["Totale vendite"]>=1000]

print(nuovo_data)

print("========================")
citta_quantita = df_csv.groupby("Città")["Quantità"].sum()

print(citta_quantita)