# %%
import pandas as pd

# %%
idades = [
    24, 31, 19, 45, 22, 38, 27, 60, 33, 29
]

nomes = [
    "Ana", "Bruno", "Carla", "Daniel", "Bruno",
    "Eduardo", "Fernanda", "Gustavo", "Helena", "Isabela"
]

# %%

series_idades = pd.Series(idades)
series_idades = series_idades.sort_values()
series_idades


# %%
series_idades[0] # Pega o valor pelo index

series_idades.iloc[-1] # Iloc ignora o index e pega pela posição ignorando as chaves

series_idades.iloc[0]

series_idades.iloc[:3]

series_idades.iloc[::-1] # Do ultimo elemento para o primeiro

# %%
idades = [
    24, 31, 19, 45, 22, 38, 27, 60, 33, 29
]

nomes = [
    "Ana", "Bruno", "Carla", "Daniel", "Bruno",
    "Eduardo", "Fernanda", "Gustavo", "Helena", "Isabela"
]
# %%

series_idades = pd.Series(idades, index=nomes)
series_idades
# %%
series_idades["Ana"]
# %%
series_idades["Bruno"]
# %%
