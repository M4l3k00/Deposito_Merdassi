import pandas as pd

data_multi = {
    'Paese': ['Italia', 'Italia', 'Francia', 'Francia'],
    'Anno': [2023, 2024, 2023, 2024],
    'Vendite': [120, 135, 110, 118]
}

df_multi = pd.DataFrame(data_multi)

# Creo un indice gerarchico con Paese e Anno
df_multi = df_multi.set_index(['Paese', 'Anno'])

print("\nDataFrame con MultiIndex:")
print(df_multi)










