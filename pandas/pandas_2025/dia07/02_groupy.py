# %%
import pandas as pd
# %%
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()
# %%

transacoes.groupby(by="IdCliente").count()
# %%
summary = (transacoes.groupby(by="IdCliente", as_index=False).agg({
    'IdTransacao': ['count'],
    'QtdePontos': ['sum', 'mean']
}))

summary[('QtdePontos', 'mean')]
summary
# %%
summary.columns
# %%
summary.columns = ['IdCliente', 'QtTransacao', 'totalPontos', 'avgPontos']

summary
# %%
