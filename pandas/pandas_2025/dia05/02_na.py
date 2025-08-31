# %%

import pandas as pd

# %%

clientes = pd.read_csv('../data/clientes.csv', sep=';')

clientes

# %%

clientes.dropna(how='all')
# how='any' -> Dropa a linha caso aja ao menos um Na na linha
# how='all' -> Dropa a linha caso aja Na na linha toda.

# %%


dataset = pd.DataFrame({
    "nome": ["João", None, "Maria", "José", "Ana", "Carlos", None, "Fernanda", "Paulo", None],
    "idade": [28, 35, 24, 40, 22, None, 31, 27, None, 45],
    "cidade": ["SP", "RJ", "BH", None, "SP", "POA", "RJ", None, "BH", "SP"],
    "salario": [3000, None, 2800, 5000, 2500, 3200, None, 4100, None, 2900]
})

dataset.dropna(how='any', subset=["nome","salario"])
# %%
dataset.fillna(0)
# %%
medias = dataset[["idade", "salario"]].mean()
dataset.fillna(medias)
# %%
