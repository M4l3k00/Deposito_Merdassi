import pandas as pd

#import dei dataset in dataframe
df_candy_data = pd.read_csv("Corso-Python-ai/venerdi_test_pratico/candy-data.csv")
df_candy_vendite = pd.read_csv("Corso-Python-ai/venerdi_test_pratico/candy-vendite.csv")


#validazione sul competitorname dei due dataset --> ci serve per fare bene i merge

df_candy_vendite["competitorname"] = df_candy_vendite["competitorname"].str.lower()
df_candy_data["competitorname"] = df_candy_data["competitorname"].str.lower()

#funzione per cercare una caramella nel dataset di vendite
def cerca_caramella(nome):
    r = df_candy_vendite[df_candy_vendite["competitorname"].str.lower()==nome.lower()]
    
    if r.empty:
        print("caramella non trovata")
    else:
        print(r[["competitorname", "unita_vendute"]])


#funzione per cercare una caramella nel dataset data
def cerca_caramella_data(nome):
    r = df_candy_data[df_candy_data["competitorname"].str.lower()==nome.lower()]
    
    if r.empty:
        print("caramella non trovata")
    else:
        print("trovata")
        
#funzione esplorativa
def esplorazione(dataset):
    print("========le prime 5 righe===============")
    print(dataset.head())
    print("========dimesioni del dataset===============")
    print(dataset.shape)
    print("\n================ informazioni sul dataset==============")
    dataset.info()
    
    print("==========valori mancanti per colonna================")
    print(dataset.isnull().sum())
    
    print("==========valori duplicati per colonna================")
    print(dataset.duplicated().sum())
    
    print("statistiche descrittive")
    print(dataset.describe())
    
print("======================================================================================================================================================================================================================")
print("=============================================================================================  ESPLORAZIONE  =========================================================================================================================")
print("======================================================================================================================================================================================================================")

#nella fase esplorativa non ho notato valori duplicati o nulli ma una differenza di dimensioni nei due dataset uno di 85 e l'altro di 83 ci aiuta nella fase di coerenza
print("======================Candy Data============================")
esplorazione(df_candy_data)
print("======================Candy vendite============================")
esplorazione(df_candy_vendite)




print("======================================================================================================================================================================================================================")
print("=============================================================================================  Verifica Coerenza  =========================================================================================================================")
print("======================================================================================================================================================================================================================")


print("//////////////////1////////////////")
confronto = pd.merge(
    df_candy_data[["competitorname"]],
    df_candy_vendite[["competitorname"]],
    on="competitorname",
    how="outer",
    indicator=True
)
print("////////////////questi dati non sono stati trovati in df_candy_vendite//////////////////")
print(
    confronto[confronto["_merge"] == "left_only"]
)

print("//////////////////////////////////")



#ho utilizzato i set per eliminare i duplicati
print("//////////////////////////////////")
nomi_candy = set(df_candy_data["competitorname"])
nomi_vendite = set(df_candy_vendite["competitorname"])

print("Presenti in candy ma non in vendite:")
print(nomi_candy - nomi_vendite)

print("Presenti in vendite ma non in candy:")
print(nomi_vendite - nomi_candy)
print("//////////////////////////////////")


'''Presenti in candy ma non in vendite:
{'whoppers', 'twizzlers', "werther's original caramel", 'warheads', "welch's fruit snacks"}
Presenti in vendite ma non in candy:
{'candy test b', 'candy test a', 'candy test c'}
//////////////////////////////////'''














prodotto_piu_venduto = df_candy_vendite.loc[df_candy_vendite["unita_vendute"].idxmax()]

print("candy piu venduta:", prodotto_piu_venduto["competitorname"])
print("unita vendute:", prodotto_piu_venduto["unita_vendute"])
cerca_caramella("Lemonhead")

df_candy_vendite["fatturato"] = (df_candy_vendite["unita_vendute"] * df_candy_vendite["prezzo_euro"])

vendite_area = df_candy_vendite.groupby("area_vendita")["fatturato"].sum()

print("fatturato per area: ", vendite_area)