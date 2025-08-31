# %%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes
# %%

df_clientes.head(20) # Retorna os 5 primeiros elementos do dataset
# %%
df_clientes.tail() # Retorna os 5 ultimos elementos do dataset 
# %%
df_clientes.sample(10) # Retorna uma ou mais amostra(s) aleatoria dos dados
# %%
df_clientes.max() # Valor maximo
# %%
df_clientes.min() # Valor minimo

# %%
df_clientes.shape # Retorna uma tupla com a quantidade de linhas e colunas
# %%
df_clientes.columns # Retorna as colunas do dataset
# %%
df_clientes.index # Retorna os index do dataset
# %%

df_clientes.info(memory_usage='deep') # Retorna as informações do dataset
# %%
df_clientes.dtypes
# %%
