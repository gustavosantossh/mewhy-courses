# %%
import pandas as pd
# %%

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()
# %%

def get_last_id(element: str):
    return element.split("-")[-1]

df["IdCliente"].apply(get_last_id)
# %%
