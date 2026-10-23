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
     
def converti_in_intero_pulito(df, colonna):
  # Crea una copia della serie convertita in stringa
  serie_str = df[colonna].astype(str)

  # Estrae solo le cifre numeriche usando le regular expression
  numeri_estratti = serie_str.str.extract(r"(\d+)", expand=False)

  # Converte in intero usando 'Int64' (il tipo intero di pandas che supporta i valori mancanti NaN)
  return numeri_estratti.astype("Int64")


print("=============================================FORNITORI==============================================")
#ELIMINAZIONE DEI DUPLICATI PER FORNITORI
ds_fornitori = ds_fornitori.drop_duplicates()
esplora_data_set(ds_fornitori)  




##Rendere tempi di consegna degli interi 
#Converti la colonna desiderata in interi

ds_fornitori['tempo_consegna_giorni'] = ds_fornitori['tempo_consegna_giorni'].astype(int)

#Salva il file SENZA includere l'indice automatico
ds_fornitori.to_csv('Corso-Python-ai/esercizio-gruppo-23-10/dati-sporchi/fornitori_modificato.csv', index=False)

def converti_in_intero_pulito(ds_fornitori, 'tempo_consegna_giorni'):
    ds_fornitori['tempo_consegna_giorni'] = ds_fornitori['tempo_consegna_giorni'].astype(int)
    print(ds_fornitori['tempo_consegna_giorni'].head(10))
    return ds_fornitori

#trasformare il rating facendolo limitante da 1 a 5 in interi con stringhe eliminate
# 1. Converte la colonna in numerico: eventuali stringhe o testo diventano NaN (valori mancanti)


ds_fornitori['rating'] = pd.to_numeric(ds_fornitori['rating'], errors='coerce') # pd.to_numeric() prova a convertire la colonna 'rating' in numeri.
                                                                            # errors='coerce' è fondamentale: dice a Python che se incontra stringhe, testo o valori non validi, 
                                                                            # non deve bloccarsi con un errore, ma deve trasformarli in NaN (valori nulli/mancanti).





# 2.  Elimina le righe che contengono NaN (questo rimuove tutte le stringhe e i valori vuoti)


ds_fornitori = ds_fornitori.dropna(subset=['rating'])   # .dropna() rimuove le righe del DataFrame. 
                                                        # subset=['rating'] specifica di controllare solo la colonna 'rating' e cancellare la riga se c'è un NaN.
                                                        # In questo modo eliminiamo tutte le righe che contenevano stringhe o celle vuote.



# 3. Mantieni solo i valori compresi tra 1 e 5 (inclusi)

ds_fornitori = ds_fornitori[ds_fornitori['rating'].between(1, 5)] # df['rating'].between(1, 5) restituisce una serie di True/False controllando quali numeri sono tra 1 e 5 (inclusi).
                                                                # Inserendo questo controllo dentro df[...] filtriamo il DataFrame tenendo solo le righe valide.


# 4. Converte definitivamente i valori rimasti in numeri interi
ds_fornitori['rating'] = ds_fornitori['rating'].astype(int)

# 5. Salva il nuovo file CSV senza includere l'indice
ds_fornitori.to_csv('Corso-Python-ai/esercizio-gruppo-23-10/dati-sporchi/fornitori_modificato.csv', index=False)






#Trasformare la colonna attivo in soli si e no, sostituendo i campi Na e stringhe in SI o NO

ds_fornitori = ds_fornitori.dropna(subset=['rating'])   # .dropna() rimuove le righe del DataFrame. 
                                                        # subset=['rating'] specifica di controllare solo la colonna 'rating' e cancellare la riga se c'è un NaN.
                                                        # In questo modo eliminiamo tutte le righe che contenevano stringhe o celle vuote.












    