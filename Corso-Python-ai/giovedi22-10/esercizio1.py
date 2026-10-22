import pandas as pd

df_csv = pd.read_csv("Corso-Python-ai/giovedi22-10/vendite_fittizie_pandas.csv")

print(df_csv)

df_pivottato = df_csv.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')

print(df_pivottato)


df_group = df_csv.groupby('Prodotto')['Vendite'].mean()

print(df_group)


#------------------------------------------



