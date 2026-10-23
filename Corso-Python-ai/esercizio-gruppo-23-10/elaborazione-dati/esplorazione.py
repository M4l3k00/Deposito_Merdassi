import pandas as pd


def esplora_data_set(data_set):
    print("========dimesioni del dataset===============")
    print(data_set.shape)
    
    print("/n================ informazioni sul dataset==============")
    data_set.info()
    
    print("==========valori mancanti per colonna================")
    print(data_set.isnull().sum())
    
    print("==========valori duplicati per colonna================")
    print(data_set.duplicated().sum())
    
    print("statistiche descrittive")
    print(data_set.describe())
    
ds_fornitori = pd.read_csv("Corso-Python-ai/esercizio-gruppo-23-10/dati-sporchi/fornitori.csv")
     
    
print("=============================================FORNITORI==============================================")
 
esplora_data_set(ds_fornitori)  
    
    