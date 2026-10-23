import pandas as pd

df_candy_data = pd.read_csv("Corso-Python-ai/venerdi_test_pratico/candy-data.csv")
df_candy_vendite = pd.read_csv("Corso-Python-ai/venerdi_test_pratico/candy-vendite.csv")


def cerca_caramella(nome):
    r = df_candy_vendite[df_candy_vendite["competitorname"].str.lower()==nome.lower()]
    
    if r.empty:
        print("caramella non trovata")
    else:
        print(r[["competitorname", "unita_vendute"]])

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


#print("======================Candy Data============================")
#esplorazione(df_candy_data)
#print("======================Candy Data============================")
#esplorazione(df_candy_vendite)


prodotto_piu_venduto = df_candy_vendite.loc[df_candy_vendite["unita_vendute"].idxmax()]

print("candy piu venduta:", prodotto_piu_venduto["competitorname"])
print("unita vendute:", prodotto_piu_venduto["unita_vendute"])



cerca_caramella("Lemonhead")


df_candy_vendite["fatturato"] = (df_candy_vendite["unita_vendute"] * df_candy_vendite["prezzo_euro"])

vendite_area = df_candy_vendite.groupby("area_vendita")["fatturato"].sum()


print("fatturato per area: ", vendite_area)