# %%

import pandas as pd

idades = [
    18, 21, 25, 30, 35, 40
]

# %%


series_idades = pd.Series(idades)
series_idades

# %%
media_idades = series_idades.mean()
media_idades
variancia_idades = series_idades.var()
variancia_idades
sumary_idades = series_idades.describe()
sumary_idades
# %%
