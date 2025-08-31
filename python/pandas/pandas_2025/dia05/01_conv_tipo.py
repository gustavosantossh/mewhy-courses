# %%
import pandas as pd
# %%

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head() # Dataframe
# %%

df['QtdePontos'] # Serie do tipo int
type(df['QtdePontos']) # Tipo Series
# %%

# Converter para outro tipo use: astype()
df['QtdePontos'].astype(float)
# %%

replace = {'old value': 'new value'}

df['DtCriacao'] = pd.to_datetime(df['DtCriacao'].replace(' UTC', '', regex=True), format='mixed')
# pd.to_datetime()

# %%
df['DtCriacao'].dt.month
df['DtCriacao'].dt.day
# %%
