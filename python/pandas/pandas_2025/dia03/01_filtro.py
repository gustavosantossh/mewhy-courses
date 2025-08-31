# %%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
df.head() # head() -> pega os 5 primeiros elementos

# %%

filtro = df['QtdePontos'] >= 50

df[filtro]
# %%
filtro = (df['QtdePontos'] >= 50) & (df['QtdePontos'] <= 100)

df[filtro]