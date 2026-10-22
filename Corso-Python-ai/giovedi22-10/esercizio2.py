import pandas as pd

df_iscritti = pd.read_csv("Corso-Python-ai/giovedi22-10/iscritti.csv")
df_presenze = pd.read_csv("Corso-Python-ai/giovedi22-10/presenze.csv")
df_costi_abbonamenti = pd.read_csv("Corso-Python-ai/giovedi22-10/costi_abbonamento.csv")


print("=========================")
print(df_iscritti)
print("========presenze=================")

print(df_presenze)
print("=========================")

print(df_costi_abbonamenti)
print("=========================")

print("==============pulizia iscritti==================")
print("valori nulli")
print(df_iscritti.isnull())
df_iscritti["Eta"] = df_iscritti["Eta"].fillna(df_iscritti["Eta"].median())
print("valori nulli")
print(df_iscritti.isnull())
print(df_iscritti.duplicated())
df_iscritti = df_iscritti.drop_duplicates()
#unione iscritti con costi abbonamenti

spesa_a_persona = pd.merge(df_iscritti, df_costi_abbonamenti, on='Tipo_Abbonamento')
print(spesa_a_persona)


#print("=========================") # non è una valutazione corretta
#corso_a_persona = pd.merge(df_iscritti, df_presenze, on='Citta')
#print(corso_a_persona)


df_group_iscritti_per_citta = df_iscritti.groupby('Citta')['Nome'].count()
print("=========================")
print(df_group_iscritti_per_citta)


