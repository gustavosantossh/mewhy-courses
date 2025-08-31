# %%
import pandas as pd

# %%
df = pd.DataFrame({
    "nome": ["João", "Maria", "Carlos"],
    "clientes": [2, 1, 3]
})

# %%
df_02 = pd.DataFrame({
    "cliente": [1, 2, 3, 4, 5, 6],
    "nome": ["João", "João", "Maria", "Carlos", "Carlos", "Carlos"],
    "idade": [28, 34, 45, 22, 29, 33]
})

# %%

df_02
# %%

pd.concat([df, df_02], ignore_index=True)

# %%
pd.concat([df, df_02], axis=1)

# %%
