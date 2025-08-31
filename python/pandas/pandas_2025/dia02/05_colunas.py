# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

# %%
df.info(memory_usage='deep')
# %%
# df = df.rename(columns={"DtCriacao": "created_at"}) # Rename cria um dataframe novo
df.rename(columns={"DtCriacao": "created_at"}, inplace=True) # Usando o inplace ele usa o propio dataframe sem precisar criar um novo.

# %%

colunas = df.columns.to_list()
colunas.sort()
colunas

# %%
df[colunas]
# %%
