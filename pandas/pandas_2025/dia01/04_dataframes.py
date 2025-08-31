# %%
import pandas as pd

# %%
idades = [
    24, 31, 19, 45, 22, 38, 27, 60, 33, 29
]

nomes = [
    "Ana", "Bruno", "Carla", "Daniel", "Bruno",
    "Eduardo", "Fernanda", "Helena", "Isabela" ,"Gustavo",
]
# %%
df = pd.DataFrame()
df
# %%
df["nomes"] = nomes
df["idades"] = idades
df
# %%
df.loc[5]["nomes"]

# %%
