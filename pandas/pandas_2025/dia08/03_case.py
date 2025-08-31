# %%
import pandas as pd
import os

# %%


def read_file(file_name: str):
    df_geral = (
        pd.read_csv(f"../ipea/{file_name}.csv", sep=";")
        .rename(columns={"valor": f"{file_name}"})
        .set_index(['nome', 'período'])
        .drop(columns=['cod'], axis=1)
    )
    
    return df_geral

# %%
file_names = os.listdir("../ipea")
file_names

# %%

dfs = []
for i in file_names:
    file_name = i.split(".")[0]
    dfs.append(read_file(file_name))
    
dfs
# %%

df_full = (
    pd.concat(dfs, axis=1)
    .reset_index()
    .sort_values(["período", "nome"])
    )
df_full
# %%
